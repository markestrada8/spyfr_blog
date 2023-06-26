import React, { useEffect } from 'react'
import { Form, Button } from 'react-bootstrap'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import { authFetch } from '../auth'

const BlogForm = ({ editMode, id, closeModal }) => {
  // const [blogToEdit, setBlogToEdit] = useState({})
  // const [titleToUpdate, setTitleToUpdate] = useState('')
  // const [contentToUpdate, setContentToUpdate] = useState('')

  const { register, handleSubmit, reset, setValue, formState: { errors } } = useForm()
  const navigate = useNavigate()

  const submitForm = (data) => {
    // TOKEN IS BEING STORED AS A STRING WITH QUOTES ADDED IN
    // const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY').slice(1, -1)

    const postURL = editMode ? `/blog/blog/${id}` : '/blog/blogs'
    const requestOptions = {
      method: editMode ? 'PUT' : 'POST',
      headers: {
        'Content-Type': 'application/json',
        // 'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data),
    }

    authFetch(postURL, requestOptions)
      .then(response => {
        return response.json()
      })
      .then(result => {
        // console.log('Blog form submit result: ', result)
        reset()
      })
      .catch((error) => {
        console.log('Blog post error: ', error)
      })
    if (editMode) {
      closeModal()
    }
    navigate('/')
  }

  useEffect(() => {
    if (id) {
      // GET SINGLE BLOG
      const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY').slice(1, -1)
      const requestOptions = {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
      }

      fetch(`/blog/blog/${id}`, requestOptions)
        .then(response => response.json())
        .then(result => {
          // setBlogToEdit(result)
          setValue('title', result.title)
          setValue('content', result.content)
        })
        .catch(error => console.log('Get blog error: ', error))
    }
  }, [id, setValue])


  return (
    <div className='container'>
      {editMode ? <h1>Update Blog</h1> : <h1>Create New Blog</h1>}
      <Form>
        <Form.Group>
          <Form.Label>Title</Form.Label>
          <Form.Control type='text'
            {...register('title', { required: true, maxLength: 100 })}
          />
          {errors.title && <p style={{ color: '#de5c5c' }}><small>Title is required</small></p>}
        </Form.Group>
        <br />
        <Form.Group >
          <Form.Label>Content</Form.Label>
          <Form.Control as='textarea' rows={5}
            {...register('content', { required: true })}
          />
        </Form.Group>
        {errors.content && <p style={{ color: '#de5c5c' }}><small>Content is required</small></p>}
        <br />
        <Form.Group>
          <Button variant='primary' onClick={handleSubmit(submitForm)}>Submit</Button>
        </Form.Group>
      </Form>
    </div>
  )
}

export default BlogForm