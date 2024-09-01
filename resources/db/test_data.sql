-- Пользователи
insert into users(user_id, username, first_name, last_name)
values (5453594403, 'vit73123', 'Vit', 'A');

insert into users(user_id, username, first_name, last_name)
values (2122321367, 'vrnov33', 'Vladimir', 'Rodionov');


-- Статусы
insert into statuses(text, grade, user_id)
values ('aaa', 3, 1);

insert into statuses(text, grade, user_id)
values ('bb', 2, 2);

insert into statuses(text, grade, user_id)
values ('aaa aaaa', 4, 1);

insert into statuses(text, grade, user_id)
values ('a a a', 0, 1);

insert into statuses(text, grade, user_id)
values ('bb bbbb', 1, 2);


select * from users join statuses on users.id = statuses.user_id order by statuses.updated_at desc limit(1)
