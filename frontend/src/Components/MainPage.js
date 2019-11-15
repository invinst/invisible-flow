import React from 'react';
import StartScrapeButton from './StartScrapeButton'


function MainPage({startScrape}){
  return(
    <div className="MainPage">
        <StartScrapeButton startScrape={startScrape} />
    </div>
  );
}

export default MainPage;