# Скрипт для взлома электронного дневника школьника

Скрипт, с помощью которого можно исправить оценки, удалить негативные и добавить похвальные замечания в электронном дневнике школьника. 




## Запуск

- Сайт электронного дневника уже должен быть настроен и работать (см. описание и инструкции по запуску в репозитории [электронного дневника школы](https://github.com/devmanorg/e-diary/tree/master))
- Проверьте наличие [переменных окружения](https://github.com/devmanorg/e-diary/tree/master#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
- Cайт будет доступен по адресу: [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
- Скачайте код из [репозитория](https://github.com/ArkJzzz/db_hack.git)
- Скачайте [архив с базой данных](https://dvmn.org/filer/canonical/1562234129/166/)
- Поместите файл со скриптами и файл базы данных рядом с `manage.py`
- Запустите Django shell
```bash
python3 manage.py shell
```
- Подключите скрипт
```python
import scripts
```


## Использование

- Получить учетную запись необходимого ученика 
```python
schoolkid = scripts.find_schoolkid('<Фамилия Имя>')
```

- Исправить плохие оценки:
```python
scripts.fix_marks(schoolkid)
```

- Удалить все замечания ученика:
```python
scripts.remove_chastisements(schoolkid)
```

- Добавить похвалу ученику:
```python
scripts.create_commendation(schoolkid, '<Предмет>')
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
