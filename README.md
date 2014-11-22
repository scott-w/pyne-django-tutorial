Python North East Django Sessions
==================================

Our base for the Python North East Django sessions.

Chatter
-------

For the purposes of the tutorial, we will make a Twitter-like app.
I have already setup the account sign-up, login, and password retrieval screens.
Django builds all of this in for us, so we can just hook up the correct parts,
and know that it's all going to just work.

Getting Started
===============

Assuming we are using OS X or Linux:

```
git clone https://github.com/scott-w/pyne-django-tutorial.git
cd pyne-django-tutorial
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Getting a Django Shell
----------------------

We can access our Django applications using a specific Django shell:

```
python manage.py shell
```
