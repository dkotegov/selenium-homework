#### no_python_team

```
(env) SEISMOGRAPH_EXTENSIONS='selenium, mocker' pip install seismograph
```
Пользуемся "export" или:

Run -> Edit Configurations -> Environment variables:

* USERNAME=
* PASSWORD=
Опционально:
* BROWSER=CHROME
* USE_REMOTE=FALSE


```
./drivers/grid.sh
./drivers/node.sh
```

```
(env) python run_tests.py
```


http://st-jira.tech-mail.ru/browse/TECH-652

* Создать заметку с помощью нескольких текстовых полей
* Создать заметку с прикрепленными фотографиями
* Создать заметку с прикрепленной музыкой (+ поиск музыки)
* Создать заметку с прикрепленной картой
* Создать заметку и отметить пользователя
* Проверить удаление заметок и их восстановление
* Проверить возможность редактирования заметок
* Проверить возможность комментирования заметки
* Поставить "класс" заметке несколькими вариантами
* Поставить заметку в статус