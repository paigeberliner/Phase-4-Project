import React from 'react';
import './NavBar.css'; 

const NavBar = ({ onLoginClick, showLogin, userFirstName, message, isLoggedIn, onLogout }) => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/reviews" className="menu-item">Reviews</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
      <div className="right-items">
        {isLoggedIn ? (
          <div className="logout-section">
            <button className="menu-item" onClick={onLogout}>
              Logout
            </button>
            {userFirstName && <div className="greeting">Hello, {userFirstName}!</div>}
          </div>
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
