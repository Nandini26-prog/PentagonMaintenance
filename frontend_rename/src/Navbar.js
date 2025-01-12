import React from 'react';
import {Link, BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
  <span className="logo-machine">Machine</span>
  <span className="logo-buddy">Buddy</span>
</div>

      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/Login">Log In</Link></li>
        <li><Link to="/Register">Register</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;




