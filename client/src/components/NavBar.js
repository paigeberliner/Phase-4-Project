import React from 'react';
import '../index.css'; 

const NavBar = () => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/reviews" className="menu-item">Reviews</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
    </div>
  );
};

export default NavBar;
