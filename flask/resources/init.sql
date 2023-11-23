create table public.university
(
    id         serial
        primary key,
    full_name  varchar,
    small_name varchar,
    date       date
);

alter table public.university
    owner to postgres;

create table public.student
(
    id         serial
        primary key,
    name       varchar,
    date       date,
    university integer
        references public.university,
    year       integer
);

alter table public.student
    owner to postgres;

create table public.users
(
    id       serial
        primary key,
    username varchar(50) not null,
    password varchar(50) not null
);

alter table public.users
    owner to postgres;