Python North East Django Sessions
==================================

Our base for the Python North East Django sessions.

Chatter
-------

For the purposes of the tutorial, we will make a Twitter-like app.
Django has built-in account creation and authentication, meaning we just need
to wire it all up.

Requirements
------------

Before getting started, you need to have the following:

* Python 2.7
* Git
* Pip
* Virtualenv
* A text editor e.g. Atom, Sublime Text

### Installing Python

Python is already installed on OS X and Ubuntu. To get pip and virtualenv,
either use your package manager:

```
sudo apt-get install python-pip
```

Or use easy install:

```
sudo easy_install pip
```

Then you can use pip to install virtualenv:

```
sudo pip install virtualenv
```

### Installing Git

In Linux, use your package manager e.g.

```
sudo apt-get install git
```

Git comes installed by default in OS X Yosemite. You can install a graphical
git client from Github (https://github.com).

### Text editors

* Atom (https://atom.io)
* Sublime Text (http://www.sublimetext.com/)

### Windows

To install python, pip and django, follow the instructions at https://docs.djangoproject.com/en/1.7/howto/windows/.
Python 3.4 comes packaged with pip and virtualenv so you shouldn't actually have to install either, just make sure that they are on PATH.
Install git from http://git-scm.com/download/win.

Another possibility is to use chocolatey (https://chocolatey.org/) which is a package manager for Windows.
Follow the installation instructions then run:
```
cinst python pip git
```
Note that you might have to restart the shell to pick up the newly installed binaries. It has also has a fairly good selection of editors (emac, vim, sublime-text, atom) and other things such as postgres.


Using this Tutorial
-------------------

This tutorial makes heavy use of git to navigate through the code. I will
reference tags throughout the tutorial that will let you skip ahead in the
tutorial.
To get to section 01 of the tutorial, run:

```
git checkout 01
```

If you're writing code as you go, you'll probably want to save it. With a
couple of exceptions, you can keep writing code.

If you want to keep your code saved before moving to a tag, you simply commit
it:

```
git add -A
git commit -m "Enter a reminder to yourself here"
```

Then run the `git checkout` command described.

Getting Started
===============

Let's get the repository downloaded and set up:

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

Enable our App
--------------

Django starts by creating a base settings file. Open
`chatter/chatter/settings.py`, find line 46 and remove the leading `#` so it
looks as so:

```python
INSTALLED_APPS = (
  ...
  'chatter.base',
  ...
)
```

This will allow Django to see the new app when running commands.

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
  created = models.DateTimeField(auto_now_add=True)
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

Skipping to the Code
--------------------

To continue the tutorial, skip ahead to tag `02`:

```
git checkout 02
```

Create Some Chats
=================

Using the admin console, create a few Chat messages.
Go to `http://localhost:8000/admin/` and click on "Add" next to "Chats".

From here, you can select the user to Chat from and the content.


Creating a Website
==================

In this part, we will start displaying the chat records we've been creating!

Start by getting the Bootstrap CSS:

```
git checkout 03
```

Templates
---------

A template is used to create the HTML that is interpreted by your browser.
Create a file called `templates/base/chat_list.html`:

```html
{% extends "base/base.html" %}

{% block content %}
<ul>
{% for chat in object_list %}
<li>{{ chat.content }}</li>
{% endfor %}
</ul>
{% endblock content %}
```

Views
-----

We now need to create a view. A view is the meat of our code connecting records
in the database to the HMTL displayed on the page. In `chatter/base/views.py`:

```python
from django.views.generic import ListView

from chatter.base.models import Chat


class ChatListView(ListView):
  """List all chats in the system.
  """
  model = Chat
```

And that's all you need! If you're curious, Django views take a number of
configuration options, but uses some reasonable pre-set defaults. With this, we
can just put our template in the right place, and it will "just work".

For those who want to see the underlying code, [CCBV](http://ccbv.co.uk) is a
great source with an excellent breakdown of each view, and how it works.

Routing
-------

Now all we need to do is tell Django what URL your view is attached to. Start
by putting the following line in `chatter/urls.py`:

```python
url(r'^admin/', include(admin.site.urls)),

# Insert the following line
url(r'', include('chatter.base.urls')),
```

Then create a file `chatter/base/urls.py`:

```python
from django.conf.urls import patterns, url

from chatter.base.views import ChatListView


urlpatterns = patterns(
'',
url(r'^$', ChatListView.as_view()),
)
```

Now, when you go to `http://localhost:8000` you will get the chats you just
created!

Improved HTML
-------------

Let's make our app a little better. Use the HTML below and do the following:
* Insert the user who made the chat in the `panel-title`
* Insert the chat body into the `panel-body`
* Insert the time of the chat into the `panel-footer`
* Loop through all the chats with a panel for each, as before

```html
{% extends "base/base.html" %}

{% block content %}
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title"></h3>
  </div>
  <div class="panel-body">
  </div>
  <div class="panel-footer">
  </div>
</div>
{% endblock content %}
```

Filter by User
==============
As our number of Chats grows, it'll become impossible to see what people have
to say! Let's view individual Chats by user. Start by moving to the latest tag:

```
git checkout 04
```

Things start to get a little more interesting now. We can start to examine the
request and act on different data. Let's start with our urls.py:
