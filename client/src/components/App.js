import React, { useState, useEffect } from 'react';
import NavBar from './NavBar';
import Form from './Form';
import Container from './Container';
import LoginForm from './LoginForm';

function App() {
  const [workoutClasses, setWorkoutClasses] = useState([]);
  const [showLogin, setShowLogin] = useState(false);
  const [userFirstName, setUserFirstName] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch("http://localhost:5555/workoutclasses")
      .then(response => response.json())
      .then(data => setWorkoutClasses(data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  const onItemFormSubmit = (classObj) => {
    fetch("http://localhost:5555/workoutclasses", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(classObj),
    })
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
      })
      .then((data) => setWorkoutClasses([...workoutClasses, data]))
      .catch((error) => console.error("Error:", error));
  };

  const handleLoginClick = () => {
    setShowLogin(!showLogin);
  };

  const handleLogin = (email) => {
    fetch("http://127.0.0.1:5555/users")
      .then(response => response.json())
      .then(users => {
        const user = users.find(user => user.email === email);
        if (user) {
          setUserFirstName(user.first_name);
          setMessage('');
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

  return (
    <>
      <NavBar 
        onLoginClick={handleLoginClick} 
        showLogin={showLogin} 
        userFirstName={userFirstName}
        message={message}
      />
      {showLogin && <LoginForm onLogin={handleLogin} />}
      {userFirstName && <div className="greeting">Hello, {userFirstName}!</div>}
      {message && <div className="message">{message}</div>}
      <Form onItemFormSubmit={onItemFormSubmit} />
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
