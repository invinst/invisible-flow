#!/bin/bash

psql -c "create user invisible_flow;"
psql -c "create database invisible_flow_testing with owner invisible_flow;"
psql invisible_flow_testing -c "CREATE EXTENSION postgis;"
psql invisible_flow_testing -U invisible_flow -c "CREATE TABLE data_area (
    id integer not null primary key,
    name character varying(100) not null,
    area_type character varying(30) not null,
    polygon public.geometry(MultiPolygon,4326),
    tags character varying(20)[] not null,
    median_income character varying(100),
    alderman character varying(255),
    commander_id integer,
    description character varying(255),
    police_hq_id integer,
    created_at timestamp with time zone not null,
    updated_at timestamp with time zone not null
);"
psql invisible_flow_testing -U invisible_flow -c "\copy data_area from cpdp_beats.sql;"