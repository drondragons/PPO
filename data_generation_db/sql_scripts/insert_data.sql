\copy public.roles(name) from 'TableData/Roles.csv' delimiter '|' csv header null as '';

\copy public.book_statuses(name) from 'TableData/Statuses.csv' delimiter '|' csv header null as '';

\copy public.users(login, email, initials, role_id, phone_number, password, actuality, birth_date) from 'TableData/Users.csv' delimiter '|' csv header null as '' force not null actuality;

\copy public.languages(title) from 'TableData/Languages.csv' delimiter '|' csv header null as '';

\copy public.countries(title) from 'TableData/Countries.csv' delimiter '|' csv header null as '';

\copy public.publishers(title, country_id) from 'TableData/Publishers.csv' delimiter '|' csv header null as '';

\copy public.books(title, isbn, total_pages, amount, publication_date, publisher_id, price, annotation, cover_photo_path, library_location) from 'TableData/Books.csv' delimiter '|' csv header null as '';

\copy public.book_register(user_id, book_id, book_status_id, book_amount, registration_date) from 'TableData/BookRecords.csv' delimiter '|' csv header null as '';

\copy public.literary_works(title, writing_date, description, text_path) from 'TableData/LiteraryWorks.csv' delimiter '|' csv header null as '';

\copy public.book_literary_works(book_id, literary_work_id) from 'TableData/BookLiteraryWorks.csv' delimiter '|' csv header null as '';

\copy public.authors(initials, birth_date, death_date, photo_path, biography) from 'TableData/Authors.csv' delimiter '|' csv header null as '';

\copy public.author_literary_works(author_id, literary_work_id) from 'TableData/AuthorLiteraryWorks.csv' delimiter '|' csv header null as '';

\copy public.genres(title, description) from 'TableData/Genres.csv' delimiter '|' csv header null as '';

\copy public.literary_work_genres(literary_work_id, genre_id) from 'TableData/LiteraryWorkGenres.csv' delimiter '|' csv header null as '';
