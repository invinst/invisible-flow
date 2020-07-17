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
