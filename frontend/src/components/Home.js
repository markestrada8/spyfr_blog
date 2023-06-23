import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

import '../styles/main.css'
import { useAuth } from '../auth'
import BlogItem from './BlogItem'

const Home = () => {
  const [blogs, setBlogs] = useState([])
  const [isLoggedIn] = useAuth()

  useEffect(() => {
    fetch('/blog/blogs')
      .then(response => response.json())
      .then(result => {
        // console.log(result)
        setBlogs(result)
      })

  }, [])


  const loggedInDisplay = () => {
    return (
      <>
        <h1>Blog Entries</h1>

      </>
    )
  }

  const loggedOutDisplay = () => {
    return (
      <>
        <h1 className='heading'>Welcome to Palimpsest</h1>
        <Link to='/signup' className='btn btn-primary btn-lg'>Get Started</Link>
        {blogs ? blogs.map(blog => (
          <BlogItem data={blog} />
        ))
          : null
        }
      </>
    )
  }


  return (
    <div className='home container'>
      {isLoggedIn ?
        loggedInDisplay()
        :
        loggedOutDisplay()

      }
    </div>
  )
}

export default Home