import React from 'react';
import './Class.css';

function Class({ studio_name, class_name, studio_location, class_time, class_duration }) {
  return (
    <div className="classTile">
      <h2>{studio_name}</h2>
      <p><strong>Class:</strong> {class_name}</p>
      <p><strong>Location:</strong> {studio_location}</p>
      <p><strong>Time:</strong> {class_time}</p>
      <p><strong>Duration:</strong> {class_duration} minutes</p>
    </div>
  );
}

export default Class;
