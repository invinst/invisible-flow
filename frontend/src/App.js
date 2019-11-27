import React from 'react';
import './App.css';
import MainPage from './Components/MainPage';
import Footer from './Components/Footer';

function App() {
    // TODO actually call python api to start the scraping
    // for now anonymous function will do until python api is ready
    const startScrape = () => {};
      return (
        <div className="App">
          <MainPage startScrape={startScrape}/>
          <Footer />
        </div>
      );
}

export default App;
