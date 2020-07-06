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


    return (<div>

        {isLoading ?
            <LoadingPage/> :
            <button id="start-scrape" onClick={handleClick}>Initiate scrape</button>}
    </div>)
}

export default MainPage;
