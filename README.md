# Safety Zone

## Table of Contents

* [Description](#description)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)


## Description

**THIS APP IS INCOMPLETE**

This application allows users to create and view flight safety notifications.
After the user submits the report, the application generates an email with the information and sends it to the proper recipient for further investigation.

## Technologies Used

* Python (Django - Rest Framework)
* HTML5 (Bootstrap)
* Javascript

## Installation


1 - Clone the repo

2 - Navigate to the project_safety_zone folder on command prompt and install required packages.  This installation was only tested in virtual Python environment using Anaconda. It is possible that there are other dependancies not covered in requirements.txt, but come pre-loaded when creating a virtual python environment with anacoda. If that is the case and you are not using anacoda, you will have to install these additional dependancies manually

```
cd project_safety_zone
pip install -r requirements.txt

```

You may need to use the absolute path of requirements.txt instead of the relative file path. For example, it can look like this

```
pip install -r C:\Users\UserName\Documents\Web_App_Safety_Zone\project_safety_zone\requirements.txt

```


3 - Create your own "admin_codes.txt" file. This should be in the project_safety_zone directory and is in the same directory as "admin_codes_blank.txt". Alternatively, you can rename "admin_codes_blank.txt" to just "admin_codes.txt" and enter your own information there. You will need your own gmail account. You will also need to setup an application password for it.
Furthermore, you will also need to set which email recieves the notifications.

```
EMAIL_HOST:smtp.gmail.com
EMAIL_HOST_USER:sender@gmail.com
EMAIL_HOST_PASSWORD:yourAppPassword
EMAIL_USE_TLS:True
EMAIL_PORT:587
SECRET_KEY:y5u*&jy+&xuxlqu30139=pogcl70-j9s_=lx=n!sl5*umkojv!
TARGET_EMAIL:reciepient@gmail.com
```

A SECRET_KEY has been provided as placeholder on admin_codes_blank. This is fine for development but for production, but it is highly reccomended to make your own for production. To make your own, you can just make another django project with django-admin startproject GenericProject, go its settings.py file and use that new SECRET_KEY.

```
django-admin startproject GenericProject

```

4 - Make migrations

```
python manage.py makemigrations
python manage.py migrate
```


5 - Create super user

```
python manage.py createsuperuser
```

6 - To start the web app, open command prompt and navigate to project_safety_zone and run python manage.py runserver.
```
cd project_safety_zone
python manage.py runserver
```

## Usage

1 - Fill in the fields on the form and click submit

2 - The web app will send an email, with the sender being the one specified at EMAIL_HOST_USER and recipient being the TARGET_EMAIL in your admin_codes.txt file

3 - To log in as admin you navigate to /rest-auth/login/. If running on your computer it would be http://127.0.0.1:8000/rest-auth/login/.
