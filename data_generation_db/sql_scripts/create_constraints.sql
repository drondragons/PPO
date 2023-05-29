alter table if exists public.roles 
	add constraint role_name_unique unique(name);


alter table if exists public.book_statuses
	add constraint book_status_name_unique unique(name);
	

alter table if exists public.users
	add constraint user_role_fk foreign key(role_id)
		references public.roles(id)
		on delete cascade,
    add constraint user_login_unique unique(login),
    add constraint check_login_format check(login ~ '^[a-zA-Z0-9_-]{8,50}$'),
    add constraint user_email_unique unique(email),
    add constraint check_email_format check(email ~ '^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
    add constraint check_initials_format check(initials ~ '^[A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ-]* [A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ-]*(| [A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ-]*)$'),
    add constraint check_phone_number_format check((phone_number is null) or (phone_number ~ '^8\d{10}$')),
    add constraint check_birth_date check((birth_date is null) or (birth_date >= '1900-01-01' and birth_date <= current_date)),
	alter column role_id set default 2,
    alter column actuality set default true;


alter table if exists public.book_register
    add constraint book_register_user_fk foreign key(user_id)
        references public.users(id)
        on delete cascade,
    add constraint book_register_book_fk foreign key(book_id)
        references public.books(id)
        on delete cascade,
    add constraint book_register_book_status_fk foreign key(book_status_id)
        references public.book_statuses(id)
        on delete cascade,
    add constraint check_book_amount check(book_amount > 0),
    add constraint check_book_registration_date check(registration_date >= '1900-01-01 00:00:00' and registration_date <= current_timestamp);


alter table if exists public.books
    add constraint book_publisher_fk foreign key(publisher_id)
        references public.publishers(id)
        on delete cascade,
    add constraint check_isbn_length check(length(isbn) >= 15 and length(isbn) <= 17),
    add constraint check_isbn_format check(isbn ~ '^[\d-]{15,17}$'),
    add constraint check_pages_amount check(total_pages > 4),
    add constraint check_book_amount check(amount >= 0),
    add constraint check_publication_date check(publication_date >= 1500 and publication_date <= extract(year from current_date)),
    add constraint check_price check(price::money::numeric::float8 > 0),
    add constraint check_book_cover_photo_path_format check(cover_photo_path ~ '^\.\.\/TableData\/BooksPhoto\/[0-9а-яА-ЯёЁa-zA-Z_-]+\.(png|jpg|jpeg)$'),
	alter column cover_photo_path set default '../TableData/BooksPhoto/default_book_cover.png';


alter table if exists public.publishers
    add constraint publisher_country_fk foreign key(country_id)
        references public.countries(id)
        on delete cascade,
    add constraint publisher_title_unique unique(title);


alter table if exists public.countries
	add constraint country_title_unique unique(title);

		
alter table if exists public.languages 
	add constraint language_title_unique unique(title);	


alter table if exists public.book_literary_works
	add constraint book_literary_works_book_fk foreign key(book_id)
		references public.books(id)
		on delete cascade,
	add constraint book_literary_works_literary_work_fk foreign key(literary_work_id)
		references public.literary_works(id)
		on delete cascade;


alter table if exists public.literary_works
	add constraint check_writing_date check((writing_date is null) or (writing_date >= 1500 and writing_date <= extract(year from current_date))),
	add constraint check_text_path check((text_path is null) or (text_path ~ '^\.\.\/TableData\/BooksEpub\/[0-9а-яА-ЯёЁa-zA-Z_-]+\.epub$'));


alter table if exists public.author_literary_works
	add constraint author_literary_works_literary_work_fk foreign key(literary_work_id)
		references public.literary_works(id)
		on delete cascade,
	add constraint author_literary_works_author_fk foreign key(author_id)
		references public.authors(id)
		on delete cascade;

	
alter table if exists public.authors
	add constraint check_initials_format check(initials ~ '^[A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ-]* [A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ-]*$'),
	add constraint check_birth_date check((birth_date is null) or (birth_date >= '1500-01-01' and birth_date <= current_date)),
	add constraint check_death_date check((death_date is null) or (death_date > birth_date and death_date <= current_date)),
	add constraint check_author_photo_path_format check(photo_path ~ '^\.\.\/TableData\/AuthorsPhoto\/[0-9а-яА-ЯёЁa-zA-Z_-]+\.(png|jpg|jpeg)$'),
	alter column photo_path set default '../TableData/AuthorsPhoto/default_author_photo.jpg';


alter table if exists public.literary_work_genres
	add constraint literary_work_genres_literary_work_fk foreign key(literary_work_id)
		references public.literary_works(id)
		on delete cascade,
	add constraint literary_works_genres_genre_fk foreign key(genre_id)
		references public.genres(id)
		on delete cascade;


alter table if exists public.genres
	add constraint genre_title_unique unique(title);