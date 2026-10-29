import React from 'react'
import { NavLink } from 'react-router'

function App() {
  return (
    <div className='w-full min-h-screen flex flex-col justify-center items-center'>
      <p className='text-3xl font-bold'>Welcome To Auth App</p>
      <div className='w-[18%] h-[40%] py-12 px-4 border-2 m-2 flex justify-between '>
        <NavLink to="/login">
          <button className="px-4 py-2 border-4 border-black font-bold hover:cursor-pointer hover:bg-black hover:text-white">LogIn</button>
        </NavLink>
        
        <NavLink to="/register">
          <button className="px-4 py-2 border-4 border-black font-bold hover:cursor-pointer hover:bg-black hover:text-white">Register</button>
        </NavLink>
      </div>
    </div>
  )
}

export default App
