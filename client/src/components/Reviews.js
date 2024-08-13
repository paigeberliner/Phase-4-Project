import React, { useEffect, useState } from 'react';
import NavBar from "./NavBar";

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
    <div>
      <NavBar />
      <h1>Reviews</h1>
      <form>
      </form>
      <ul>
        {reviews.map((review, index) => (
          <li key={index}>
            <strong>{review.user}:</strong> {review.review}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Reviews;
