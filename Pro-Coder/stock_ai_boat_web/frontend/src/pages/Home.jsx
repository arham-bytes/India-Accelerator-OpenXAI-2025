import React, {useState} from 'react'
import axios from 'axios'
export default function Home(){
  const [csvFile, setCsvFile] = useState(null)
  const [imgFile, setImgFile] = useState(null)
  const [result, setResult] = useState(null)
  const API = (import.meta.env.VITE_API_URL) || 'http://localhost:8000/api'
  const uploadCsv = async ()=>{
    if(!csvFile) return alert('Select CSV')
    const f = new FormData(); f.append('file', csvFile)
    const r = await axios.post(API + '/predict/csv', f)
    setResult(r.data)
  }
  const uploadImg = async ()=>{
    if(!imgFile) return alert('Select image')
    const f = new FormData(); f.append('file', imgFile)
    const r = await axios.post(API + '/predict/image', f)
    setResult(r.data)
  }
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl mb-4">Upload chart CSV or image</h1>
      <div className="bg-slate-800 p-4 rounded-lg">
        <label className="block mb-2">CSV file</label>
        <input type="file" accept=".csv" onChange={e=>setCsvFile(e.target.files[0])} />
        <button onClick={uploadCsv} className="mt-3 px-4 py-2 bg-emerald-500 rounded">Predict CSV</button>
        <hr className="my-4" />
        <label className="block mb-2">Chart image</label>
        <input type="file" accept="image/*" onChange={e=>setImgFile(e.target.files[0])} />
        <button onClick={uploadImg} className="mt-3 px-4 py-2 bg-indigo-500 rounded">Predict Image</button>
      </div>
      {result && (
        <div className="mt-6 bg-slate-800 p-4 rounded">
          <h3 className="text-xl">Prediction</h3>
          <pre className="whitespace-pre-wrap">{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  )
}
