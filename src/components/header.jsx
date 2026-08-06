// components/header.jsx
import React from 'react';

const Header = () => {
  return (
    <header className="bg-white shadow-sm py-6 mb-4">
      <h1 className="text-4xl font-extrabold text-center text-gray-900">CodeGuru</h1>
      <p className="text-center text-gray-500 text-sm mt-2">
        AI-powered code reviewer and mentor
      </p>
    </header>
  );
};

export default Header;
