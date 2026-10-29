import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
import App from './App.tsx'
import Login from './components/Login.tsx';
import Register from './components/Register.tsx';
import ResetPassword from './components/ResetPassword.tsx';


createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/register" element={<Register/>} />
      <Route path="/resetpassword" element={<ResetPassword/>} />
    </Routes>
  </BrowserRouter>
)
