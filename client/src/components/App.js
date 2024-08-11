import React, { useState, useEffect } from "react";
import NavBar from "./NavBar";
import Form from "./Form";
import Container from "./Container";

function App() {
  const [workoutClasses, setWorkoutClasses] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/workoutclasses")
      .then(response => response.json())
      .then(data => {
        setWorkoutClasses(data);
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  }, []);

  function onItemFormSubmit(classObj) {
    fetch("http://localhost:5555/workoutclasses", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(classObj),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setWorkoutClasses([...workoutClasses, data]);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  return (
    <>
      <NavBar />
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
