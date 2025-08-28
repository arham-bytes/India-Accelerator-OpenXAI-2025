from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.models.ml import predict_from_csv, predict_from_image
import io, json
router = APIRouter()
@router.post('/csv')
async def predict_csv(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(status_code=400, detail='CSV required')
    content = await file.read()
    res = predict_from_csv(io.BytesIO(content))
    return res
@router.post('/image')
async def predict_image(file: UploadFile = File(...)):
    content = await file.read()
    res = predict_from_image(content)
    return res
