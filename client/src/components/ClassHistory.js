import React, { useEffect, useState } from 'react';
import NavBar from "./NavBar";
import '../index.css'; // Ensure this is imported correctly

const ClassHistory = () => {
  const [reviews, setReviews] = useState([]);

  // Function to fetch and update reviews
  const fetchReviews = () => {
    fetch("/reviews")
      .then((res) => res.json())
      .then((data) => setReviews(data))
      .catch((error) => console.error("Error fetching reviews:", error));
  };

  // Fetch reviews when the component mounts
  useEffect(() => {
    fetchReviews();
  }, []);

  return (
    <div className="reviews-container">
      <NavBar />
      <ul className="reviews-list">
        {reviews.map((review, index) => {
          // Check if review.workout_class_date is a valid date
          let formattedDate = '';
          try {
            const classDate = new Date(review.workout_class_date);
            if (!isNaN(classDate.getTime())) { // Check if the date is valid
              formattedDate = classDate.toISOString().split('T')[0];
            } else {
              formattedDate = 'Invalid date'; // Default message for invalid dates
            }
          } catch (error) {
            formattedDate = 'Error parsing date'; // Error handling message
          }

          return (
            <li key={index} className="reviews-item">
              <strong>{review.user} posted a {review.workout_class} Class:</strong> {review.review}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default ClassHistory;
