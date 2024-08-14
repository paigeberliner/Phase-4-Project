import React, { createContext, useState, useContext } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [userFirstName, setUserFirstName] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (firstName) => {
    setUserFirstName(firstName);
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setUserFirstName('');
    setIsLoggedIn(false);
  };

  return (
    <AuthContext.Provider value={{ userFirstName, isLoggedIn, handleLogin, handleLogout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
