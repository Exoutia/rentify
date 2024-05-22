import './App.css'

import Login from './Login'
import { useState } from 'react'



function App() {

  const [token, setToken] = useState<string>(localStorage.getItem('token')|| '')
  return (
    <Login setToken={(token: string) => {
      setToken(token);
      localStorage.setItem('token', token);
    }} />
  )
}

export default App
