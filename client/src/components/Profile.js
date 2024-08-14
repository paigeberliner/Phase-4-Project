import React, { useState, useEffect } from 'react';
import NavBar from './NavBar';
import LoginForm from './LoginForm';

const Profile = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [userFirstName, setUserFirstName] = useState('');
  const [message, setMessage] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Handle login click to show/hide login form
  const handleLoginClick = () => {
    setShowLogin(!showLogin);
  };

  // Handle user login
  const handleLogin = (email) => {
    fetch("http://127.0.0.1:5555/users")
      .then(response => response.json())
      .then(users => {
        const user = users.find(user => user.email === email);
        if (user) {
          setUserFirstName(user.first_name);
          setMessage('');
          setIsLoggedIn(true);
        } else {
          setUserFirstName('');
          setMessage('Not a user - sign up');
        }
        setShowLogin(false); // Hide the login form after checking
      })
      .catch(error => {
        console.error("Error:", error);
        setMessage('Error checking user - try again');
      });
  };

  // Handle user logout
  const handleLogout = () => {
    setUserFirstName('');
    setIsLoggedIn(false);
    setMessage('');
  };

  return (
    <div>
      <NavBar />
      <div className="profile-content">
        <h1>Profile</h1>
        {showLogin && <LoginForm onLogin={handleLogin} />}
        {!isLoggedIn && (
          <>
            <button onClick={handleLoginClick}>
              {showLogin ? 'Cancel' : 'Login'}
            </button>
            {message && <div className="message">{message}</div>}
          </>
        )}
        {isLoggedIn && (
          <>
            <ul>
              <li><strong>Name:</strong> {userFirstName}</li>
              {/* Add more user details as needed */}
            </ul>
            <button onClick={handleLogout}>Logout</button>
          </>
        )}
      </div>
    </div>
  );
};

export default Profile;
