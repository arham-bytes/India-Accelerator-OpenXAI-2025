import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Signup from './pages/Signup'
export default function App(){
  return (
    <div className="min-h-screen bg-slate-900 text-white">
      <nav className="p-4 flex justify-between items-center">
        <div className="text-xl font-bold">Stock-AI-Boat</div>
        <div className="space-x-4">
          <Link to="/" className="text-slate-300">Home</Link>
          <Link to="/login" className="text-slate-300">Login</Link>
        </div>
      </nav>
      <main className="p-6">
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/signup" element={<Signup/>} />
        </Routes>
      </main>
    </div>
  )
}
