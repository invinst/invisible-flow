import React from 'react';

function StartScrapeButton({startScrape}) {
  return (
    <button className='Scrape-Button' onClick={startScrape} data-testid='startScrape'>Initiate COPA Scrape</button>
  );
}

export default StartScrapeButton;