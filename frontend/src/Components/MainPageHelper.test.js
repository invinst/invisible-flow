import {clearIntervalAndGoToStatusPage, pollForStatus, runCopaJob} from "./MainPageHelper";

function flushPromises() {
    // put here so we can flush the chain of promises in the component https://github.com/facebook/jest/issues/2157
    return new Promise(resolve => setImmediate(resolve))
}

describe('MainPageHelper', function () {
    it('should hit /start_copa_job when runCopaJob is called and periodically poll for copa job status after starting job', async () => {
        const randId = Math.floor(Math.random() * 100);
        jest.spyOn(global, 'setInterval').mockImplementation(() => {
        })
        jest.spyOn(global, "fetch")
            .mockImplementation(() => {
                return Promise.resolve({
                    json: () => Promise.resolve({job_id: randId})
                })
            });

        runCopaJob(jest.fn(), jest.fn());

        await flushPromises()
        expect(global.fetch).toHaveBeenCalledWith("/start_copa_job")
        expect(global.setInterval).toHaveBeenCalledWith(pollForStatus, 500, randId, expect.any(Function))
    });

    describe('pollForStatus', function () {
        it('should call oncomplete when job status is completed', async () => {
            const randId = Math.floor(Math.random() * 100)
            jest.spyOn(global, "fetch").mockImplementation(() =>
                Promise.resolve({json: () => Promise.resolve({status: 'COMPLETED'})})
            );

            const mockFn = jest.fn()
            pollForStatus(randId, mockFn)
            await flushPromises()

            expect(global.fetch).toHaveBeenCalledWith("/job_status/" + randId)
            expect(mockFn).toHaveBeenCalled()
        });

        it('should not call oncomplete when job status is not completed', async () => {
            const randId = Math.floor(Math.random() * 100)
            jest.spyOn(global, "fetch").mockImplementation(() =>
                Promise.resolve({json: () => Promise.resolve({status: 'INCOMPLETE'})})
            );

            const mockFn = jest.fn()
            pollForStatus(randId, mockFn)
            await flushPromises()

            expect(global.fetch).toHaveBeenCalledWith("/job_status/" + randId)
            expect(mockFn).not.toHaveBeenCalled()
        });
    });

    describe('clearIntervalAndGoToStatusPage', function () {
        it('should  clear the interval with the given intervalId and go to the /scrapeStatus page', function () {
            const randId = Math.floor(Math.random() * 100)
            jest.spyOn(global, "clearInterval")

            const fakeHistoryObject = {
                push: jest.fn()
            };

            clearIntervalAndGoToStatusPage(randId, fakeHistoryObject)

            expect(global.clearInterval).toHaveBeenCalledWith(randId)
            expect(fakeHistoryObject.push).toHaveBeenCalledWith("/scrapeStatus")
        });
    });


});
