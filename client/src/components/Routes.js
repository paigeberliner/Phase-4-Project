import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import App from './App';
import ClassHistory from './ClassHistory';
import Profile from './Profile';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route path="/home" element={<App />} />
      <Route path="/classhistory" element={<ClassHistory />} />
      <Route path="/profile" element={<Profile />} />
    </Routes>
  );
};

export default AppRoutes;