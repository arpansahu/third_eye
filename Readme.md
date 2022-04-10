
# Third Eye Project

This project is with Django. The purpose of building this project is, a large population hesitate to visit doctors at first.
So they try some home remedies first and then when they give up in home remedies, and they are still suffering from the same disease
they visit doctors. This project is build to help them determine which is the most probable disease they would be suffering from.
This is not recommended since Machine LEarning model is training on limited data collected by MIT. Only 53 symptoms are accounted in
data. Moreover, Model is trained with 97.0 accuracy. But in Filed of Medical ever 0.1 accuracy is important. It can be improved with other
Machine LEarning Models. After getting the prediction users can also locate nearby medical facilities for India. Since I have saved only 
Indian Medical Facilities in my database. Although you can add your area hospitals too.


-Implemented A simple Web App using Naive Bayes Machine Learning algorithm.
    
1. Used built in Django Auth Model
2. Built three views, function based
3. Used Naive Machine Learning Algorithm for model training and prediction
4. Collected data from MIT Website is used for model training
5. Trained model was pickled and then used in django views for prediction
6. Google MAps API and MindMax Database used for user location identification and show them nearby hospital facilities
7. Hospitals data is collected from indian gov website.


-Deployed on Heroku

~~1. Used Heroku Postgres 
2. Used AWS S3 Bucket for static and media files~~
## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)
[![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)](https://graphql.org/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Demo

Available at: https://django-project-api-crud-graphq.herokuapp.com/

admin login details:--
username: arpansahu
password: showmecode
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installing Pre requisites

```bash
  pip install -r requirements.txt

```

Making Migrations and Migrating them.

```bash
  python manage.py makemigrations
  python manage.py migrate

```

Creating Super User

```bash
  python manage.py createsuperuser

```

Updating Hospital and Symptoms Data

```bash
  python manage.py update_hospitals_data
  python manage.py update_symptoms_data
```

Run Server
```bash
  python manage.py runserver
```

## Tech Stack

**Client:** HTML, Jinja, CSS, BootStrap, Jquery

**Server:** Django, Django Rest Framework, Gunicorn, GraphQL, Heroku


## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  add all the env variables used from app setting page on heroku app dashboard.

```
Configuring Django App for Heroku
```
    install whitenoise : pip install whitenoise 
    include it in included_apps=[]
    add whitenoise middleware
    add: procfile
    add: release-task.sh for running mutilple commands in run: section of procfile
    make relase-task.sh executable : chmod +x release-tasks.sh 
```
## Documentation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)
[![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)](https://graphql.org/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

SECRET_KEY=

DEBUG=

DB_HOST=

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_PORT=

EMAIL_USER=

EMAIL_PASS=

ALLOWED_HOSTS=

