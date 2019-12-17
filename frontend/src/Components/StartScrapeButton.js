import React from 'react';

function StartScrapeButton() {
  // TODO actually call python api to start the scraping
  function goToScrapeStatus() {
    window.location.assign("/scrapeStatus")
  }

  return <button className='Scrape-Button' onClick={goToScrapeStatus} data-testid='startScrape'>
           Initiate COPA Scrape
         </button>
}

export default StartScrapeButton;