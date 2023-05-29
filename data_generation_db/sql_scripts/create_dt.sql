create table if not exists public.roles
(
	id smallserial primary key,
	name text not null
);


create table if not exists public.book_statuses
(
	id smallserial primary key,
	name text not null
);


create table if not exists public.users
(
	id serial primary key,
	login text not null,
	email text not null,
	initials text not null,
	role_id smallint not null,
	phone_number text,
	password text not null,
	birth_date date,
	actuality boolean not null
);


create table if not exists public.book_register
(
	id serial primary key,
	user_id integer not null,
	book_id integer not null,
	book_status_id smallint not null,
	book_amount integer not null,
	registration_date timestamp not null
);


create table if not exists public.books
(
	id serial primary key,
	title text not null,
	isbn text not null,
	total_pages smallint not null,
	amount integer not null,
	publication_date integer not null,
	publisher_id integer not null,
	price money not null,
	annotation text not null,
	cover_photo_path text not null,
	library_location text
);


create table if not exists public.publishers
(
	id serial primary key,
	title text not null,
	country_id smallint not null 
);


create table if not exists public.countries
(
	id smallserial primary key,
	title text not null
);


create table if not exists public.languages
(
	id smallserial primary key,
	title text not null
);


create table if not exists public.book_literary_works
(
	id serial primary key,
	book_id integer not null,
	literary_work_id integer not null
);


create table if not exists public.literary_works
(
	id serial primary key,
	title text not null,
	writing_date integer,
	description text not null,
	text_path text
);


create table if not exists public.author_literary_works
(
	id serial primary key,
	literary_work_id integer not null,
	author_id integer not null
);


create table if not exists public.authors
(
	id serial primary key,
	initials text not null,
	birth_date date,
	death_date date,
	photo_path text not null, 
	biography text not null
);


create table if not exists public.literary_work_genres
(
	id serial primary key,
	literary_work_id integer not null,
	genre_id smallint not null
);


create table if not exists public.genres
(
	id smallserial primary key,
	title text not null,
	description text not null
);