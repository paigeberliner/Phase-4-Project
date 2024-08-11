import React, { useState, useEffect } from 'react';
import NavBar from './NavBar';
import Form from './Form';
import Container from './Container';
import LoginForm from './LoginForm'; // Import LoginForm component

function App() {
  const [workoutClasses, setWorkoutClasses] = useState([]);
  const [showLogin, setShowLogin] = useState(false); // State to manage login form visibility

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
    console.log("Login with email:", email);
    // Add logic for email validation and authentication
    setShowLogin(false); // Hide the login form after submission
  };

  return (
    <>
      <NavBar onLoginClick={handleLoginClick} showLogin={showLogin} />
      {showLogin && <LoginForm onLogin={handleLogin} />}
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
