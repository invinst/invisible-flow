--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: data_allegation; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_allegation (
    crid character varying(30) NOT NULL,
    summary text NOT NULL,
    add2 character varying(255) NOT NULL,
    city character varying(255) NOT NULL,
    incident_date timestamp with time zone,
    point public.geometry(Point,4326),
    source character varying(20) NOT NULL,
    beat_id integer,
    is_officer_complaint boolean NOT NULL,
    add1 character varying(16) NOT NULL,
    location character varying(64) NOT NULL,
    old_complaint_address character varying(255),
    first_end_date date,
    first_start_date date,
    most_common_category_id integer,
    coaccused_count integer,
    subjects character varying(255)[] NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_allegation OWNER TO cpdb;

--
-- Name: data_allegation_areas; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_allegation_areas (
    id integer NOT NULL,
    allegation_id character varying(30) NOT NULL,
    area_id integer NOT NULL
);


ALTER TABLE public.data_allegation_areas OWNER TO cpdb;

--
-- Name: data_allegation_areas_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_allegation_areas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_allegation_areas_id_seq OWNER TO cpdb;

--
-- Name: data_allegation_areas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_allegation_areas_id_seq OWNED BY public.data_allegation_areas.id;


--
-- Name: data_allegation_line_areas; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_allegation_line_areas (
    id integer NOT NULL,
    allegation_id character varying(30) NOT NULL,
    linearea_id integer NOT NULL
);


ALTER TABLE public.data_allegation_line_areas OWNER TO cpdb;

--
-- Name: data_allegation_line_areas_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_allegation_line_areas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_allegation_line_areas_id_seq OWNER TO cpdb;

--
-- Name: data_allegation_line_areas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_allegation_line_areas_id_seq OWNED BY public.data_allegation_line_areas.id;


--
-- Name: data_allegationcategory; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_allegationcategory (
    id integer NOT NULL,
    category_code character varying(255) NOT NULL,
    category character varying(255) NOT NULL,
    allegation_name character varying(255) NOT NULL,
    on_duty boolean NOT NULL,
    citizen_dept character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_allegationcategory OWNER TO cpdb;

--
-- Name: data_allegationcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_allegationcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_allegationcategory_id_seq OWNER TO cpdb;

--
-- Name: data_allegationcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_allegationcategory_id_seq OWNED BY public.data_allegationcategory.id;


--
-- Name: data_area; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_area (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    area_type character varying(30) NOT NULL,
    polygon public.geometry(MultiPolygon,4326),
    tags character varying(20)[] NOT NULL,
    median_income character varying(100),
    alderman character varying(255),
    commander_id integer,
    description character varying(255),
    police_hq_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_area OWNER TO cpdb;

--
-- Name: data_area_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_area_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_area_id_seq OWNER TO cpdb;

--
-- Name: data_area_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_area_id_seq OWNED BY public.data_area.id;


--
-- Name: data_attachmentfile; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_attachmentfile (
    id integer NOT NULL,
    file_type character varying(10) NOT NULL,
    title character varying(255),
    url character varying(255) NOT NULL,
    additional_info jsonb,
    tag character varying(50) NOT NULL,
    original_url character varying(255) NOT NULL,
    external_created_at timestamp with time zone,
    external_last_updated timestamp with time zone,
    preview_image_url character varying(255),
    external_id character varying(255) NOT NULL,
    source_type character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    text_content text NOT NULL,
    allegation_id character varying(30) NOT NULL,
    downloads_count integer NOT NULL,
    views_count integer NOT NULL,
    show boolean NOT NULL,
    notifications_count integer NOT NULL,
    pages integer NOT NULL,
    manually_updated boolean NOT NULL,
    last_updated_by_id integer,
    pending_documentcloud_id character varying(255),
    upload_fail_attempts integer NOT NULL
);


ALTER TABLE public.data_attachmentfile OWNER TO cpdb;

--
-- Name: data_attachmentfile_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_attachmentfile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_attachmentfile_id_seq OWNER TO cpdb;

--
-- Name: data_attachmentfile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_attachmentfile_id_seq OWNED BY public.data_attachmentfile.id;


--
-- Name: data_award; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_award (
    id integer NOT NULL,
    award_type character varying(255) NOT NULL,
    start_date date,
    end_date date,
    current_status character varying(20) NOT NULL,
    request_date date NOT NULL,
    rank character varying(100) NOT NULL,
    last_promotion_date date,
    requester_full_name character varying(255),
    ceremony_date date,
    tracking_no character varying(255),
    officer_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_award OWNER TO cpdb;

--
-- Name: data_award_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_award_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_award_id_seq OWNER TO cpdb;

--
-- Name: data_award_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_award_id_seq OWNED BY public.data_award.id;


--
-- Name: data_complainant; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_complainant (
    id integer NOT NULL,
    gender character varying(1) NOT NULL,
    race character varying(50) NOT NULL,
    age integer,
    birth_year integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30)
);


ALTER TABLE public.data_complainant OWNER TO cpdb;

--
-- Name: data_complainant_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_complainant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_complainant_id_seq OWNER TO cpdb;

--
-- Name: data_complainant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_complainant_id_seq OWNED BY public.data_complainant.id;


--
-- Name: data_investigator; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_investigator (
    id integer NOT NULL,
    appointed_date date,
    first_name character varying(255),
    last_name character varying(255),
    middle_initial character varying(5),
    officer_id integer,
    suffix_name character varying(5),
    gender character varying(1) NOT NULL,
    race character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_investigator OWNER TO cpdb;

--
-- Name: data_investigator_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_investigator_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_investigator_id_seq OWNER TO cpdb;

--
-- Name: data_investigator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_investigator_id_seq OWNED BY public.data_investigator.id;


--
-- Name: data_investigatorallegation; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_investigatorallegation (
    id integer NOT NULL,
    current_star character varying(10),
    current_rank character varying(100),
    current_unit_id integer,
    investigator_id integer NOT NULL,
    investigator_type character varying(32),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30) NOT NULL
);


ALTER TABLE public.data_investigatorallegation OWNER TO cpdb;

--
-- Name: data_investigatorallegation_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_investigatorallegation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_investigatorallegation_id_seq OWNER TO cpdb;

--
-- Name: data_investigatorallegation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_investigatorallegation_id_seq OWNED BY public.data_investigatorallegation.id;


--
-- Name: data_involvement; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_involvement (
    id integer NOT NULL,
    full_name character varying(50) NOT NULL,
    involved_type character varying(25) NOT NULL,
    gender character varying(1),
    race character varying(50) NOT NULL,
    age integer,
    officer_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30) NOT NULL
);


ALTER TABLE public.data_involvement OWNER TO cpdb;

--
-- Name: data_involvement_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_involvement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_involvement_id_seq OWNER TO cpdb;

--
-- Name: data_involvement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_involvement_id_seq OWNED BY public.data_involvement.id;


--
-- Name: data_linearea; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_linearea (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    linearea_type character varying(30) NOT NULL,
    geom public.geometry(MultiLineString,4326) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_linearea OWNER TO cpdb;

--
-- Name: data_linearea_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_linearea_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_linearea_id_seq OWNER TO cpdb;

--
-- Name: data_linearea_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_linearea_id_seq OWNED BY public.data_linearea.id;


--
-- Name: data_officer; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officer (
    id integer NOT NULL,
    gender character varying(1) NOT NULL,
    race character varying(50) NOT NULL,
    appointed_date date,
    rank character varying(100) NOT NULL,
    active character varying(10) NOT NULL,
    birth_year integer,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    tags character varying(20)[] NOT NULL,
    middle_initial character varying(5),
    suffix_name character varying(5),
    resignation_date date,
    complaint_percentile numeric(6,4),
    middle_initial2 character varying(5),
    civilian_allegation_percentile numeric(6,4),
    honorable_mention_percentile numeric(6,4),
    internal_allegation_percentile numeric(6,4),
    trr_percentile numeric(6,4),
    allegation_count integer,
    sustained_count integer,
    civilian_compliment_count integer,
    current_badge character varying(10),
    current_salary integer,
    discipline_count integer,
    honorable_mention_count integer,
    last_unit_id integer,
    major_award_count integer,
    trr_count integer,
    unsustained_count integer,
    has_unique_name boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT data_officer_current_salary_check CHECK ((current_salary >= 0))
);


ALTER TABLE public.data_officer OWNER TO cpdb;

--
-- Name: data_officer_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officer_id_seq OWNER TO cpdb;

--
-- Name: data_officer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officer_id_seq OWNED BY public.data_officer.id;


--
-- Name: data_officeralias; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officeralias (
    id integer NOT NULL,
    old_officer_id integer NOT NULL,
    new_officer_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_officeralias OWNER TO cpdb;

--
-- Name: data_officeralias_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officeralias_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officeralias_id_seq OWNER TO cpdb;

--
-- Name: data_officeralias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officeralias_id_seq OWNED BY public.data_officeralias.id;


--
-- Name: data_officerallegation; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officerallegation (
    id integer NOT NULL,
    start_date date,
    end_date date,
    officer_age integer,
    recc_finding character varying(2) NOT NULL,
    recc_outcome character varying(32) NOT NULL,
    final_finding character varying(2) NOT NULL,
    final_outcome character varying(32) NOT NULL,
    final_outcome_class character varying(20) NOT NULL,
    allegation_category_id integer,
    officer_id integer,
    disciplined boolean,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30)
);


ALTER TABLE public.data_officerallegation OWNER TO cpdb;

--
-- Name: data_officerallegation_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officerallegation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officerallegation_id_seq OWNER TO cpdb;

--
-- Name: data_officerallegation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officerallegation_id_seq OWNED BY public.data_officerallegation.id;


--
-- Name: data_officerbadgenumber; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officerbadgenumber (
    id integer NOT NULL,
    star character varying(10) NOT NULL,
    current boolean NOT NULL,
    officer_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_officerbadgenumber OWNER TO cpdb;

--
-- Name: data_officerbadgenumber_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officerbadgenumber_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officerbadgenumber_id_seq OWNER TO cpdb;

--
-- Name: data_officerbadgenumber_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officerbadgenumber_id_seq OWNED BY public.data_officerbadgenumber.id;


--
-- Name: data_officerhistory; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officerhistory (
    id integer NOT NULL,
    effective_date date,
    end_date date,
    officer_id integer,
    unit_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_officerhistory OWNER TO cpdb;

--
-- Name: data_officerhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officerhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officerhistory_id_seq OWNER TO cpdb;

--
-- Name: data_officerhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officerhistory_id_seq OWNED BY public.data_officerhistory.id;


--
-- Name: data_officeryearlypercentile; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_officeryearlypercentile (
    id integer NOT NULL,
    year integer NOT NULL,
    percentile_trr numeric(6,4),
    percentile_allegation numeric(6,4),
    percentile_allegation_civilian numeric(6,4),
    percentile_allegation_internal numeric(6,4),
    officer_id integer NOT NULL
);


ALTER TABLE public.data_officeryearlypercentile OWNER TO cpdb;

--
-- Name: data_officeryearlypercentile_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_officeryearlypercentile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_officeryearlypercentile_id_seq OWNER TO cpdb;

--
-- Name: data_officeryearlypercentile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_officeryearlypercentile_id_seq OWNED BY public.data_officeryearlypercentile.id;


--
-- Name: data_pipeline_appliedfixture; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_pipeline_appliedfixture (
    id integer NOT NULL,
    file_name character varying(255) NOT NULL,
    created date NOT NULL
);


ALTER TABLE public.data_pipeline_appliedfixture OWNER TO cpdb;

--
-- Name: data_pipeline_appliedfixture_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_pipeline_appliedfixture_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_pipeline_appliedfixture_id_seq OWNER TO cpdb;

--
-- Name: data_pipeline_appliedfixture_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_pipeline_appliedfixture_id_seq OWNED BY public.data_pipeline_appliedfixture.id;


--
-- Name: data_policeunit; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_policeunit (
    id integer NOT NULL,
    unit_name character varying(5) NOT NULL,
    description character varying(255),
    tags character varying(20)[] NOT NULL,
    active boolean,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.data_policeunit OWNER TO cpdb;

--
-- Name: data_policeunit_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_policeunit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_policeunit_id_seq OWNER TO cpdb;

--
-- Name: data_policeunit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_policeunit_id_seq OWNED BY public.data_policeunit.id;


--
-- Name: data_policewitness; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_policewitness (
    id integer NOT NULL,
    officer_id integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30)
);


ALTER TABLE public.data_policewitness OWNER TO cpdb;

--
-- Name: data_policewitness_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_policewitness_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_policewitness_id_seq OWNER TO cpdb;

--
-- Name: data_policewitness_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_policewitness_id_seq OWNED BY public.data_policewitness.id;


--
-- Name: data_racepopulation; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_racepopulation (
    id integer NOT NULL,
    race character varying(255) NOT NULL,
    count integer NOT NULL,
    area_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT data_racepopulation_count_check CHECK ((count >= 0))
);


ALTER TABLE public.data_racepopulation OWNER TO cpdb;

--
-- Name: data_racepopulation_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_racepopulation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_racepopulation_id_seq OWNER TO cpdb;

--
-- Name: data_racepopulation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_racepopulation_id_seq OWNED BY public.data_racepopulation.id;


--
-- Name: data_salary; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_salary (
    id integer NOT NULL,
    pay_grade character varying(16) NOT NULL,
    rank character varying(64),
    salary integer NOT NULL,
    employee_status character varying(32) NOT NULL,
    org_hire_date date,
    spp_date date,
    start_date date,
    year smallint NOT NULL,
    age_at_hire smallint,
    officer_id integer NOT NULL,
    rank_changed boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT data_salary_age_at_hire_check CHECK ((age_at_hire >= 0)),
    CONSTRAINT data_salary_salary_check CHECK ((salary >= 0)),
    CONSTRAINT data_salary_year_check CHECK ((year >= 0))
);


ALTER TABLE public.data_salary OWNER TO cpdb;

--
-- Name: data_salary_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_salary_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_salary_id_seq OWNER TO cpdb;

--
-- Name: data_salary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_salary_id_seq OWNED BY public.data_salary.id;


--
-- Name: data_versioning_changelog; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_versioning_changelog (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    target_model character varying(255) NOT NULL,
    log_type integer NOT NULL,
    object_pk integer,
    content jsonb NOT NULL,
    source jsonb NOT NULL
);


ALTER TABLE public.data_versioning_changelog OWNER TO cpdb;

--
-- Name: data_versioning_changelog_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_versioning_changelog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_versioning_changelog_id_seq OWNER TO cpdb;

--
-- Name: data_versioning_changelog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_versioning_changelog_id_seq OWNED BY public.data_versioning_changelog.id;


--
-- Name: data_victim; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.data_victim (
    id integer NOT NULL,
    gender character varying(1) NOT NULL,
    race character varying(50) NOT NULL,
    age integer,
    birth_year integer,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    allegation_id character varying(30) NOT NULL
);


ALTER TABLE public.data_victim OWNER TO cpdb;

--
-- Name: data_victim_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.data_victim_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_victim_id_seq OWNER TO cpdb;

--
-- Name: data_victim_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.data_victim_id_seq OWNED BY public.data_victim.id;


--
-- Name: trr_actionresponse; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_actionresponse (
    id integer NOT NULL,
    person character varying(16),
    resistance_type character varying(32),
    action character varying(64),
    other_description character varying(64),
    member_action character varying(64),
    force_type character varying(64),
    action_sub_category character varying(3),
    action_category character varying(1),
    resistance_level character varying(16),
    trr_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.trr_actionresponse OWNER TO cpdb;

--
-- Name: trr_actionresponse_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_actionresponse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_actionresponse_id_seq OWNER TO cpdb;

--
-- Name: trr_actionresponse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_actionresponse_id_seq OWNED BY public.trr_actionresponse.id;


--
-- Name: trr_charge; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_charge (
    id integer NOT NULL,
    sr_no integer,
    statute character varying(64),
    description character varying(64),
    subject_no integer,
    trr_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT trr_charge_sr_no_check CHECK ((sr_no >= 0)),
    CONSTRAINT trr_charge_subject_no_check CHECK ((subject_no >= 0))
);


ALTER TABLE public.trr_charge OWNER TO cpdb;

--
-- Name: trr_charge_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_charge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_charge_id_seq OWNER TO cpdb;

--
-- Name: trr_charge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_charge_id_seq OWNED BY public.trr_charge.id;


--
-- Name: trr_subjectweapon; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_subjectweapon (
    id integer NOT NULL,
    weapon_type character varying(64),
    firearm_caliber character varying(16),
    weapon_description character varying(64),
    trr_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.trr_subjectweapon OWNER TO cpdb;

--
-- Name: trr_subjectweapon_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_subjectweapon_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_subjectweapon_id_seq OWNER TO cpdb;

--
-- Name: trr_subjectweapon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_subjectweapon_id_seq OWNED BY public.trr_subjectweapon.id;


--
-- Name: trr_trr; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_trr (
    id integer NOT NULL,
    beat smallint,
    block character varying(8),
    direction character varying(8),
    street character varying(64),
    location character varying(64),
    trr_datetime timestamp with time zone,
    indoor_or_outdoor character varying(8),
    lighting_condition character varying(32),
    weather_condition character varying(32),
    "notify_OEMC" boolean,
    notify_district_sergeant boolean,
    "notify_OP_command" boolean,
    "notify_DET_division" boolean,
    number_of_weapons_discharged smallint,
    party_fired_first character varying(16),
    location_recode character varying(64),
    taser boolean,
    total_number_of_shots smallint,
    firearm_used boolean,
    number_of_officers_using_firearm smallint,
    officer_assigned_beat character varying(16),
    officer_on_duty boolean,
    officer_in_uniform boolean,
    officer_injured boolean,
    officer_rank character varying(32),
    subject_id integer,
    subject_armed boolean,
    subject_injured boolean,
    subject_alleged_injury boolean,
    subject_age smallint,
    subject_birth_year smallint,
    subject_gender character varying(1),
    subject_race character varying(32),
    officer_id integer,
    officer_unit_id integer,
    officer_unit_detail_id integer,
    point public.geometry(Point,4326),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT trr_trr_beat_check CHECK ((beat >= 0)),
    CONSTRAINT trr_trr_number_of_officers_using_firearm_check CHECK ((number_of_officers_using_firearm >= 0)),
    CONSTRAINT trr_trr_number_of_weapons_discharged_check CHECK ((number_of_weapons_discharged >= 0)),
    CONSTRAINT trr_trr_subject_age_check CHECK ((subject_age >= 0)),
    CONSTRAINT trr_trr_subject_birth_year_check CHECK ((subject_birth_year >= 0)),
    CONSTRAINT trr_trr_subject_id_check CHECK ((subject_id >= 0)),
    CONSTRAINT trr_trr_total_number_of_shots_check CHECK ((total_number_of_shots >= 0))
);


ALTER TABLE public.trr_trr OWNER TO cpdb;

--
-- Name: trr_trr_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_trr_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_trr_id_seq OWNER TO cpdb;

--
-- Name: trr_trr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_trr_id_seq OWNED BY public.trr_trr.id;


--
-- Name: trr_trrstatus; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_trrstatus (
    id integer NOT NULL,
    rank character varying(16),
    star character varying(10),
    status character varying(16),
    status_datetime timestamp with time zone,
    age smallint,
    officer_id integer,
    trr_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.trr_trrstatus OWNER TO cpdb;

--
-- Name: trr_trrstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_trrstatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_trrstatus_id_seq OWNER TO cpdb;

--
-- Name: trr_trrstatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_trrstatus_id_seq OWNED BY public.trr_trrstatus.id;


--
-- Name: trr_weapondischarge; Type: TABLE; Schema: public; Owner: cpdb
--

CREATE TABLE public.trr_weapondischarge (
    id integer NOT NULL,
    weapon_type character varying(32),
    weapon_type_description character varying(32),
    firearm_make character varying(64),
    firearm_model character varying(32),
    firearm_barrel_length character varying(16),
    firearm_caliber character varying(16),
    total_number_of_shots smallint,
    firearm_reloaded boolean,
    number_of_catdridge_reloaded smallint,
    handgun_worn_type character varying(32),
    handgun_drawn_type character varying(32),
    method_used_to_reload character varying(64),
    sight_used boolean,
    protective_cover_used character varying(32),
    discharge_distance character varying(16),
    object_struck_of_discharge character varying(32),
    discharge_position character varying(32),
    trr_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.trr_weapondischarge OWNER TO cpdb;

--
-- Name: trr_weapondischarge_id_seq; Type: SEQUENCE; Schema: public; Owner: cpdb
--

CREATE SEQUENCE public.trr_weapondischarge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trr_weapondischarge_id_seq OWNER TO cpdb;

--
-- Name: trr_weapondischarge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cpdb
--

ALTER SEQUENCE public.trr_weapondischarge_id_seq OWNED BY public.trr_weapondischarge.id;


--
-- Name: data_allegation_areas id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_areas ALTER COLUMN id SET DEFAULT nextval('public.data_allegation_areas_id_seq'::regclass);


--
-- Name: data_allegation_line_areas id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_line_areas ALTER COLUMN id SET DEFAULT nextval('public.data_allegation_line_areas_id_seq'::regclass);


--
-- Name: data_allegationcategory id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegationcategory ALTER COLUMN id SET DEFAULT nextval('public.data_allegationcategory_id_seq'::regclass);


--
-- Name: data_area id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_area ALTER COLUMN id SET DEFAULT nextval('public.data_area_id_seq'::regclass);


--
-- Name: data_attachmentfile id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_attachmentfile ALTER COLUMN id SET DEFAULT nextval('public.data_attachmentfile_id_seq'::regclass);


--
-- Name: data_award id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_award ALTER COLUMN id SET DEFAULT nextval('public.data_award_id_seq'::regclass);


--
-- Name: data_complainant id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_complainant ALTER COLUMN id SET DEFAULT nextval('public.data_complainant_id_seq'::regclass);


--
-- Name: data_investigator id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigator ALTER COLUMN id SET DEFAULT nextval('public.data_investigator_id_seq'::regclass);


--
-- Name: data_investigatorallegation id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigatorallegation ALTER COLUMN id SET DEFAULT nextval('public.data_investigatorallegation_id_seq'::regclass);


--
-- Name: data_involvement id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_involvement ALTER COLUMN id SET DEFAULT nextval('public.data_involvement_id_seq'::regclass);


--
-- Name: data_linearea id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_linearea ALTER COLUMN id SET DEFAULT nextval('public.data_linearea_id_seq'::regclass);


--
-- Name: data_officer id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officer ALTER COLUMN id SET DEFAULT nextval('public.data_officer_id_seq'::regclass);


--
-- Name: data_officeralias id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeralias ALTER COLUMN id SET DEFAULT nextval('public.data_officeralias_id_seq'::regclass);


--
-- Name: data_officerallegation id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerallegation ALTER COLUMN id SET DEFAULT nextval('public.data_officerallegation_id_seq'::regclass);


--
-- Name: data_officerbadgenumber id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerbadgenumber ALTER COLUMN id SET DEFAULT nextval('public.data_officerbadgenumber_id_seq'::regclass);


--
-- Name: data_officerhistory id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerhistory ALTER COLUMN id SET DEFAULT nextval('public.data_officerhistory_id_seq'::regclass);


--
-- Name: data_officeryearlypercentile id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeryearlypercentile ALTER COLUMN id SET DEFAULT nextval('public.data_officeryearlypercentile_id_seq'::regclass);


--
-- Name: data_pipeline_appliedfixture id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_pipeline_appliedfixture ALTER COLUMN id SET DEFAULT nextval('public.data_pipeline_appliedfixture_id_seq'::regclass);


--
-- Name: data_policeunit id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policeunit ALTER COLUMN id SET DEFAULT nextval('public.data_policeunit_id_seq'::regclass);


--
-- Name: data_policewitness id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policewitness ALTER COLUMN id SET DEFAULT nextval('public.data_policewitness_id_seq'::regclass);


--
-- Name: data_racepopulation id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_racepopulation ALTER COLUMN id SET DEFAULT nextval('public.data_racepopulation_id_seq'::regclass);


--
-- Name: data_salary id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_salary ALTER COLUMN id SET DEFAULT nextval('public.data_salary_id_seq'::regclass);


--
-- Name: data_versioning_changelog id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_versioning_changelog ALTER COLUMN id SET DEFAULT nextval('public.data_versioning_changelog_id_seq'::regclass);


--
-- Name: data_victim id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_victim ALTER COLUMN id SET DEFAULT nextval('public.data_victim_id_seq'::regclass);


--
-- Name: trr_actionresponse id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_actionresponse ALTER COLUMN id SET DEFAULT nextval('public.trr_actionresponse_id_seq'::regclass);


--
-- Name: trr_charge id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_charge ALTER COLUMN id SET DEFAULT nextval('public.trr_charge_id_seq'::regclass);


--
-- Name: trr_subjectweapon id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_subjectweapon ALTER COLUMN id SET DEFAULT nextval('public.trr_subjectweapon_id_seq'::regclass);


--
-- Name: trr_trr id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trr ALTER COLUMN id SET DEFAULT nextval('public.trr_trr_id_seq'::regclass);


--
-- Name: trr_trrstatus id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trrstatus ALTER COLUMN id SET DEFAULT nextval('public.trr_trrstatus_id_seq'::regclass);


--
-- Name: trr_weapondischarge id; Type: DEFAULT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_weapondischarge ALTER COLUMN id SET DEFAULT nextval('public.trr_weapondischarge_id_seq'::regclass);


--
-- Name: data_allegation_areas data_allegation_areas_allegation_id_area_id_48b0b5a3_uniq; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_areas
    ADD CONSTRAINT data_allegation_areas_allegation_id_area_id_48b0b5a3_uniq UNIQUE (allegation_id, area_id);


--
-- Name: data_allegation_areas data_allegation_areas_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_areas
    ADD CONSTRAINT data_allegation_areas_pkey PRIMARY KEY (id);


--
-- Name: data_allegation data_allegation_crid_1770709b_pk; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation
    ADD CONSTRAINT data_allegation_crid_1770709b_pk PRIMARY KEY (crid);


--
-- Name: data_allegation data_allegation_crid_1770709b_uniq; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation
    ADD CONSTRAINT data_allegation_crid_1770709b_uniq UNIQUE (crid);


--
-- Name: data_allegation_line_areas data_allegation_line_are_allegation_id_linearea_i_ce5f75be_uniq; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_line_areas
    ADD CONSTRAINT data_allegation_line_are_allegation_id_linearea_i_ce5f75be_uniq UNIQUE (allegation_id, linearea_id);


--
-- Name: data_allegation_line_areas data_allegation_line_areas_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_line_areas
    ADD CONSTRAINT data_allegation_line_areas_pkey PRIMARY KEY (id);


--
-- Name: data_allegationcategory data_allegationcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegationcategory
    ADD CONSTRAINT data_allegationcategory_pkey PRIMARY KEY (id);


--
-- Name: data_area data_area_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_area
    ADD CONSTRAINT data_area_pkey PRIMARY KEY (id);


--
-- Name: data_attachmentfile data_attachmentfile_allegation_external_id_s_3059a89b_uniq; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_attachmentfile
    ADD CONSTRAINT data_attachmentfile_allegation_external_id_s_3059a89b_uniq UNIQUE (allegation_id, external_id, source_type);


--
-- Name: data_attachmentfile data_attachmentfile_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_attachmentfile
    ADD CONSTRAINT data_attachmentfile_pkey PRIMARY KEY (id);


--
-- Name: data_award data_award_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_award
    ADD CONSTRAINT data_award_pkey PRIMARY KEY (id);


--
-- Name: data_complainant data_complainant_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_complainant
    ADD CONSTRAINT data_complainant_pkey PRIMARY KEY (id);


--
-- Name: data_investigator data_investigator_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigator
    ADD CONSTRAINT data_investigator_pkey PRIMARY KEY (id);


--
-- Name: data_investigatorallegation data_investigatorallegation_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigatorallegation
    ADD CONSTRAINT data_investigatorallegation_pkey PRIMARY KEY (id);


--
-- Name: data_involvement data_involvement_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_involvement
    ADD CONSTRAINT data_involvement_pkey PRIMARY KEY (id);


--
-- Name: data_linearea data_linearea_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_linearea
    ADD CONSTRAINT data_linearea_pkey PRIMARY KEY (id);


--
-- Name: data_officer data_officer_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officer
    ADD CONSTRAINT data_officer_pkey PRIMARY KEY (id);


--
-- Name: data_officeralias data_officeralias_old_officer_id_ca37bbe0_uniq; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeralias
    ADD CONSTRAINT data_officeralias_old_officer_id_ca37bbe0_uniq UNIQUE (old_officer_id, new_officer_id);


--
-- Name: data_officeralias data_officeralias_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeralias
    ADD CONSTRAINT data_officeralias_pkey PRIMARY KEY (id);


--
-- Name: data_officerallegation data_officerallegation_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerallegation
    ADD CONSTRAINT data_officerallegation_pkey PRIMARY KEY (id);


--
-- Name: data_officerbadgenumber data_officerbadgenumber_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerbadgenumber
    ADD CONSTRAINT data_officerbadgenumber_pkey PRIMARY KEY (id);


--
-- Name: data_officerhistory data_officerhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerhistory
    ADD CONSTRAINT data_officerhistory_pkey PRIMARY KEY (id);


--
-- Name: data_officeryearlypercentile data_officeryearlypercentile_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeryearlypercentile
    ADD CONSTRAINT data_officeryearlypercentile_pkey PRIMARY KEY (id);


--
-- Name: data_pipeline_appliedfixture data_pipeline_appliedfixture_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_pipeline_appliedfixture
    ADD CONSTRAINT data_pipeline_appliedfixture_pkey PRIMARY KEY (id);


--
-- Name: data_policeunit data_policeunit_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policeunit
    ADD CONSTRAINT data_policeunit_pkey PRIMARY KEY (id);


--
-- Name: data_policewitness data_policewitness_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policewitness
    ADD CONSTRAINT data_policewitness_pkey PRIMARY KEY (id);


--
-- Name: data_racepopulation data_racepopulation_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_racepopulation
    ADD CONSTRAINT data_racepopulation_pkey PRIMARY KEY (id);


--
-- Name: data_salary data_salary_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_salary
    ADD CONSTRAINT data_salary_pkey PRIMARY KEY (id);


--
-- Name: data_versioning_changelog data_versioning_changelog_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_versioning_changelog
    ADD CONSTRAINT data_versioning_changelog_pkey PRIMARY KEY (id);


--
-- Name: data_victim data_victim_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_victim
    ADD CONSTRAINT data_victim_pkey PRIMARY KEY (id);


--
-- Name: trr_actionresponse trr_actionresponse_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_actionresponse
    ADD CONSTRAINT trr_actionresponse_pkey PRIMARY KEY (id);


--
-- Name: trr_charge trr_charge_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_charge
    ADD CONSTRAINT trr_charge_pkey PRIMARY KEY (id);


--
-- Name: trr_subjectweapon trr_subjectweapon_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_subjectweapon
    ADD CONSTRAINT trr_subjectweapon_pkey PRIMARY KEY (id);


--
-- Name: trr_trr trr_trr_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trr
    ADD CONSTRAINT trr_trr_pkey PRIMARY KEY (id);


--
-- Name: trr_trrstatus trr_trrstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trrstatus
    ADD CONSTRAINT trr_trrstatus_pkey PRIMARY KEY (id);


--
-- Name: trr_weapondischarge trr_weapondischarge_pkey; Type: CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_weapondischarge
    ADD CONSTRAINT trr_weapondischarge_pkey PRIMARY KEY (id);


--
-- Name: data_allegation_5f70871c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_5f70871c ON public.data_allegation USING btree (beat_id);


--
-- Name: data_allegation_areas_allegation_id_1ccd7982; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_areas_allegation_id_1ccd7982 ON public.data_allegation_areas USING btree (allegation_id);


--
-- Name: data_allegation_areas_allegation_id_1ccd7982_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_areas_allegation_id_1ccd7982_like ON public.data_allegation_areas USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_allegation_areas_area_id_e57d0e71; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_areas_area_id_e57d0e71 ON public.data_allegation_areas USING btree (area_id);


--
-- Name: data_allegation_crid_1770709b_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_crid_1770709b_like ON public.data_allegation USING btree (crid varchar_pattern_ops);


--
-- Name: data_allegation_line_areas_allegation_id_6c00ce82; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_line_areas_allegation_id_6c00ce82 ON public.data_allegation_line_areas USING btree (allegation_id);


--
-- Name: data_allegation_line_areas_allegation_id_6c00ce82_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_line_areas_allegation_id_6c00ce82_like ON public.data_allegation_line_areas USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_allegation_line_areas_linearea_id_b5b1b663; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_line_areas_linearea_id_b5b1b663 ON public.data_allegation_line_areas USING btree (linearea_id);


--
-- Name: data_allegation_most_common_category_id_88004da7; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_most_common_category_id_88004da7 ON public.data_allegation USING btree (most_common_category_id);


--
-- Name: data_allegation_point_id; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_allegation_point_id ON public.data_allegation USING gist (point);


--
-- Name: data_area_commander_id_45ac9547; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_area_commander_id_45ac9547 ON public.data_area USING btree (commander_id);


--
-- Name: data_area_police_hq_id_a848cb39; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_area_police_hq_id_a848cb39 ON public.data_area USING btree (police_hq_id);


--
-- Name: data_area_polygon_id; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_area_polygon_id ON public.data_area USING gist (polygon);


--
-- Name: data_attachmentfile_196c2a24; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_196c2a24 ON public.data_attachmentfile USING btree (original_url);


--
-- Name: data_attachmentfile_572d4e42; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_572d4e42 ON public.data_attachmentfile USING btree (url);


--
-- Name: data_attachmentfile_68a7d484; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_68a7d484 ON public.data_attachmentfile USING btree (file_type);


--
-- Name: data_attachmentfile_allegation_id_1b6443a8; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_allegation_id_1b6443a8 ON public.data_attachmentfile USING btree (allegation_id);


--
-- Name: data_attachmentfile_allegation_id_1b6443a8_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_allegation_id_1b6443a8_like ON public.data_attachmentfile USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_attachmentfile_external_id_d823de40; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_external_id_d823de40 ON public.data_attachmentfile USING btree (external_id);


--
-- Name: data_attachmentfile_external_id_d823de40_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_external_id_d823de40_like ON public.data_attachmentfile USING btree (external_id varchar_pattern_ops);


--
-- Name: data_attachmentfile_file_type_28f6a0c3_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_file_type_28f6a0c3_like ON public.data_attachmentfile USING btree (file_type varchar_pattern_ops);


--
-- Name: data_attachmentfile_last_updated_by_id_061dfbf8; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_last_updated_by_id_061dfbf8 ON public.data_attachmentfile USING btree (last_updated_by_id);


--
-- Name: data_attachmentfile_original_url_a70b5f02_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_original_url_a70b5f02_like ON public.data_attachmentfile USING btree (original_url varchar_pattern_ops);


--
-- Name: data_attachmentfile_source_type_534b7b9f; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_source_type_534b7b9f ON public.data_attachmentfile USING btree (source_type);


--
-- Name: data_attachmentfile_source_type_534b7b9f_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_source_type_534b7b9f_like ON public.data_attachmentfile USING btree (source_type varchar_pattern_ops);


--
-- Name: data_attachmentfile_url_89b39fb4_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_attachmentfile_url_89b39fb4_like ON public.data_attachmentfile USING btree (url varchar_pattern_ops);


--
-- Name: data_award_officer_id_92c5d789; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_award_officer_id_92c5d789 ON public.data_award USING btree (officer_id);


--
-- Name: data_complainant_allegation_id_f5452147; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_complainant_allegation_id_f5452147 ON public.data_complainant USING btree (allegation_id);


--
-- Name: data_complainant_allegation_id_f5452147_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_complainant_allegation_id_f5452147_like ON public.data_complainant USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_investigator_first_name_21d1280b; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigator_first_name_21d1280b ON public.data_investigator USING btree (first_name);


--
-- Name: data_investigator_first_name_21d1280b_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigator_first_name_21d1280b_like ON public.data_investigator USING btree (first_name varchar_pattern_ops);


--
-- Name: data_investigator_last_name_adf05435; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigator_last_name_adf05435 ON public.data_investigator USING btree (last_name);


--
-- Name: data_investigator_last_name_adf05435_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigator_last_name_adf05435_like ON public.data_investigator USING btree (last_name varchar_pattern_ops);


--
-- Name: data_investigator_officer_id_8095dac6; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigator_officer_id_8095dac6 ON public.data_investigator USING btree (officer_id);


--
-- Name: data_investigatorallegation_allegation_id_655b5938; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigatorallegation_allegation_id_655b5938 ON public.data_investigatorallegation USING btree (allegation_id);


--
-- Name: data_investigatorallegation_allegation_id_655b5938_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigatorallegation_allegation_id_655b5938_like ON public.data_investigatorallegation USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_investigatorallegation_current_unit_id_da1ab9e3; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigatorallegation_current_unit_id_da1ab9e3 ON public.data_investigatorallegation USING btree (current_unit_id);


--
-- Name: data_investigatorallegation_investigator_id_cd1fd6b1; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_investigatorallegation_investigator_id_cd1fd6b1 ON public.data_investigatorallegation USING btree (investigator_id);


--
-- Name: data_involvement_allegation_id_c248e036; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_involvement_allegation_id_c248e036 ON public.data_involvement USING btree (allegation_id);


--
-- Name: data_involvement_allegation_id_c248e036_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_involvement_allegation_id_c248e036_like ON public.data_involvement USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_involvement_e1d6855c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_involvement_e1d6855c ON public.data_involvement USING btree (officer_id);


--
-- Name: data_linearea_geom_id; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_linearea_geom_id ON public.data_linearea USING gist (geom);


--
-- Name: data_office_current_f8bc5a_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_office_current_f8bc5a_idx ON public.data_officerbadgenumber USING btree (current);


--
-- Name: data_office_effecti_f0cc97_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_office_effecti_f0cc97_idx ON public.data_officerhistory USING btree (effective_date);


--
-- Name: data_office_end_dat_a1e9be_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_office_end_dat_a1e9be_idx ON public.data_officerhistory USING btree (end_date);


--
-- Name: data_office_start_d_8e9651_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_office_start_d_8e9651_idx ON public.data_officerallegation USING btree (start_date);


--
-- Name: data_office_year_c8b488_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_office_year_c8b488_idx ON public.data_officeryearlypercentile USING btree (year);


--
-- Name: data_officer_2a034e9d; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officer_2a034e9d ON public.data_officer USING btree (first_name);


--
-- Name: data_officer_7d4553c0; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officer_7d4553c0 ON public.data_officer USING btree (last_name);


--
-- Name: data_officer_last_unit_id_b746c190; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officer_last_unit_id_b746c190 ON public.data_officer USING btree (last_unit_id);


--
-- Name: data_officeralias_8b44b9c5; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officeralias_8b44b9c5 ON public.data_officeralias USING btree (new_officer_id);


--
-- Name: data_officerallegation_allegation_id_429ce710; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerallegation_allegation_id_429ce710 ON public.data_officerallegation USING btree (allegation_id);


--
-- Name: data_officerallegation_allegation_id_429ce710_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerallegation_allegation_id_429ce710_like ON public.data_officerallegation USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_officerallegation_e1d6855c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerallegation_e1d6855c ON public.data_officerallegation USING btree (officer_id);


--
-- Name: data_officerallegation_f5234087; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerallegation_f5234087 ON public.data_officerallegation USING btree (allegation_category_id);


--
-- Name: data_officerbadgenumber_e1d6855c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerbadgenumber_e1d6855c ON public.data_officerbadgenumber USING btree (officer_id);


--
-- Name: data_officerhistory_e1d6855c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerhistory_e1d6855c ON public.data_officerhistory USING btree (officer_id);


--
-- Name: data_officerhistory_e8175980; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officerhistory_e8175980 ON public.data_officerhistory USING btree (unit_id);


--
-- Name: data_officeryearlypercentile_officer_id_310c59d7; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_officeryearlypercentile_officer_id_310c59d7 ON public.data_officeryearlypercentile USING btree (officer_id);


--
-- Name: data_policewitness_allegation_id_b8dc2d75; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_policewitness_allegation_id_b8dc2d75 ON public.data_policewitness USING btree (allegation_id);


--
-- Name: data_policewitness_allegation_id_b8dc2d75_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_policewitness_allegation_id_b8dc2d75_like ON public.data_policewitness USING btree (allegation_id varchar_pattern_ops);


--
-- Name: data_policewitness_e1d6855c; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_policewitness_e1d6855c ON public.data_policewitness USING btree (officer_id);


--
-- Name: data_racepopulation_area_id_4ae23fb5; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_racepopulation_area_id_4ae23fb5 ON public.data_racepopulation USING btree (area_id);


--
-- Name: data_salary_officer_id_8d6c46ab; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_salary_officer_id_8d6c46ab ON public.data_salary USING btree (officer_id);


--
-- Name: data_salary_year_51b276_idx; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_salary_year_51b276_idx ON public.data_salary USING btree (year);


--
-- Name: data_victim_allegation_id_bef5a29d; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_victim_allegation_id_bef5a29d ON public.data_victim USING btree (allegation_id);


--
-- Name: data_victim_allegation_id_bef5a29d_like; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX data_victim_allegation_id_bef5a29d_like ON public.data_victim USING btree (allegation_id varchar_pattern_ops);


--
-- Name: trr_actionresponse_trr_id_59e4c15b; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_actionresponse_trr_id_59e4c15b ON public.trr_actionresponse USING btree (trr_id);


--
-- Name: trr_charge_trr_id_983da4e1; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_charge_trr_id_983da4e1 ON public.trr_charge USING btree (trr_id);


--
-- Name: trr_subjectweapon_trr_id_bac23e40; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_subjectweapon_trr_id_bac23e40 ON public.trr_subjectweapon USING btree (trr_id);


--
-- Name: trr_trr_officer_id_75e45524; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trr_officer_id_75e45524 ON public.trr_trr USING btree (officer_id);


--
-- Name: trr_trr_officer_unit_detail_id_3db18cbd; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trr_officer_unit_detail_id_3db18cbd ON public.trr_trr USING btree (officer_unit_detail_id);


--
-- Name: trr_trr_officer_unit_id_fc0d7ceb; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trr_officer_unit_id_fc0d7ceb ON public.trr_trr USING btree (officer_unit_id);


--
-- Name: trr_trr_point_id; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trr_point_id ON public.trr_trr USING gist (point);


--
-- Name: trr_trrstatus_officer_id_e12565ea; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trrstatus_officer_id_e12565ea ON public.trr_trrstatus USING btree (officer_id);


--
-- Name: trr_trrstatus_trr_id_3285fe79; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_trrstatus_trr_id_3285fe79 ON public.trr_trrstatus USING btree (trr_id);


--
-- Name: trr_weapondischarge_trr_id_a259df23; Type: INDEX; Schema: public; Owner: cpdb
--

CREATE INDEX trr_weapondischarge_trr_id_a259df23 ON public.trr_weapondischarge USING btree (trr_id);


--
-- Name: data_allegation_areas data_allegation_area_allegation_id_1ccd7982_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_areas
    ADD CONSTRAINT data_allegation_area_allegation_id_1ccd7982_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_allegation_areas data_allegation_areas_area_id_e57d0e71_fk_data_area_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_areas
    ADD CONSTRAINT data_allegation_areas_area_id_e57d0e71_fk_data_area_id FOREIGN KEY (area_id) REFERENCES public.data_area(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_allegation data_allegation_beat_id_3812d8f9_fk_data_area_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation
    ADD CONSTRAINT data_allegation_beat_id_3812d8f9_fk_data_area_id FOREIGN KEY (beat_id) REFERENCES public.data_area(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_allegation_line_areas data_allegation_line_allegation_id_6c00ce82_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_line_areas
    ADD CONSTRAINT data_allegation_line_allegation_id_6c00ce82_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_allegation_line_areas data_allegation_line_linearea_id_b5b1b663_fk_data_line; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation_line_areas
    ADD CONSTRAINT data_allegation_line_linearea_id_b5b1b663_fk_data_line FOREIGN KEY (linearea_id) REFERENCES public.data_linearea(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_allegation data_allegation_most_common_category_88004da7_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_allegation
    ADD CONSTRAINT data_allegation_most_common_category_88004da7_fk_data_alle FOREIGN KEY (most_common_category_id) REFERENCES public.data_allegationcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_area data_area_commander_id_45ac9547_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_area
    ADD CONSTRAINT data_area_commander_id_45ac9547_fk_data_officer_id FOREIGN KEY (commander_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_area data_area_police_hq_id_a848cb39_fk_data_area_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_area
    ADD CONSTRAINT data_area_police_hq_id_a848cb39_fk_data_area_id FOREIGN KEY (police_hq_id) REFERENCES public.data_area(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_attachmentfile data_attachmentfile_allegation_id_1b6443a8_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_attachmentfile
    ADD CONSTRAINT data_attachmentfile_allegation_id_1b6443a8_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_attachmentfile data_attachmentfile_last_updated_by_id_061dfbf8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_attachmentfile
    ADD CONSTRAINT data_attachmentfile_last_updated_by_id_061dfbf8_fk_auth_user_id FOREIGN KEY (last_updated_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_award data_award_officer_id_92c5d789_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_award
    ADD CONSTRAINT data_award_officer_id_92c5d789_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_complainant data_complainant_allegation_id_f5452147_fk_data_allegation_crid; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_complainant
    ADD CONSTRAINT data_complainant_allegation_id_f5452147_fk_data_allegation_crid FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_investigator data_investigator_officer_id_8095dac6_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigator
    ADD CONSTRAINT data_investigator_officer_id_8095dac6_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_investigatorallegation data_investigatorall_allegation_id_655b5938_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigatorallegation
    ADD CONSTRAINT data_investigatorall_allegation_id_655b5938_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_investigatorallegation data_investigatorall_current_unit_id_da1ab9e3_fk_data_poli; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigatorallegation
    ADD CONSTRAINT data_investigatorall_current_unit_id_da1ab9e3_fk_data_poli FOREIGN KEY (current_unit_id) REFERENCES public.data_policeunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_investigatorallegation data_investigatorall_investigator_id_cd1fd6b1_fk_data_inve; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_investigatorallegation
    ADD CONSTRAINT data_investigatorall_investigator_id_cd1fd6b1_fk_data_inve FOREIGN KEY (investigator_id) REFERENCES public.data_investigator(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_involvement data_involvement_allegation_id_c248e036_fk_data_allegation_crid; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_involvement
    ADD CONSTRAINT data_involvement_allegation_id_c248e036_fk_data_allegation_crid FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_involvement data_involvement_officer_id_73520b64_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_involvement
    ADD CONSTRAINT data_involvement_officer_id_73520b64_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officer data_officer_last_unit_id_b746c190_fk_data_policeunit_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officer
    ADD CONSTRAINT data_officer_last_unit_id_b746c190_fk_data_policeunit_id FOREIGN KEY (last_unit_id) REFERENCES public.data_policeunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officeralias data_officeralias_new_officer_id_4f38b294_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeralias
    ADD CONSTRAINT data_officeralias_new_officer_id_4f38b294_fk_data_officer_id FOREIGN KEY (new_officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerallegation data_officerallegati_allegation_category__023a83f1_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerallegation
    ADD CONSTRAINT data_officerallegati_allegation_category__023a83f1_fk_data_alle FOREIGN KEY (allegation_category_id) REFERENCES public.data_allegationcategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerallegation data_officerallegati_allegation_id_429ce710_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerallegation
    ADD CONSTRAINT data_officerallegati_allegation_id_429ce710_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerallegation data_officerallegation_officer_id_a68f4888_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerallegation
    ADD CONSTRAINT data_officerallegation_officer_id_a68f4888_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerbadgenumber data_officerbadgenumber_officer_id_c76d8363_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerbadgenumber
    ADD CONSTRAINT data_officerbadgenumber_officer_id_c76d8363_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerhistory data_officerhistory_officer_id_db19fe27_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerhistory
    ADD CONSTRAINT data_officerhistory_officer_id_db19fe27_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officerhistory data_officerhistory_unit_id_c33c0072_fk_data_policeunit_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officerhistory
    ADD CONSTRAINT data_officerhistory_unit_id_c33c0072_fk_data_policeunit_id FOREIGN KEY (unit_id) REFERENCES public.data_policeunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_officeryearlypercentile data_officeryearlype_officer_id_310c59d7_fk_data_offi; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_officeryearlypercentile
    ADD CONSTRAINT data_officeryearlype_officer_id_310c59d7_fk_data_offi FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_policewitness data_policewitness_allegation_id_b8dc2d75_fk_data_alle; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policewitness
    ADD CONSTRAINT data_policewitness_allegation_id_b8dc2d75_fk_data_alle FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_policewitness data_policewitness_officer_id_8d0c044d_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_policewitness
    ADD CONSTRAINT data_policewitness_officer_id_8d0c044d_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_racepopulation data_racepopulation_area_id_4ae23fb5_fk_data_area_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_racepopulation
    ADD CONSTRAINT data_racepopulation_area_id_4ae23fb5_fk_data_area_id FOREIGN KEY (area_id) REFERENCES public.data_area(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_salary data_salary_officer_id_8d6c46ab_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_salary
    ADD CONSTRAINT data_salary_officer_id_8d6c46ab_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: data_victim data_victim_allegation_id_bef5a29d_fk_data_allegation_crid; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.data_victim
    ADD CONSTRAINT data_victim_allegation_id_bef5a29d_fk_data_allegation_crid FOREIGN KEY (allegation_id) REFERENCES public.data_allegation(crid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_actionresponse trr_actionresponse_trr_id_59e4c15b_fk_trr_trr_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_actionresponse
    ADD CONSTRAINT trr_actionresponse_trr_id_59e4c15b_fk_trr_trr_id FOREIGN KEY (trr_id) REFERENCES public.trr_trr(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_charge trr_charge_trr_id_983da4e1_fk_trr_trr_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_charge
    ADD CONSTRAINT trr_charge_trr_id_983da4e1_fk_trr_trr_id FOREIGN KEY (trr_id) REFERENCES public.trr_trr(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_subjectweapon trr_subjectweapon_trr_id_bac23e40_fk_trr_trr_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_subjectweapon
    ADD CONSTRAINT trr_subjectweapon_trr_id_bac23e40_fk_trr_trr_id FOREIGN KEY (trr_id) REFERENCES public.trr_trr(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_trr trr_trr_officer_id_75e45524_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trr
    ADD CONSTRAINT trr_trr_officer_id_75e45524_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_trr trr_trr_officer_unit_detail_id_3db18cbd_fk_data_policeunit_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trr
    ADD CONSTRAINT trr_trr_officer_unit_detail_id_3db18cbd_fk_data_policeunit_id FOREIGN KEY (officer_unit_detail_id) REFERENCES public.data_policeunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_trr trr_trr_officer_unit_id_fc0d7ceb_fk_data_policeunit_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trr
    ADD CONSTRAINT trr_trr_officer_unit_id_fc0d7ceb_fk_data_policeunit_id FOREIGN KEY (officer_unit_id) REFERENCES public.data_policeunit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_trrstatus trr_trrstatus_officer_id_e12565ea_fk_data_officer_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trrstatus
    ADD CONSTRAINT trr_trrstatus_officer_id_e12565ea_fk_data_officer_id FOREIGN KEY (officer_id) REFERENCES public.data_officer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_trrstatus trr_trrstatus_trr_id_3285fe79_fk_trr_trr_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_trrstatus
    ADD CONSTRAINT trr_trrstatus_trr_id_3285fe79_fk_trr_trr_id FOREIGN KEY (trr_id) REFERENCES public.trr_trr(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: trr_weapondischarge trr_weapondischarge_trr_id_a259df23_fk_trr_trr_id; Type: FK CONSTRAINT; Schema: public; Owner: cpdb
--

ALTER TABLE ONLY public.trr_weapondischarge
    ADD CONSTRAINT trr_weapondischarge_trr_id_a259df23_fk_trr_trr_id FOREIGN KEY (trr_id) REFERENCES public.trr_trr(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: TABLE data_allegation; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_allegation TO numeracy;
GRANT SELECT ON TABLE public.data_allegation TO notebook;


--
-- Name: TABLE data_allegation_areas; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_allegation_areas TO civis;


--
-- Name: TABLE data_allegation_line_areas; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_allegation_line_areas TO civis;


--
-- Name: TABLE data_allegationcategory; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_allegationcategory TO numeracy;
GRANT SELECT ON TABLE public.data_allegationcategory TO notebook;
GRANT SELECT ON TABLE public.data_allegationcategory TO civis;


--
-- Name: TABLE data_area; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_area TO numeracy;
GRANT SELECT ON TABLE public.data_area TO notebook;
GRANT SELECT ON TABLE public.data_area TO civis;


--
-- Name: TABLE data_attachmentfile; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_attachmentfile TO numeracy;
GRANT SELECT ON TABLE public.data_attachmentfile TO notebook;
GRANT SELECT ON TABLE public.data_attachmentfile TO civis;


--
-- Name: TABLE data_award; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_award TO numeracy;
GRANT SELECT ON TABLE public.data_award TO notebook;
GRANT SELECT ON TABLE public.data_award TO civis;


--
-- Name: TABLE data_complainant; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_complainant TO numeracy;
GRANT SELECT ON TABLE public.data_complainant TO notebook;
GRANT SELECT ON TABLE public.data_complainant TO civis;


--
-- Name: TABLE data_investigator; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_investigator TO numeracy;
GRANT SELECT ON TABLE public.data_investigator TO notebook;
GRANT SELECT ON TABLE public.data_investigator TO civis;


--
-- Name: TABLE data_investigatorallegation; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_investigatorallegation TO numeracy;
GRANT SELECT ON TABLE public.data_investigatorallegation TO notebook;
GRANT SELECT ON TABLE public.data_investigatorallegation TO civis;


--
-- Name: TABLE data_involvement; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_involvement TO numeracy;
GRANT SELECT ON TABLE public.data_involvement TO notebook;
GRANT SELECT ON TABLE public.data_involvement TO civis;


--
-- Name: TABLE data_linearea; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_linearea TO numeracy;
GRANT SELECT ON TABLE public.data_linearea TO notebook;
GRANT SELECT ON TABLE public.data_linearea TO civis;


--
-- Name: TABLE data_officer; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officer TO numeracy;
GRANT SELECT ON TABLE public.data_officer TO notebook;
GRANT SELECT ON TABLE public.data_officer TO civis;


--
-- Name: TABLE data_officeralias; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officeralias TO numeracy;
GRANT SELECT ON TABLE public.data_officeralias TO notebook;
GRANT SELECT ON TABLE public.data_officeralias TO civis;


--
-- Name: TABLE data_officerallegation; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officerallegation TO numeracy;
GRANT SELECT ON TABLE public.data_officerallegation TO notebook;
GRANT SELECT ON TABLE public.data_officerallegation TO civis;


--
-- Name: TABLE data_officerbadgenumber; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officerbadgenumber TO numeracy;
GRANT SELECT ON TABLE public.data_officerbadgenumber TO notebook;
GRANT SELECT ON TABLE public.data_officerbadgenumber TO civis;


--
-- Name: TABLE data_officerhistory; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officerhistory TO numeracy;
GRANT SELECT ON TABLE public.data_officerhistory TO notebook;
GRANT SELECT ON TABLE public.data_officerhistory TO civis;


--
-- Name: TABLE data_officeryearlypercentile; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_officeryearlypercentile TO civis;


--
-- Name: TABLE data_pipeline_appliedfixture; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_pipeline_appliedfixture TO civis;


--
-- Name: TABLE data_policeunit; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_policeunit TO numeracy;
GRANT SELECT ON TABLE public.data_policeunit TO notebook;
GRANT SELECT ON TABLE public.data_policeunit TO civis;


--
-- Name: TABLE data_policewitness; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_policewitness TO numeracy;
GRANT SELECT ON TABLE public.data_policewitness TO notebook;
GRANT SELECT ON TABLE public.data_policewitness TO civis;


--
-- Name: TABLE data_racepopulation; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_racepopulation TO numeracy;
GRANT SELECT ON TABLE public.data_racepopulation TO notebook;
GRANT SELECT ON TABLE public.data_racepopulation TO civis;


--
-- Name: TABLE data_salary; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_salary TO numeracy;
GRANT SELECT ON TABLE public.data_salary TO notebook;
GRANT SELECT ON TABLE public.data_salary TO civis;


--
-- Name: TABLE data_versioning_changelog; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_versioning_changelog TO numeracy;
GRANT SELECT ON TABLE public.data_versioning_changelog TO notebook;
GRANT SELECT ON TABLE public.data_versioning_changelog TO civis;


--
-- Name: TABLE data_victim; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.data_victim TO numeracy;
GRANT SELECT ON TABLE public.data_victim TO notebook;
GRANT SELECT ON TABLE public.data_victim TO civis;


--
-- Name: TABLE trr_actionresponse; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_actionresponse TO numeracy;
GRANT SELECT ON TABLE public.trr_actionresponse TO notebook;
GRANT SELECT ON TABLE public.trr_actionresponse TO civis;


--
-- Name: TABLE trr_charge; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_charge TO numeracy;
GRANT SELECT ON TABLE public.trr_charge TO notebook;
GRANT SELECT ON TABLE public.trr_charge TO civis;


--
-- Name: TABLE trr_subjectweapon; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_subjectweapon TO numeracy;
GRANT SELECT ON TABLE public.trr_subjectweapon TO notebook;
GRANT SELECT ON TABLE public.trr_subjectweapon TO civis;


--
-- Name: TABLE trr_trr; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_trr TO numeracy;
GRANT SELECT ON TABLE public.trr_trr TO notebook;
GRANT SELECT ON TABLE public.trr_trr TO civis;


--
-- Name: TABLE trr_trrstatus; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_trrstatus TO numeracy;
GRANT SELECT ON TABLE public.trr_trrstatus TO notebook;
GRANT SELECT ON TABLE public.trr_trrstatus TO civis;


--
-- Name: TABLE trr_weapondischarge; Type: ACL; Schema: public; Owner: cpdb
--

GRANT SELECT ON TABLE public.trr_weapondischarge TO numeracy;
GRANT SELECT ON TABLE public.trr_weapondischarge TO notebook;
GRANT SELECT ON TABLE public.trr_weapondischarge TO civis;


--
-- PostgreSQL database dump complete
--

