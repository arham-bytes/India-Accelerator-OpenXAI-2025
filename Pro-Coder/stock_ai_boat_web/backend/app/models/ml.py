# Demo ML inference functions (replace with trained models for production)
import numpy as np
import pandas as pd
import io
from PIL import Image
def predict_from_csv(csv_bytes_io, window=20):
    try:
        df = pd.read_csv(csv_bytes_io)
    except Exception as e:
        return {'error':'invalid csv', 'detail': str(e)}
    col = None
    for name in ['close','Close','adj_close','close_price']:
        if name in df.columns:
            col = name; break
    if col is None:
        return {'error':'CSV missing close column', 'columns': list(df.columns)}
    prices = df[col].astype(float).dropna().values
    if len(prices) < 5:
        return {'error':'Not enough points'}
    seq = prices[-window:]
    diffs = np.diff(seq)
    score = float(np.tanh(diffs.mean()))
    if score > 0.05:
        direction = 'up'
    elif score < -0.05:
        direction = 'down'
    else:
        direction = 'neutral'
    conf = min(0.99, abs(score)*2)
    return {'type':'csv','direction':direction,'confidence': round(conf,3),'score': score}
def predict_from_image(image_bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB').resize((128,128))
    except Exception as e:
        return {'error':'invalid image', 'detail': str(e)}
    arr = np.array(img)/255.0
    left = arr[:, :64, :].mean()
    right = arr[:, 64:, :].mean()
    diff = float(right - left)
    if diff > 0.01:
        d = 'up'
    elif diff < -0.01:
        d = 'down'
    else:
        d = 'neutral'
    conf = min(0.99, abs(diff)*50)
    return {'type':'image','direction':d,'confidence': round(conf,3),'diff': diff}
