import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../auth'
import BlogItem from './BlogItem'
import { Modal } from 'react-bootstrap'
import BlogForm from './BlogForm'
import { authFetch } from '../auth'

import '../styles/main.css'



const Home = () => {
  const [blogs, setBlogs] = useState([])
  const [blogId, setBlogId] = useState('')
  const [displayModal, setDisplayModal] = useState(false)
  const [isLoggedIn] = useAuth()


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


  const closeModal = () => {
    setDisplayModal(false)
    getBlogs()
  }

  const showModal = (id) => {
    setDisplayModal(true)
    setBlogId(id)
  }

  const handleDelete = (id) => {

    const postURL = `/blog/blog/${id}`
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    }

    authFetch(postURL, requestOptions)
      .then(response => {
        return response.json()
      })
      .then(result => {
        // console.log('Blog delete submit result: ', result)
        getBlogs()
      })
      .catch((error) => {
        console.log('Blog delete error: ', error)
      })

  }

  const loggedInDisplay = () => {
    return (
      <>
        <Modal
          show={displayModal}
          size='lg'
          onHide={closeModal}
        >
          <Modal.Header closeButton>
            <Modal.Title>
              Update
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <BlogForm editMode={true} id={blogId} closeModal={closeModal} />
          </Modal.Body>
        </Modal>
        <h1>Blog Entries</h1>
        {blogs && blogs.map(blog => (
          <BlogItem data={blog} key={blog.id} handleUpdate={showModal} handleDelete={handleDelete} />
        ))
        }
      </>
    )
  }

  const loggedOutDisplay = () => {
    return (
      <>
        <h1 className='heading'>Welcome to Palimpsest</h1>
        <Link to='/signup' className='btn btn-primary btn-lg'>Get Started</Link>
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