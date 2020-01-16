import React from 'react';
import { useHistory } from 'react-router-dom';

function StartScrapeButton(props) {
  let history = useHistory();

  async function goToScrapeStatus() {
    await props.toggleLoading();
    const request = new XMLHttpRequest();
    request.open('GET', '/copa_scrape', false);
    request.send();
    if (request.status === 200) {
      props.toggleLoading();
      //history.push('/scrapeStatus');
    }
  }

  return (
    <button className='Scrape-Button' onClick={goToScrapeStatus}>
      Initiate COPA Scrape
    </button>
  );
}

export default StartScrapeButton;
