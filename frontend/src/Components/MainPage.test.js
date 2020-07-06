import {act, render} from "@testing-library/react";
import React from "react";
import MainPage from "./MainPage";

jest.useFakeTimers()
jest.mock('react-router-dom', () => {
    return {useHistory: () => ''}
})

jest.mock('./MainPageHelper')

const mockedHelper = require('./MainPageHelper')

function flushPromises() {
    // put here so we can flush the chain of promises in the component https://github.com/facebook/jest/issues/2157
    return new Promise(resolve => setImmediate(resolve))
}

describe('MainPage', function () {
    let container = null;
    beforeEach(() => {
        jest.mock('./MainPageHelper',)

        // setup a DOM element as a render target
        container = document.createElement("div");
        container.id = "me-yo"
        document.body.appendChild(container);
    });

    afterEach(() => {
        container.remove();
        container = null;
    });

    describe('MainPage', function () {
        it('should show start scrape button', function () {
            const {container} = render(<MainPage/>);
            const button = container.querySelector("#start-scrape")

            expect(button).toBeTruthy()
        });

        it('should show loading screen when scrape button is clicked and hide button', async () => {
            // Use the asynchronous version of act to apply resolved promises
            await act(async () => {
                render(<MainPage/>, {container: container});
            });

            expect(container.querySelector("[data-testid=spinner]")).toBeFalsy();
            const button = document.querySelector("#start-scrape");

            act(() => {
                // fireEvent.click(getByText('Initiate'))
                button.dispatchEvent(new MouseEvent("click", {bubbles: true}));
            });

            expect(container.querySelector("[data-testid=spinner]")).toBeTruthy();
            expect(container.querySelector("#start-scrape")).toBeFalsy();

        })
    });

    describe('loading logic', () => {
        it('should start a copa job  when button is clicked', async () => {
            await act(async () => {
                render(<MainPage/>, {container: container});
            });

            const button = document.querySelector("#start-scrape");

            act(() => {
                button.dispatchEvent(new MouseEvent("click", {bubbles: true}));
            });

            expect(mockedHelper.runCopaJob).toHaveBeenCalled()
        });

        it('should go to status page when copa job finsihes', async () => {
            await act(async () => {
                render(<MainPage/>, {container: container});
            });

            const button = document.querySelector("#start-scrape");

            act(() => {
                button.dispatchEvent(new MouseEvent("click", {bubbles: true}));
            });

            expect(mockedHelper.runCopaJob).toHaveBeenCalled()
        });

    });
});


