import React from 'react'
import { Link } from 'react-router'
import { useState } from 'react'

function Login() {
    const [loginForm,setLoginForm] = useState({email:"",password:""})
    // State to hold the API response
    const [apiResponse, setApiResponse] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) =>{
        const {name, value} = e.target

        
        setLoginForm((prev)=>({
            ...prev,
            [name]:value
        }));
    }

    const handleSubmit = async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        e.preventDefault();
        setLoading(true)
        setError(null)
        setApiResponse(null)
        console.log("handle submit!")
        try{
            const response = await fetch('http://localhost:8000/api/auth/login',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                },
                body: JSON.stringify({...loginForm,username:null})
            })

            if(!response.ok)
            {
                throw new Error(`Server error: ${response.status}`)
            }

            const data = await response.json();
            setApiResponse(data)
        } catch (err:any) {
            setError(err.message)
        } finally {
            setLoading(false)
        }
    }
  return (
    <div className='w-full min-h-screen  flex  items-center justify-center'>
        <div className='p-3 h-[90%] flex flex-col border-2 items-center justify-center'>
            <div className='h-fit w-fit m-2 '>
                <p className='font-bold text-2xl'>Login Form</p>
            </div>
            <div className='h-fit w-fit m-4'>
                <input
                    className='border-2 focus:border-black focus:outline  w-55 h-8'
                    type="email" 
                    placeholder='email' 
                    name="email" 
                    id="email" 
                    value={loginForm.email}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className='h-fit w-fit  mb-4'>
                <div>
                    <input    
                        className='border-2 focus:border-black focus:outline   w-55 h-8'
                        type="password" 
                        placeholder='Password' 
                        name="password" 
                        id="password" 
                        value={loginForm.password}
                        onChange={handleChange}
                        required
                    />
                </div>
                <Link to="/resetpassword" className='text-sm underline'>forgot password? </Link>
            </div>
        

            <div className='h-fit w-fit m-2'>
                <div className='h-fit w-fit border-3'>
                    <button 
                        className='w-55 h-8 font-semibold hover:bg-black hover:text-white hover:cursor-pointer' 
                        type='submit' 
                        disabled={loading}
                        onClick={handleSubmit}
                    >
                    {loading ? 'Logging in...' : 'Login'}
                    </button>
                </div>
                <Link to="/register" className='text-sm underline'>new Guy?</Link>    
            </div>

            {error && <div className='text-red-600'>Error: {error}</div>}

            {apiResponse && (
                <div className='bg-green-300 p-5 h-fit w-fit border-2'>
                    <h3>API Response:</h3>
                    <pre>{JSON.stringify(apiResponse,null,2)}</pre>
                </div>
            )}
        </div>
    </div>
  )
}

export default Login
