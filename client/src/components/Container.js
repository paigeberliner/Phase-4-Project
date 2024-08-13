import React from 'react';
import './Container.css'; // Ensure this file exists and is correctly styled

const Container = ({ id, studio_name, studio_location, class_name, class_duration, class_date, class_time, created_at }) => {
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
    </div>
  );
};

export default Container;
