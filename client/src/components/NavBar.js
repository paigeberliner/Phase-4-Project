import React from 'react';
import './NavBar.css'; 

const NavBar = ({ onLoginClick, showLogin, userFirstName, message }) => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/reviews" className="menu-item">Reviews</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
      <div className="right-items">
        {userFirstName ? (
          <span className="menu-item">Hello, {userFirstName}</span>
        ) : (
          <button className="menu-item" onClick={onLoginClick}>
            {showLogin ? 'Cancel' : 'Login'}
          </button>
        )}
      </div>
      {message && <div className="message">{message}</div>}
    </div>
  );
};

export default NavBar;
