import React from 'react';
import StartScrapeButton from './StartScrapeButton'
import bgPic from '../images/AllTheDocs.jpeg'


function MainPage({startScrape}){
  return(
    <div className="MainPage">
        <img src={bgPic}  alt=''/>
        <StartScrapeButton startScrape={startScrape} />
    </div>
  );
}

export default MainPage;