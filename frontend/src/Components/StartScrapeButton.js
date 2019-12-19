import React from 'react';

function StartScrapeButton() {
  function goToScrapeStatus() {
    const request = new XMLHttpRequest();
    request.open("GET", "http://localhost:5000/copa_scrape", false);
    request.send();
    if (request.status === 200) {
      window.location.assign("/scrapeStatus");
    }
  }

  return (
    <button className='Scrape-Button' onClick={goToScrapeStatus} data-testid='startScrape'>
      Initiate COPA Scrape
    </button>
  );
}

export default StartScrapeButton;