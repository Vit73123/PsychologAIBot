-- Пользователи
insert into users(user_id, username, first_name, last_name, created_at)
values (5453594403, 'vit73123', 'Vit', 'A', '2024-09-01 19:00:00');

insert into users(user_id, username, first_name, last_name, created_at)
values (2122321367, 'vrnov33', 'Vladimir', 'Rodionov', '2024-09-01 19:01:00');

insert into users(user_id, username, first_name, last_name, created_at)
values (1111111111, 'Username A', 'First name A', 'Last name A', '2024-09-01 19:02:02');

insert into users(user_id, username, first_name, last_name, created_at)
values (2222222222, 'Username B', 'First name B', 'Last name B', '2024-09-01 19:03:00');

insert into users(user_id, username, first_name, last_name, created_at)
values (3333333333, 'Username C', 'First name C', 'Last name C', '2024-09-01 19:04:00');

-- Статусы
insert into statuses(text, grade, user_id, created_at)
values ('aaa', 3, 1, '2024-09-01 20:00:00');

insert into statuses(text, grade, user_id, created_at)
values ('bbb', 2, 2, '2024-09-01 20:01:00');

insert into statuses(text, grade, user_id, created_at)
values ('ccc', 4, 1, '2024-09-01 20:02:00');

insert into statuses(text, grade, user_id, created_at)
values ('ddd', 0, 1, '2024-09-01 20:03:00');

insert into statuses(text, grade, user_id, created_at)
values ('eee', 1, 2, '2024-09-01 20:04:00');

insert into statuses(text, grade, user_id, created_at)
values ('fff', 3, 2, '2024-09-01 20:05:00');

insert into statuses(text, grade, user_id, created_at)
values ('ggg', 3, 2, '2024-09-01 20:06:00');

insert into statuses(text, grade, user_id, created_at)
values ('hhh', 1, 3, '2024-09-01 20:07:00');

insert into statuses(text, grade, user_id, created_at)
values ('iii', 0, 3, '2024-09-01 20:08:00');

insert into statuses(text, grade, user_id, created_at)
values ('jjj', -1, 3, '2024-09-01 20:09:00');

insert into statuses(text, grade, user_id, created_at)
values ('kkk', -5, 4, '2024-09-01 20:10:00');

insert into statuses(text, grade, user_id, created_at)
values ('lll', -4, 4, '2024-09-01 20:11:00');

insert into statuses(text, grade, user_id, created_at)
values ('mmm', -3, 2, '2024-09-01 20:12:00');

insert into statuses(text, grade, user_id, created_at)
values ('nnn', 1, 1, '2024-09-01 20:13:00');

insert into statuses(text, grade, user_id, created_at)
values ('ooo', 1, 5, '2024-09-01 20:14:00');

-- insert into sessions(review, user_id, created_at)
-- values ('aaa aaa', 1,'2024-09-01 20:14:00');

select *
from users
         join statuses on users.id = statuses.user_id
order by statuses.updated_at desc;