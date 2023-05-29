-- Установка значения по умолчанию для поля <аннотация> таблицы книги.
create or replace function default_book_annotation()
returns trigger AS $book_annotation_trigger$
begin
    if new.annotation is null then
	    new.annotation := 'Аннотация по умолчанию для книги «' || new.title || '».';
    end if;
	return new;
end;
$book_annotation_trigger$ language plpgsql;

create trigger book_annotation_trigger
    before insert on public.books
	for each row 
    execute procedure default_book_annotation();


-- Установка значения по умолчанию для поля <описание> таблицы литературные произведения.
create or replace function default_literary_work_description()
returns trigger as $lw_description_trigger$
begin
    if new.description is null then
        new.description := 'Описание по умолчанию для произведения «' || new.title || '».';
    end if;
    return new;
end;
$lw_description_trigger$ language plpgsql;

create trigger lw_description_trigger 
    before insert on public.literary_works
    for each row 
    execute procedure default_literary_work_description();


-- Установка значения по умолчанию для поля <биография> таблицы авторы.
create or replace function default_author_biography()
returns trigger as $author_biography_trigger$
begin
    if new.biography is null then 
        new.biography := new.initials || ' - писатель. Биография по умолчанию.';
    end if;
    return new;
end;
$author_biography_trigger$ language plpgsql;

create trigger author_biography_trigger
    before insert on public.authors
    for each row
    execute procedure default_author_biography();


-- Установка значения по умолчанию для поля <описание> таблицы жанры.
create or replace function default_genre_description()
returns trigger as $genre_description_trigger$
begin
    if new.description is null then
        new.description := 'Описание жанра ' || new.title || ' по умолчанию.';
    end if;
    return new;
end;
$genre_description_trigger$ language plpgsql;

create trigger genre_description_trigger 
    before insert on public.genres
    for each row
    execute procedure default_genre_description();


-- Проверка соответствия количества книг.
create or replace function check_book_amount()
returns trigger as $book_amount_trigger$
begin
    if new.book_amount > (select amount from public.books where id = new.book_id) then
        raise exception 'Такое количество книг превышает их реальное количество!';
    end if;
    return new;
end;
$book_amount_trigger$ language plpgsql;

create trigger book_amount_trigger
    before insert on public.book_register
    for each row
    execute procedure check_book_amount();


-- Поиск информации по таблице авторов по подстроке из инициалов автора.
create or replace function find_person_by_substr_of_initials(substr text)
returns setof authors as $$
begin
    return query
    select * 
    from authors
    where substr = substring(initials, position(substr in initials), length(substr));
end;
$$ language plpgsql stable;

-- select id, user_id, book_id, book_status_id, book_amount, to_char(registration_date, 'HH24:MI:SS DD.MM.YYYY') as registration_date from book_register limit 10;
-- select initials, death_date, birth_date from authors where date_part('year', age(death_date, birth_date)) > 90;