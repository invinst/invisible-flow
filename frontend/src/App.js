import React from 'react';
import './App.css';
import StartScrapeButton from './Components/StartScrapeButton';

function App() {
  const startScrape = () => {

  }
  return (
    <div className="App">
        <StartScrapeButton startScrape={startScrape}/>
    </div>
  );
}

export default App;
