import React, { useState, useEffect } from 'react';
import NavBar from './NavBar';
import { Form } from './Form';
import Container from './Container';
import LoginForm from './LoginForm';

function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [userFirstName, setUserFirstName] = useState('');
  const [message, setMessage] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [workoutClasses, setWorkoutClasses] = useState([]);

  // Function to fetch and update workout classes
  const updateWorkoutClasses = () => {
    fetch("/workoutclasses")
      .then((res) => res.json())
      .then((data) => setWorkoutClasses(data))
      .catch((error) => console.error("Error fetching workout classes:", error));
  };

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

  // Fetch workout classes on component mount
  useEffect(() => {
    updateWorkoutClasses();
  }, []);

  return (
    <>
      <NavBar 
        onLoginClick={handleLoginClick} 
        showLogin={showLogin} 
        userFirstName={userFirstName}
        message={message}
        isLoggedIn={isLoggedIn}
        onLogout={handleLogout}
      />
      {showLogin && <LoginForm onLogin={handleLogin} />}
      {userFirstName && !isLoggedIn && <div className="greeting">Hello, {userFirstName}!</div>}
      {message && <div className="message">{message}</div>}
      <Form updateWorkoutClasses={updateWorkoutClasses} />
      {workoutClasses.map(workoutClass => (
        <Container
          key={workoutClass.id}
          studio_name={workoutClass.studio_name}
          studio_location={workoutClass.studio_location}
          class_name={workoutClass.class_name}
          class_duration={workoutClass.class_duration}
          class_time={workoutClass.class_time}
        />
      ))}
    </>
  );
}

export default App;
