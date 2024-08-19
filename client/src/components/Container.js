import React, { useState, useEffect } from 'react';
import '../index.css';

const Container = ({ id, studio_name, studio_location, class_name, class_duration, class_date, class_time, user_claimed, onDelete }) => {
  const [email, setEmail] = useState('');
  const [isClaimed, setIsClaimed] = useState(false);

  const formattedDate = new Date(class_date).toISOString().split('T')[0];

  useEffect(() => {
    setIsClaimed(Number.isInteger(user_claimed));
  }, [user_claimed]);

  async function handleDeleteClick(e) {
    e.preventDefault();
    const password = prompt("Enter password to delete:");

    if (password === '123') {
      console.log('Class ID to delete:', id);

      try {
        const response = await fetch(`/workoutclasses/${id}`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
          },
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
    } else {
      alert('Incorrect password. Class not deleted.');
    }
  }

  async function handleClaimClick(e) {
    e.preventDefault();
    console.log('Class ID to claim:', id, 'Email:', email);

    try {
      const response = await fetch(`/workoutclasses/${id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id, email }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data.message);
        setIsClaimed(true); // Update the UI to reflect that the class has been claimed
        setEmail(''); // Clear the email input field
      } else {
        const errorData = await response.json();
        console.error('Error claiming class:', errorData.error);
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
        <div className="classTile-cell"><strong>Date:</strong> {formattedDate}</div>
        <div className="classTile-cell"><strong>Time:</strong> {class_time}</div>
      </div>
      {isClaimed ? (
        <div className="claimedMessage">This class has been claimed!</div>
      ) : (
        <>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email to claim"
          />
          <button onClick={handleClaimClick}>Claim Class</button>
          <button onClick={handleDeleteClick}>Delete</button>
        </>
      )}
    </div>
  );
};

export default Container;
