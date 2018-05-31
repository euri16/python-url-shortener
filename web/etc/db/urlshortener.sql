CREATE ROLE urlsdba WITH LOGIN CONNECTION LIMIT -1 ENCRYPTED PASSWORD '#T%a1-sC32zFZju_XFr"!~Y6k3YU{dD9';
CREATE TABLESPACE urlshortener OWNER urlsdba LOCATION '/var/chroot/pgsql/data/urlshortener';
CREATE DATABASE urlshortener WITH OWNER urlsdba TEMPLATE template0 ENCODING 'UTF8' TABLESPACE urlshortener CONNECTION LIMIT 1024;

---update pg_database set datistemplate = FALSE where datname = 'template1';
---drop database urlshortener;
---create database urlshortener with template = template0 encoding = 'UTF8';
---update pg_database set datistemplate = TRUE where datname = 'template1';

--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
--

\connect urlshortener

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- DATA STRUCTURE DEFINITION
--

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO urlsdba;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO urlsdba;
