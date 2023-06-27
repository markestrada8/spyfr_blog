import React, { useEffect, useState } from 'react'
import Navbar from './components/Navbar'
import { Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import Login from './components/Login'
import Signup from './components/Signup'
import BlogForm from './components/BlogForm'

const App = () => {
  const [blogs, setBlogs] = useState([])

  const getBlogs = () => {
    fetch('/blog/blogs')
      .then(response => response.json())
      .then(result => {
        // console.log('Get posts response: ', result)
        setBlogs(result)
      })
  }

  useEffect(() => {
    getBlogs()
  }, [])


  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home getBlogs={getBlogs} blogs={blogs} setBlogs={setBlogs} />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/blogform' element={<BlogForm getBlogs={getBlogs} blogs={blogs} setBlogs={setBlogs} />} />
      </Routes>
    </>
  )
}

export default App
