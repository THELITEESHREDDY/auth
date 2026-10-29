import React from 'react'
import { Link } from 'react-router'

function ResetPassword() {
  return (
    <div className='w-full min-h-screen  flex  items-center justify-center'>
        <div className='p-3 h-[90%] flex flex-col border-2 items-center justify-center'>
            <div className='h-fit w-fit m-2 '>
                <p className='font-bold text-2xl'>Reset Password</p>
            </div>
            <div className='h-fit w-fit m-4'>
                <input
                    className='border-2 focus:border-black focus:outline  w-55 h-8'
                    type="text" 
                    placeholder='Username' 
                    name="email" 
                    id="email" 
                    required
                />
            </div>
            <div className='h-fit w-fit  mb-4'>
                <input
                    className='border-2 focus:border-black focus:outline   w-55 h-8'
                    type="email" 
                    placeholder='Email' 
                    name="email" 
                    id="email" 
                    required
                />
            </div>
            <div className='h-fit w-fit  mb-8 '>
                <div className='h-fit w-fit '>
                    <input
                        className='border-2 focus:border-black focus:outline   w-55 h-8'
                        type="password" 
                        placeholder='new password' 
                        name="password" 
                        id="password"
                         
                        required
                    />
                    
                </div>
                
            </div>
        

            <div className='h-fit w-fit m-2'>
                <div className='h-fit w-fit border-3'>
                    <button className='w-55 h-8 font-semibold hover:bg-black hover:text-white hover:cursor-pointer'>Reset</button>
                </div>
                
            </div>
        </div>
    </div>
  )
}

export default ResetPassword
