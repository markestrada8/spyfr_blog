import React, { Fragment } from 'react'
import { Link } from 'react-router-dom'
import { logout, useAuth } from '../auth'



const Navbar = () => {
  const [isLoggedIn] = useAuth()


  const loggedInDisplay = () => {
    return (
      <>
        <li className="nav-item">
          <Link to='/' className="nav-link active">Home</Link>
        </li>
        <li className="nav-item">
          <Link to='/blogform' className="nav-link active">New Entry</Link>
        </li>
        <li className="nav-item">
          <Link to='/' className="nav-link active" onClick={logout}>Logout</Link>
        </li>
      </>
    )
  }


  const loggedOutDisplay = () => {
    return (
      <>
        <li className="nav-item">
          <Link to='/' className="nav-link active">Home</Link>
        </li>
        <li className="nav-item">
          <Link to='/login' className="nav-link active">Login</Link>
        </li>
        <li className="nav-item">
          <Link to='/signup' className="nav-link active">Signup</Link>
        </li>
      </>
    )
  }


  return (
    <Fragment>
      <nav className="navbar navbar-expand-lg bg-body-tertiary navbar-dark bg-dark">
        <div className="container-fluid">
          <Link to='/' className="nav-link active">Palimpsest</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              {isLoggedIn ?
                loggedInDisplay()
                :
                loggedOutDisplay()
              }
            </ul>
          </div>
        </div>
      </nav>
    </Fragment>
  )
}

export default Navbar

