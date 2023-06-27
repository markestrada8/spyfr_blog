import React from 'react'
import { Form, Button } from 'react-bootstrap'
import { Link, useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import { login } from '../auth'

const Login = () => {
  const { register, handleSubmit, formState: { errors } } = useForm()
  const navigate = useNavigate()

  const submitForm = (data) => {
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }

    fetch('/auth/login', requestOptions)
      .then((response) => response.json())
      .then(result => {
        // console.log(result)
        login(result.access_token)
      })
      .catch((error) => {
        console.log(error)
      })
    navigate('/')
  }

  return (
    <div className='container'>
      <div className='form'>
        <h1>Login</h1>
        <form>
          <br />
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control
              type='email'
              placeholder='Enter email'
              {...register('email', { required: true, maxLength: 100 })}
            />

            {errors.email && <p style={{ color: '#de5c5c' }}><small>Email is required</small></p>}
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='Enter password'
              {...register('password', { required: true, minLength: 8, maxLength: 500 })}
            />

            {errors.password && <p style={{ color: '#de5c5c' }}><small>Password must be at least 8 characters</small></p>}
          </Form.Group>
          <br />
          <Form.Group>
            <Button as='sub' variant='primary' onClick={handleSubmit(submitForm)}>Login</Button>
          </Form.Group>
          <Form.Group>
            <small>Don't have an account? <Link to='/signup'>Sign up</Link></small>
          </Form.Group>

        </form>
      </div>
    </div>
  )
}

export default Login
