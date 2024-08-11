import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import App from './App';
import Reviews from './Reviews';
import Profile from './Profile';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route path="/home" element={<App />} />
      <Route path="/reviews" element={<Reviews />} />
      <Route path="/profile" element={<Profile />} />
    </Routes>
  );
};

export default AppRoutes;
