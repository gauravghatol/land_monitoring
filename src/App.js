import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Map from './components/Map';
import './App.css';

function App() {
  const [landUses, setLandUses] = useState([]);

  useEffect(() => {
    axios.get('/api/land_use')
      .then(response => {
        setLandUses(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the land use data!', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Land Monitoring Application</h1>
      </header>
      <Map landUses={landUses} />
    </div>
  );
}

export default App;
