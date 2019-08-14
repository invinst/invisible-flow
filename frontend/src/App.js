import React from 'react';
import './App.css';


import StartScrapeButton from "./Components/StartScrapeButton";

function App() {
      return (
        <div className="App">
          <h1>Invisible Flow</h1>
          <StartScrapeButton startScrape={startScrape} />
        </div>
      );
}

export default App;
