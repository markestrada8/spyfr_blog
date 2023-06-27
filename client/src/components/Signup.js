import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import Alert from 'react-bootstrap/Alert'

const Signup = () => {
  const { register, handleSubmit, reset, formState: { errors } } = useForm()
  const [show, setShow] = useState(false)
  const [serverResponse, setserverResponse] = useState('')

  const submitForm = (data) => {
    if (data.password !== data.confirmPassword) {
      alert('Passwords do not match')
    } else {

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }

      fetch('/auth/signup', requestOptions)
        .then(response => response.json())
        .then(result => {
          console.log(result)
          setserverResponse(result.message)
          setShow(true)
        })
        .catch(error => {
          console.log(error)
        })

      reset()
    }
  }


  return (
    <div className='container'>
      <div className='form'>
        {show ?
          <>
            <Alert variant={serverResponse.includes('success') ? 'success' : 'danger'} onClose={() => {
              setShow(false)
            }} dismissible>
              <p>
                {serverResponse}
              </p>
            </Alert>
            <h1>Sign Up</h1>
          </>
          :
          <h1>Sign Up</h1>
        }
        <form>
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control
              type='text'
              placeholder='Enter username'
              {...register('username', { required: true, maxLength: 100 })}
            />

            {errors.username && <p style={{ color: '#de5c5c' }}><small>Username is required</small></p>}
          </Form.Group>

          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control
              type='email'
              placeholder='Enter email'
              {...register('email', { required: true, maxLength: 100 })}
            />

            {errors.email && <p style={{ color: '#de5c5c' }}><small>Email is required</small></p>}
          </Form.Group>

          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='Enter password'
              {...register('password', { required: true, minLength: 8, maxLength: 500 })}
            />

            {errors.password && <p style={{ color: '#de5c5c' }}><small>Password must be at least 8 characters</small></p>}
          </Form.Group>

          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control
              type='password'
              placeholder='Confirm password'
              {...register('confirmPassword', { required: true, minLength: 8, maxLength: 500 })}
            />
            {/* {errors.confirmPassword && <p style={{ color: "#de5c5c" }}><small>Confirm password</small></p>} */}
            {errors.confirmPassword && <p style={{ color: '#de5c5c' }}><small>Password must be at least 8 characters</small></p>}
          </Form.Group>
          <br />

          <Form.Group>
            <Button as='sub' variant='primary' onClick={handleSubmit(submitForm)}>Signup</Button>
          </Form.Group>
          <Form.Group>
            <small>Already have an account? <Link to='/login'>Login</Link></small>
          </Form.Group>
        </form>
      </div>
    </div>
  )
}

export default Signup