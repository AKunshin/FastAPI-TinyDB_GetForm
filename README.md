# Web-приложение для определения заполненных форм.
-------

В базе данных хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Пример шаблона формы:
```
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```

Всего должно поддерживаться четыре типа данных полей: 
* email
* телефон
* дата
* текст.

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате +7 xxx xxx xx xx, дата передается в формате DD.MM.YYYY или YYYY-MM-DD.

Имя шаблона формы задается в свободной форме, например MyForm или Order Form.
Имена полей также задаются в свободной форме (желательно осмысленно), например user_name, order_date или lead_email.

-------
На вход по урлу /get_form POST запросом передаются данные такого вида:
```
f_name1=value1&f_name2=value2
```
В ответ нужно вернуть имя шаблона формы, если она была найдена.
Чтобы найти подходящий шаблон нужно выбрать тот, поля которого совпали с полями в присланной форме. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в форме.

Если подходящей формы не нашлось, вернуть ответ в следующем формате
```
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```

где FIELD_TYPE это тип поля, выбранный на основе правил валидации, проверка правил должна производиться в следующем порядке дата, телефон, email, текст.

# Установка и запуск
-------
```
git clone https://github.com/AKunshin/FastAPI-TinyDB_GetForm.git
cd FastAPI-TinyDB_GetForm
```
Необходимо создать вирутальное окружение и активировать его:
```
python3 -m venv env
```
Для Linux:
```
. ./env/bin/activate
```

Для Windows:
```
. .\env\Scripts\activate
```
Далее установить зависимости:
```
pip install -r requirements.txt
```
Для запуска сервера:
```
uvicorn main:app --reload
```
Перейдя по адресу http://127.0.0.1:8000/docs Вы увидите автоматически сгенерированную, интерактивную документацию по API (предоставленную Swagger UI)

Для автоматического тестирования используется pytest. Для запуска pytest, в новом окне терминала перейдите в папку проекта, активируйте вирутальное окружение. Запуск тестов производится командой:
```
pytest -v -s
```
* test_get_template_only_by_existing_fields - тестируется поиск шаблона, если в форме переданы только все поля из требуемого шаблона
* test_get_template_with_filds_from_diffrent_templates - тестируется поиск шаблона, если в форме переданы поля из разных шаблонов. Результат - шаблон, количество сопавших полей у которого больше всего
* test_not_found_template - тестируется вариант, в котором шаблон не найден

