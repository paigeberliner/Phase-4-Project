import React, { useState, useEffect } from 'react';
import NavBar from './NavBar';
import { Form } from './Form';
import Container from './Container';

function App() {
  const [workoutClasses, setWorkoutClasses] = useState([]);

  // Function to fetch and update workout classes
  const updateWorkoutClasses = () => {
    fetch("/workoutclasses")
      .then((res) => res.json())
      .then((data) => setWorkoutClasses(data))
      .catch((error) => console.error("Error fetching workout classes:", error));
  };

  // Fetch workout classes on component mount
  useEffect(() => {
    updateWorkoutClasses();
  }, []);

  return (
    <>
      <NavBar />
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
