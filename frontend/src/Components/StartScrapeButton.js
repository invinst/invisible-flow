import React from 'react';
import { useHistory } from "react-router-dom";

function StartScrapeButton() {
  let history = useHistory();

  function goToScrapeStatus() {
    const request = new XMLHttpRequest();
    request.open("GET", "/copa_scrape", false);
    request.send();
    if (request.status === 200) {
        history.push('/scrapeStatus');
    }
  }

  return (
    <button className='Scrape-Button' onClick={goToScrapeStatus} data-testid='startScrape'>
      Initiate COPA Scrape
    </button>
  );
}

export default StartScrapeButton;