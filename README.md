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

2 - Navigate to the project_safety_zone folder on command prompt and install required packages. You may need to use the full path of requirements.txt

```
pip install -r requirements.txt

```

3 - Create your own "admin_codes.txt" file. This should be in the project_safety_zone directory and is in the same directory as "admin_codes_blank.txt". Alternatively, you can rename "admin_codes_blank.txt" to just "admin_codes.txt" and enter your own information there. You will need your own gmail account. You will also need to setup an application password for it.
Furthermore, you will also need to set which email recieves the notifications.
```
EMAIL_HOST:smtp.gmail.com
EMAIL_HOST_USER:sender@gmail.com
EMAIL_HOST_PASSWORD:yourAppPassword
EMAIL_USE_TLS:True
EMAIL_PORT:587
SECRET_KEY:yourSecretKey
TARGET_EMAIL:reciepient@gmail.com
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

## Usage

1 - Fill in the fields on the form and click submit

2 - The web app will send an email, with the sender being the one specified at EMAIL_HOST_USER and recipient being the TARGET_EMAIL in your admin_codes.txt file

3 - To log in as admin you navigate to /rest-auth/login/. If running on your computer it would be http://127.0.0.1:8000/rest-auth/login/.
