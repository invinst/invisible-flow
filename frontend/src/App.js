import React from 'react';
import './App.css';
import Header from './Components/Header';
import MainPage from './Components/MainPage';

function App() {
    // TODO actually call python api to start the scraping
    // for now anonymous function will do until python api is ready
    const startScrape = () => {};
      return (
        <div className="App">
          <Header />
          <MainPage startScrape={startScrape}/>
        </div>
      );
}

export default App;
