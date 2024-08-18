import React, { useState } from 'react';
import NavBar from './NavBar';
import LoginForm from './LoginForm';

const Profile = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [userFirstName, setUserFirstName] = useState('');
  const [userLastName, setUserLastName] = useState(''); // Added state for last name
  const [userEmail, setUserEmail] = useState(''); // Added state for email
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
          setUserLastName(user.last_name); // Fixed function call
          setUserEmail(user.email); // Fixed function call
          setMessage('');
          setIsLoggedIn(true);
        } else {
          setUserFirstName('');
          setUserLastName(''); // Ensure last name is reset
          setUserEmail(''); // Ensure email is reset
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
    setUserLastName(''); // Reset last name on logout
    setUserEmail(''); // Reset email on logout
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
              <li><strong>First Name:</strong> {userFirstName}</li>
              <li><strong>Last Name:</strong> {userLastName}</li>
              <li><strong>Email:</strong> {userEmail}</li> {/* Display email */}
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
