import React from 'react';
import '../index.css'; 

const NavBar = () => {
  return (
    <div className="nav-bar">
      <div className="left-items">
        <a href="/home" className="menu-item">Home</a>
        <a href="/classhistory" className="menu-item">Class History</a>
        <a href="/profile" className="menu-item">Profile</a>
      </div>
    </div>
  );
};

export default NavBar;
