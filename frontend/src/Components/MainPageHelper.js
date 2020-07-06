
export function pollForStatus(jobId, onCompleteCallback) {
    console.log('called')
    fetch(`/job_status/${jobId}`).then(res => res.json())
        .then(jobStatus => {
            if (jobStatus.status === "COMPLETED") {
                onCompleteCallback()
            }
        })
}
export function runCopaJob(setFinishedLoading, setMaybeIntervalId) {
    fetch('/start_copa_job').then(res => {
        return res.json()
    }).then(jsonResponse => {
        const jobID = jsonResponse.job_id;

        const intervalId = setInterval(pollForStatus, 500, jobID, () => setFinishedLoading(true));
        setMaybeIntervalId(intervalId)

    })
}

export function clearIntervalAndGoToStatusPage(intervalId, history) {
    clearInterval(intervalId)
    history.push("/scrapeStatus")
}
