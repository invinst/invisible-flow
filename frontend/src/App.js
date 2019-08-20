import React from 'react';
import './App.css';


import StartScrapeButton from "./Components/StartScrapeButton";

function App() {
    // TODO actually call python api to start the scraping
    // for now anonymous function will do until python api is ready
    const startScrape = () => {};
      return (
        <div className="App">
          <h1>Invisible Flow</h1>
          <StartScrapeButton startScrape={startScrape} />
        </div>
      );
}

export default App;
