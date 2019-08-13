# Use React Router

## Status

approved

## Context

The need here is to be able to change to a different view based on user interaction in app.
Example: User clicks Scrape COPA Data button, app page should change and display information 
about the scrape operation.

##Discussion

So why should we use Reach-Router over the React-Router or No Router?
Reach-Router:
    + Smaller than React-Router (less than 4k)
    + Always save to the session the forms created
    - New tech, developers have little/no experience

React-Router:
    = History blocking
    + Jeff and Jovanka have experience with this router
    *CHOSEN*

No Router:
    A reason to not do this is because we have at least 1 main view and 2 sub-views; stackoverflow says don't do this.

## Decision

Adding a router so that we can display multiple pages/paths to the user as needed.

## Consequences

Having multiple pages with differing needs, for example, inputting foia request data, 
or showing status of COPA scraping job