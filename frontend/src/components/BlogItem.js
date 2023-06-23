import React from 'react'

const BlogItem = ({ data }) => {
  const { id, title, content } = data
  console.log(title)
  return (
    <div key={id}>
      <h2>{title}</h2>
      <p>{content}</p>
    </div>
  )
}

export default BlogItem