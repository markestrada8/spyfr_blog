import React from 'react'
import { Card, Button } from 'react-bootstrap'

const BlogItem = ({ data, handleUpdate, handleDelete }) => {
  const { id, title, content } = data

  return (
    <Card className='blog'>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <p>{content}</p>
        <Button
          variant='primary'
          style={{ marginRight: '20px' }}
          onClick={() => handleUpdate(id)}
        >Update</Button>

        <Button
          variant='danger'
          onClick={() => handleDelete(id)}
        >Delete</Button>
      </Card.Body>
    </Card>
  )
}

export default BlogItem