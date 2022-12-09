# Yacut сервис укорачивания ссылок и API к нему
Технологии:
Python, Flask, Flask-Migrate, SQLalchemy, Html|CSS
Ключевые возможности сервиса:
генерация коротких ссылок и связь их с исходными длинными ссылками,
переадресация на исходный адрес при обращении к коротким ссылкам.
Пользовательский интерфейс сервиса — одна страница с формой. Эта форма должна состоять из двух полей:
обязательного для длинной исходной ссылки;
необязательного для пользовательского варианта короткой ссылки.


Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AlexGriv/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Автор
AlexGriv
https://github.com/AlexGriv

