# Use Google Cloud Services for storage

## Status

accepted

## Context

The need here is to be able to store data as it goes through the ETL process.
Client currently uses GCP to hold their database, so it's simpler to use the same tech stack.

## Decision

Add google cloud storage to Invisible Flow project for use as cloud storage provider.

## Consequences

- This enables us to programatically generate and save the transformed data in a specific 
format and organizational structure for ease of use and retrieval at a later time/date.
