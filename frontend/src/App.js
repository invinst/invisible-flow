import React from 'react';
import './App.css';


import StartScrapeButton from "./Components/StartScrapeButton";

function App() {
  function startScrape() {
    console.log('TODO make actual start scrape function to scrape copa records');
    // redirect to scrapeStatus route
    window.location='/scrapeStatus'
  }
  return (
    <div className="App">
      <h1>Invisible Flow</h1>
      <StartScrapeButton startScrape={startScrape} />
    </div>
  );
}

export default App;
