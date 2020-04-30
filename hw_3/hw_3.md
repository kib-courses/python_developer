# Домашка 3

Все задания - продолжение кода из домашки №2

1. В классах Patient и PatientCollection логирование реализовать через декоратор:
```class Patient:

    @my_logging_decorator
    def __init__(self, ....):
        ....

    @my_logging_decorator
    def save(self):
        ....
```

У многих это уже реализовано, так что кому-то будет проще =)

2. Развернуть локально Postgres, MySQL или SQLite (последнее - проще всего). Сохранение и считывание данных теперь производить не из csv, а из БД.

3. Реализовать следующий интерфейс командной строки (рекомендация - через click):

- Добавление нового пользователя в БД: ```python homework/cli/cli.py create Имя Фамилия --birth-date 1990-01-01 --phone +7-916-000-00-00 --document-type паспорт --document-number 0000 000000```
- Вывод на экран первых 10 пользователей: ```python homework/cli/cli.py show```
- Вывод на экран произвольного количества пользователей: ```python homework/cli/cli.py show 8```
- Вывод на экран количества сохраненных пользователей: ```python homework/cli/cli.py count```