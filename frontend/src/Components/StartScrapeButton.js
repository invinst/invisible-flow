import React from 'react';

function StartScrapeButton() {
  return (
    <button className='Scrape-Button' onClick={StartScrapeButton.startScrape} data-testid='startScrape'>Initiate COPA Scrape</button>
  );
}

// TODO actually call python api to start the scraping
function startScrape() {}

export default StartScrapeButton;