import React, { useEffect, useState } from 'react'
import Navbar from './components/Navbar'
import { Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import Login from './components/Login'
import Signup from './components/Signup'
import BlogForm from './components/BlogForm'

const App = () => {
  // const [message, setMessage] = useState('message')

  // useEffect(() => {
  //   fetch('/blog/test')
  //     .then(res => res.json())
  //     .then(data => {
  //       console.log(data)
  //       setMessage(data.message)
  //     })
  //     .catch(err => console.error(err))

  // }, [])


  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/blogform' element={<BlogForm />} />
      </Routes>
    </>
  )
}

export default App
