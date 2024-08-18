import React, { useEffect, useState } from 'react';
import NavBar from "./NavBar";
import '../index.css'; // Ensure this is imported correctly

const Reviews = () => {
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
      <h1 className="reviews-heading">Reviews</h1>
      <ul className="reviews-list">
        {reviews.map((review, index) => (
          <li key={index} className="reviews-item">
            <strong>{review.user}'s review for {review.workout_class}:</strong> {review.review}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Reviews;