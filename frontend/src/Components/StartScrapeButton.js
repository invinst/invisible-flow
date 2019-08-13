import React from 'react';

function StartScrapeButton({startScrape}) {
  return (
    <button onClick={startScrape} data-testid='startScrape'>Start COPA scrape</button>
  );
}

export default StartScrapeButton;