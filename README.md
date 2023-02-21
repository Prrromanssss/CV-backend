# Сайт-резюме на Django

![flake8 test](https://github.com/Prrromanssss/CV-django/actions/workflows/python-package.yml/badge.svg)


## About

This project is a creative task for applicants to [Django Web Development Intensives from the Yandex Academy](https://academy.yandex.ru/intensive/django), namely, a resume site written in the Django framework.
On it I told about my hobbies, development experience.

[Learn more about the Django framework](https://www.djangoproject.com/)
***

## Deployment instructions


### 1. Cloning project from GitHub

1.1 Run this command
```commandline
git clone https://github.com/Prrromanssss/CV-backend
```

### 2. Creation and activation venv

2.1 First of all, from root directory run this commands to activate venv
#### Mac OS / Linux
```commandline
python3 -m venv venv
source venv/bin/activate
```
#### Windows
```commandline
python -m venv venv
.\venv\Scripts\activate
```

### 3. Installation all requirements

3.3 Run this command 
```commandline
pip install -r requirements.txt
```

### 4. Generate file with virtual environment variables (.env)

4.1 Generate file '.env' in root directory with such structure
```text
SECRET_KEY=YOUR_SECRET_KEY_123
DEBUG=True
```


### 5. Running project

5.1 Run this command
```commandline
python mysite/manage.py runserver
```

So, we launched our site on the local host, on port 8000 (this port is the default when starting the server)
***
The site is a one-page site that features my photo and my short resume.

The database connection is not presented here; we do not need it for this project. The layout was made using the [bootstrap framework](https://getbootstrap.com/)

