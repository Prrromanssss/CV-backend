# Сайт-резюме на Django

![flake8 test](https://github.com/Prrromanssss/CV-django/actions/workflows/python-package.yml/badge.svg)


Данный проект представляет из себя творческое задание для поступления на [Django интенсивы от Академия](https://academy.yandex.ru/intensive/django), а именно сайт-резюме, написанный на фреймворке Django.
На нем я рассказал о своих увлечениях, опыте разработки.

[Подробнее о фреймворке Django](https://www.djangoproject.com/)
***
Для его __запуска__ нам необходимо:
* склонировать проект из гитхаба
```commandline
git clone https://github.com/Prrromanssss/CV-django.git
```
* установить все необходимые зависимости
```commandline
pip install -r requirements.txt
```
* для поднятия сервера используется файл manage.py, давайте запустим его
```commandline
cd mysite
python manage.py runserver
```
Итак, мы запустили наш сайт на локальном хосте, на 8000 порте(этот порт стоит по умолчанию при запуске сервера)
***
Сайт является одностраничным, на котором представлена моя фотография и мое краткое резюме.

Подключение базы данных здесь не представлена, для данного проекта она нам не требуется. Верстка выполнена при помощи фреймворка [bootstrap](https://getbootstrap.com/)

