create database city_library with 
    owner = postgres
    encoding = 'UTF8'
    tablespace = pg_default
    connection limit = -1
    is_template = False;

comment on database city_library
    is 'База данных для курсового проекта.';

alter database city_library set datestyle to 'GERMAN, DMY';
alter database city_library set time zone 'Europe/Moscow';
alter database city_library set lc_monetary to 'ru_RU.UTF-8';