INSERT INTO public.tasklists (list_id, name, description, created_dttm) VALUES (1, 'work_daily', 'Рабочий список дел', '2020-05-08 09:19:00.000000');
INSERT INTO public.tasklists (list_id, name, description, created_dttm) VALUES (3, 'rest_outside', 'Базовый список при загороных поездках', '2020-05-08 09:20:05.000000');
INSERT INTO public.tasklists (list_id, name, description, created_dttm) VALUES (4, 'daily_evening', 'Simple evening routine', '2020-05-08 12:21:36.000000');
INSERT INTO public.tasklists (list_id, name, description, created_dttm) VALUES (2, 'home_evening', 'Complex evening routine', '2020-05-08 12:24:08.000000');


INSERT INTO public.task (task_id, list_id, value, created_dttm) VALUES (1, 1, 'Выпить чашку кофе', '2020-05-08 09:20:59.000000');
INSERT INTO public.task (task_id, list_id, value, created_dttm) VALUES (2, 2, 'Почистить зубы', '2020-05-08 09:21:13.000000');
INSERT INTO public.task (task_id, list_id, value, created_dttm) VALUES (3, 3, 'Вынести мусор', '2020-05-08 09:21:24.000000');
INSERT INTO public.task (task_id, list_id, value, created_dttm) VALUES (4, 3, 'Помыть посуду', '2020-05-08 10:07:04.000000');
INSERT INTO public.task (task_id, list_id, value, created_dttm) VALUES (5, 2, 'Сделать уборку', '2020-05-08 10:07:26.000000');