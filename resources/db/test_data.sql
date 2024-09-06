-- Пользователи

insert into users(user_id, username, first_name, last_name, created_at, updated_at)
values (5453594403, 'vit73123', 'Vit', 'A', '2024-09-01 19:00:00', '2024-09-01 19:00:00');

insert into users(user_id, username, first_name, last_name, created_at, updated_at)
values (2122321367, 'vrnov33', 'Vladimir', 'Rodionov', '2024-09-01 19:01:00', '2024-09-01 19:01:00');

insert into users(user_id, username, first_name, last_name, created_at, updated_at)
values (1111111111, 'Username A', 'First name A', 'Last name A', '2024-09-01 19:02:02', '2024-09-01 19:02:02');

insert into users(user_id, username, first_name, last_name, created_at, updated_at)
values (2222222222, 'Username B', 'First name B', 'Last name B', '2024-09-01 19:03:00', '2024-09-01 19:03:00');

insert into users(user_id, username, first_name, last_name, created_at, updated_at)
values (3333333333, 'Username C', 'First name C', 'Last name C', '2024-09-01 19:04:00', '2024-09-01 19:04:00');

-- Статусы

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status aaa', 3, 1, '2024-09-01 20:00:00', '2024-09-01 20:00:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status bbb', 2, 2, '2024-09-01 20:01:00', '2024-09-01 20:01:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status ccc', 4, 1, '2024-09-01 20:02:00', '2024-09-01 20:02:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status ddd', 0, 1, '2024-09-01 20:03:00', '2024-09-01 20:03:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status eee', 1, 2, '2024-09-01 20:04:00', '2024-09-01 20:04:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status fff', 3, 2, '2024-09-01 20:05:00', '2024-09-01 20:05:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status ggg', 3, 2, '2024-09-01 20:06:00', '2024-09-01 20:06:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status hhh', 1, 3, '2024-09-01 20:07:00', '2024-09-01 20:07:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status iii', 0, 3, '2024-09-01 20:08:00', '2024-09-01 20:08:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status jjj', -1, 3, '2024-09-01 20:09:00', '2024-09-01 20:09:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status kkk', -5, 4, '2024-09-01 20:10:00', '2024-09-01 20:10:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status lll', -4, 4, '2024-09-01 20:11:00', '2024-09-01 20:11:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status mmm', -3, 2, '2024-09-01 20:12:00', '2024-09-01 20:12:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status nnn', 1, 1, '2024-09-01 20:13:00', '2024-09-01 20:13:00');

insert into statuses(text, grade, user_id, created_at, updated_at)
values ('status ooo', 1, 5, '2024-09-01 20:14:00', '2024-09-01 20:14:00');

-- Сеансы

insert into appointments(review, user_id, created_at, updated_at)
values ('review aaa', 1, '2024-09-01 20:00:00', '2024-09-01 20:00:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review bbb', 2, '2024-09-01 20:01:00', '2024-09-01 20:01:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review ccc', 1, '2024-09-01 20:02:00', '2024-09-01 20:02:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review ddd', 1, '2024-09-01 20:03:00', '2024-09-01 20:03:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review eee', 2, '2024-09-01 20:04:00', '2024-09-01 20:04:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review fff', 2, '2024-09-01 20:05:00', '2024-09-01 20:05:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review ggg', 2, '2024-09-01 20:06:00', '2024-09-01 20:06:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review hhh', 3, '2024-09-01 20:07:00', '2024-09-01 20:07:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review iii', 3, '2024-09-01 20:08:00', '2024-09-01 20:08:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review jjj', 3, '2024-09-01 20:09:00', '2024-09-01 20:09:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review kkk', 4, '2024-09-01 20:10:00', '2024-09-01 20:10:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review lll', 4, '2024-09-01 20:11:00', '2024-09-01 20:11:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review mmm', 2, '2024-09-01 20:12:00', '2024-09-01 20:12:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review nnn', 1, '2024-09-01 20:13:00', '2024-09-01 20:13:00');

insert into appointments(review, user_id, created_at, updated_at)
values ('review ooo', 5, '2024-09-01 20:14:00', '2024-09-01 20:14:00');

-- insert into sessions(review, user_id, created_at)
-- values ('aaa aaa', 1,'2024-09-01 20:14:00');

select *
from users
         join statuses on users.id = statuses.user_id
order by statuses.updated_at desc;