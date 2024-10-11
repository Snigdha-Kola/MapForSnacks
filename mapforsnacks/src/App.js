import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainPage from './MainPage';
import MapPage from './MapPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} /> {/* MainPage on the root path */}
        <Route path="/map" element={<MapPage />} /> {/* Map page */}
      </Routes>
    </Router>
  );
}

export default App;
