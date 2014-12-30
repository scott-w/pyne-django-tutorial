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

Running the Testserver
----------------------

We can run the test web server:

```
python manage.py runserver
```

Then, in a web browser, go to `http://localhost:8000`

Tutorial
========

Let's get started using Django!

Create an Admin User
------

We'll start by creating our database and setting up an administrator:

```
cd pyne-django-tutorial
git checkout 01
. venv/bin/activate

# Create the database and don't ask for input
./manage.py migrate --noinput

# Enter our shell
./manage.my shell
```

Once we're in our shell we can create an administrator:

```python
from django.contrib.auth.models import User

User.objects.create_superuser(
  username='admin',
  email='admin@example.com',
  password='password',
)
```

Create our models
-----------------

Now that we have an administrator, we can login to the admin panel. With a
running server, navigate to `http://localhost:8000/admin/`. However, there's
not a lot we can do without any custom data models, so let's create some! Open
`chatter/chatter/base/models.py` and enter the following:

```python
from django.conf import settings
from django.db import models


# Create your models here.
class Chat(models.Model):
  """A single chat from a User.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  content = models.CharField(max_length=200)
  created = models.DateTimeField(auto_add_now=True)
```

Now we need to create these models in the database:

```
./manage.py makemigrations
./manage.py migrate
```

Register with the Admin Site
----------------------------

Now we just need to register the new model with the Django admin site. Open up
`chatter/chatter/base/admin.py` and enter the following:

```python
from django.contrib import admin

from .models import Chat


# Register your models here.
admin.site.register(Chat)
```

Now when we navigate to `http://localhost:8000/admin/` we can see our Chat
model. Now we can list, create and amend these records from the administrator
backend.
