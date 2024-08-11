import React, { useState } from "react";
import './Form.css';

const Form = ({ onItemFormSubmit }) => {
  const [studioName, setStudioName] = useState("");
  const [studioLocation, setStudioLocation] = useState("");
  const [className, setClassName] = useState("");
  const [classDuration, setClassDuration] = useState("");
  const [classDate, setClassDate] = useState("");
  const [classTime, setClassTime] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    // Combine date and time into a single datetime string
    const combinedDateTime = classDate && classTime ? `${classDate}T${classTime}` : null;

    const newClass = {
      studio_name: studioName,
      studio_location: studioLocation,
      class_name: className,
      class_duration: classDuration,
      class_date: combinedDateTime, // Send combined datetime to backend
      class_time: combinedDateTime // Optionally include this if your backend needs it separately
    }

    onItemFormSubmit(newClass);
    console.log(newClass);
  };

  return (
    <div className="form-container">
      <h2>Workout Class Submission</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="studioName">Studio Name</label>
          <input
            id="studioName"
            type="text"
            value={studioName}
            onChange={(event) => setStudioName(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="studioLocation">Studio Location</label>
          <input
            id="studioLocation"
            type="text"
            value={studioLocation}
            onChange={(event) => setStudioLocation(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="className">Class Name</label>
          <input
            id="className"
            type="text"
            value={className}
            onChange={(event) => setClassName(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="classDuration">Class Duration (minutes)</label>
          <input
            id="classDuration"
            type="number"
            value={classDuration}
            onChange={(event) => setClassDuration(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="classDate">Class Date</label>
          <input
            id="classDate"
            type="date"
            value={classDate}
            onChange={(event) => setClassDate(event.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="classTime">Class Time</label>
          <input
            id="classTime"
            type="time"
            value={classTime}
            onChange={(event) => setClassTime(event.target.value)}
          />
        </div>
        <div className="form-group">
          <button className="button" type="submit">Submit Class</button>
        </div>
      </form>
    </div>
  );
};

export default Form;
