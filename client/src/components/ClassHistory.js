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
          const classDate = new Date(review.workout_class_date);
          //const today = new Date();
          //today.setHours(0, 0, 0, 0); // Set today's date to midnight for accurate comparison

          // Check if the class date is not null and is in the past
          //if (review.workout_class_date && classDate < today) {
            // Format the date to YYYY-MM-DD
            const formattedDate = classDate.toISOString().split('T')[0];

            return (
              <li key={index} className="reviews-item">
                <strong>{review.user} posted a {review.workout_class} Class on {formattedDate}:</strong> {review.review}
              </li>
            );
          }
          //return null; // Do not render anything if the class date is null or in the future
        //}
      )}
      </ul>
    </div>
  );
};

export default ClassHistory;
