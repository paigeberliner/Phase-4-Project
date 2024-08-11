import React, { useState } from 'react';
import './NavBar.css'; 

const NavBar = ({ onLoginClick, showLogin }) => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/reviews" className="menu-item">Reviews</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
      <div className="right-items">
        <button className="menu-item" onClick={onLoginClick}>
          {showLogin ? 'Cancel' : 'Login'}
        </button>
      </div>
    </div>
  );
};

export default NavBar;
