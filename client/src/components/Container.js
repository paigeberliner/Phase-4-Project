import React from 'react';
import './Container.css';

const Container = ({ id, studio_name, studio_location, class_name, class_duration, class_date, class_time, onDelete }) => {

  async function handleClick(e) {
    e.preventDefault();
    console.log('Class ID to delete:', id);

    try {
      const response = await fetch('/workoutclasses', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id }), // Send the class ID in the request body
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data.message); // Log the success message
        onDelete(id); // Call onDelete to remove the class from the list in the parent component
      } else {
        const errorData = await response.json();
        console.error('Error deleting class:', errorData.error);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  }

  return (
    <div className="classTile">
      <div className="classTile-row">
        <div className="classTile-cell"><strong>Studio Name:</strong> {studio_name}</div>
        <div className="classTile-cell"><strong>Class Name:</strong> {class_name}</div>
      </div>
      <div className="classTile-row">
        <div className="classTile-cell"><strong>Location:</strong> {studio_location}</div>
        <div className="classTile-cell"><strong>Duration:</strong> {class_duration} minutes</div>
      </div>
      <div className="classTile-row">
        <div className="classTile-cell"><strong>Date:</strong> {new Date(class_date).toLocaleDateString()}</div>
        <div className="classTile-cell"><strong>Time:</strong> {new Date(class_time).toLocaleTimeString()}</div>
      </div>
      <button onClick={handleClick}>Delete</button>
    </div>
  );
};

export default Container;
