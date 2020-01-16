import React from 'react';
import { useHistory } from 'react-router-dom';

function StartScrapeButton(props) {
  let history = useHistory();

  async function goToScrapeStatus() {
    await props.toggleLoading();
    const request = new XMLHttpRequest();
    request.open('GET', '/copa_scrape', false);
    request.send();

    await new Promise(r => setTimeout(r, 2000));

    if (request.status === 200) {
      props.toggleLoading();
      history.push('/scrapeStatus');
    } else if (request.status === 500) {
			props.toggleLoading();
    }
  }

  return (
    <button className='Scrape-Button' onClick={goToScrapeStatus}>
      Initiate scrape
    </button>
  );
}

export default StartScrapeButton;
