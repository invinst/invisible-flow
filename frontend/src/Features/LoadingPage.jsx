import React from "react";

export function LoadingPage() {


    return (<div className='MainPageLoading'>
        <h1>COPA Scrape</h1>
        <div className="spinner-box" data-testid="spinner">
            <div className="spinner"></div>
            <p>Scraping...</p>
        </div>
    </div>)
}

// intent
/*
    intent
        - loading page should show loading screen, no matter how long it loads for
            - loading page will initialize a request to do a copa job
            - loading page will periodically poll for the status of the copa job
            - When copa job is complete, loading page will change to /scrapeStatus
* */
