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

Recap
=====

Let's quickly recap on our first session:
  1. We set up our app
  2. We configured database models
  3. We created a screen listing our data and wired it up
  4. We played with templates


Filter by User
==============
As our number of Chats grows, it'll become impossible to see what people have
to say! Let's view individual Chats by user. Start by moving to the latest tag:

```
git checkout 04
```

Things start to get a little more interesting now. We can start to examine the
request and act on different data. Let's start by modifying
`chatter/base/urls.py`:

```python
from django.conf.urls import patterns, url

from chatter.base.views import ChatListView, UserChatListView


urlpatterns = patterns(
    '',
    url(r'^$', ChatListView.as_view(), name='index'),
    url(r'^@(?P<username>.+)/$', UserChatListView, name='chat-user')
)
```

The `\+` is just some custom syntax that we'll use to differentiate users from
other types of links. We need to escape the `+` to stop the regex from
recognising it. We've also named our `username` argument for the sake of our
views later.

A quick aside, for those who don't know regex syntax, the most common patterns
you'll see in URLs are:
* `.+` Any character 1 or more times
* `\d+` Any digit (0-9) 1 or more times
* `\w+` Any letter (a-z, A-Z) 1 or more times

You'll see we've also named the URLs above. You'll see why shortly.

The View
--------

This is where we get interesting. We'll have to start customising Django's
built-in views!

Our standard `ListView` lets us override a method called `get_queryset` to
simplify our filtering. Let's give it a go in `chatter/base/views.py`:

```python
class UserChatListView(ListView):
    """List all chats filtered by username.
    """
    model = Chat
    template_name = 'base/chat_list.html'

    def get_queryset(self):
        """Use the view kwargs to get a list of Chats by user.
        """
        return self.model.objects.filter(
                user__username=self.kwargs['username'])
```

The first thing to note is that we have to explicitly add `template_name` as
we want to reuse our existing template.

Onto the `get_queryset` method, we can see the reference to `self.model`. It's
possible to go without `model = Chat` here, but I prefer to do it this way.

The `filter` syntax is also worth a look. You should recall our `Chat` in
`models.py` references a `user`. We then tell Django to look inside the
`contrib.User` model for the `username` field using the `__` syntax. You will
see this referenced through Django's documentation.

Linking to the View
-------------------

Now it's all in place, we need to figure out how to link to it. Let's jump into
the `chatter/templates/base/chat_list.html` template at the `panel-heading`
class:

```html
<div class="panel-heading">
  <h3 class="panel-title">
    <a href="{% url "chat-user" username=chat.user.username %}">
      @{{ chat.user }}
    </a>
  </h3>
</div>
```

We have introduced a template tag. Template tags are identified with
`{% function  "args" kwarg=value %}` and let us execute Python code in our
templates in a structured way.

Have a Look
-----------

You may want to create more users and Chats from the admin console, then you'll
be free to click on any name to see just that user's Chats!

Ordering
--------

You've probably noticed out Chats aren't displaying the newest first. Let's
fix that by opening `chatter/base/models.py`:

```python
class Chat(models.Model):
    """A single chat from a User.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = '-created',
```

**Note the comma!** The value of `ordering` must be a list or tuple. The
leading `-` tells Django to reverse the order.

This sets a default which we can override in views like so:

```python
Chat.objects.filter(
  user__username=some_value).order_by(
  'user__username')
```


Authentication
==============

Firstly, let's update to the latest tag:

```
git checkout 06
```

This gives us an outline login template, with our URLs wired up. Let's take a
quick look at our `chatter/urls.py`:

```python
urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', name='login'),
)
```  

A quick explanation here. The first argument to `patterns` is the base import
path. That means our second argument to `url()` gets joined to that path to
become `django.contrib.auth.views.login` and is imported by Django.

Before we can use it, let's tell Django where to go once we log in. Open
`settings.py` and add the following at the bottom:

```python
LOGIN_REDIRECT_URL = '/'
```

For the default `login` view to work, we also need
`templates/registration/login.html`, so open it up and have a look.

This is just a standard HTML form, with some tags that come from the login
view's default form class.

If we wanted to, we could replace the `<input>` tags with `{{ form.fieldname }}`
to have Django generate the HTML tags for us.

Let's customise the login button so it displays the logged-in user's name. Open
`templates/base/base.html` and look for:

```html
<a class="pull-right btn btn-success" href="{% url "login" %}">
  Login
</a>
```

The request object contains the currently logged-in user, with an
`is_authenticated` method. Use this, with the `{% if %}` `{% else %}` and
`{% endif %}` tags, to insert the following information if the user is logged
in, otherwise display the login button. To help you, here's some HTML:

```html
<span class="pull-right small">{{ view.request.user.username }}</span>
```

User Input
==========

Finally, we have want to handle some user input. We will use a Django Form to
take and validate the input for the user. Let's create a file `forms.py`:

```python
from django import forms

from chatter.base.models import Chat


class ChatForm(forms.ModelForm):
    """
    """
    class Meta:
        exclude = 'user', 'created'
        model = Chat
```

Let's break this down.
  1. We're using a `ModelForm` which hooks our form handler to the database
  2. We tell the form not to look at the `user` or `created` fields
  3. We point it to the `Chat` model

The `ModelForm` will automatically take the fields from the attached model and
translate them to our templates and back into the database.

Let's create a new view:

```python
class ChatCreateView(CreateView):
    """Create a new Chat and attach it to the logged in user.
    """
    model = Chat
    form_class = ChatForm
```
