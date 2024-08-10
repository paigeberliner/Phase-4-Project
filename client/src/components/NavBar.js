import React from 'react';
import './NavBar.css'; // Import your CSS file

const NavBar = () => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
      <div className="right-items">
        <a href="/login" className="menu-item">Login</a>
      </div>
    </div>
  );
};

export default NavBar;