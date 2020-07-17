import React, {useState} from 'react';
import {LoadingPage} from "../Features/LoadingPage";
import {useHistory} from 'react-router-dom';
import {clearIntervalAndGoToStatusPage, runCopaJob} from "./MainPageHelper";

export function MainPage() {
  const [isLoading, setLoading] = useState(false)

  const [isFinishedLoading, setFinishedLoading] = useState(false)
  const [maybeIntervalID, setMaybeIntervalId] = useState(null)

  const history = useHistory();

  if (isFinishedLoading && maybeIntervalID) {
    console.log('clearing interval id')
    clearIntervalAndGoToStatusPage(maybeIntervalID, history)
  }

  const handleClick = function () {
    setLoading(oldState => !oldState)
    runCopaJob(setFinishedLoading, setMaybeIntervalId);
  };


  return (
      <div className='MainPage'>
        <h1>COPA Scrape</h1>

        {isLoading ?
            <LoadingPage/> :
            <button id="start-scrape" className='Scrape-Button' onClick={handleClick}>Initiate scrape</button>}
      </div>
  )
}

/*
    intent
        - loading page should show loading screen, no matter how long it loads for
        - When copa job is complete, loading page will change to /scrapeStatus
* */

export default MainPage;
