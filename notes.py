"""
Any Python libraries you install while your virtual environment is active will go into the my_env/lib/python3.8/site-packages directory.
"""

#to know django version
"""
(blog_env) [Aps@aps djangoblog]$ python
Python 3.8.5 (default, Aug 12 2020, 00:00:00)
[GCC 10.2.1 20200723 (Red Hat 10.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'3.1.1'
>>>

"""

"""
You can run the Django development server on a custom host and port or tell
Django to load a specific settings file, as follows:
python manage.py runserver 127.0.0.1:8001 \--settings=mysite.settings
"""

"""
Django with different web servers at
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/ .
"""

"""
You can see all the settings and their default values
at https://docs.djangoproject.com/en/3.0/ref/settings/ .
"""

"""
Let's take a look at the SQL code that Django will execute in the database to create
the table for your model. The sqlmigrate command takes the migration names and
returns their SQL without executing it. Run the following command to inspect the
SQL output of your first migration:
python manage.py sqlmigrate blog 0001
"""

"""
Django creates a primary key automatically for each model, but you can also
override this by specifying primary_key=True in one of your model fields.
"""

"""
Username (leave blank to use 'aps'): Aps
Email address: admin@thesocialtalks.com

"""

"""

Adding models to the administration site
Let's add your blog models to the administration site. Edit the admin.py file of the
blog application and make it look like this:


from django.contrib import admin
from .models import Post
admin.site.register(Post)
"""
"""
Customizing the way that models are
displayed
Now, we will take a look at how to customize the administration site. Edit the
admin.py file of your blog application and change it, as follows:
from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
list_display = ('title', 'slug', 'author', 'publish', 'status')
"""

"""
The Django ORM is based on QuerySets. A QuerySet is a collection of database
queries to retrieve objects from your database. You can apply filters to QuerySets
to narrow down the query results based on given parameters.
"""

#Creating objects
"""
blog_env) [Aps@aps mysite]$ ./manage.py shell
Python 3.8.5 (default, Aug 12 2020, 00:00:00)
[GCC 10.2.1 20200723 (Red Hat 10.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='Aps')
>>> user
<User: Aps>
>>> post = Post(title='Another post', slug='another-post',
...             body='Post body.', author=user)
>>> post.save()
>>> posts = Post.objects.all()
>>> posts
<QuerySet [<Post: Another post>, <Post: Thesocialtalks>]>
>>>

"""
#The preceding action performs an INSERT SQL statement behind the scenes.

#The get() method allows you to retrieve a single object from the database.

"""
you can also create the object and persist it into the database in a
single operation using the create() method.
"""
(blog_env) [Aps@aps mysite]$ ./manage.py shell
Python 3.8.5 (default, Aug 12 2020, 00:00:00)
[GCC 10.2.1 20200723 (Red Hat 10.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='Aps')
>>> user
<User: Aps>
>>> Post.objects.create(title='One more post',
...                     slug='one-more-post', body='Post body',
...                     author=user)
<Post: One more post>
>>> post = Post.objects.get(title='One more post')
>>> post
<Post: One more post>
#update
>>> post.title = 'New title'
>>> post.save()



##########################################################*************************************

Each Django model has at least one manager, and the default manager is called objects . You get a
QuerySet object using your model manager. To retrieve all objects from a table,
you just use the all() method on the default objects manager, like this:
>>> all_posts = Post.objects.all()
############################################################


###########################################################

Using the filter() method
To filter a QuerySet, you can use the filter() method of the manager. For example,
you can retrieve all posts published in the year 2020 using the following QuerySet:
>>> Post.objects.filter(publish__year=2020)
You can also filter by multiple fields. For example, you can retrieve all posts
published in 2020 by the author with the username admin :
>>> Post.objects.filter(publish__year=2020, author__username='admin')

This equates to building the same QuerySet chaining multiple filters:
>>> Post.objects.filter(publish__year=2020) \
>>>
.filter(author__username='admin')

#############################################################


###########################################################

Using exclude()
You can exclude certain results from your QuerySet using the exclude() method
of the manager. For example, you can retrieve all posts published in 2020 whose
titles don't start with Why :
>>> Post.objects.filter(publish__year=2020) \
>>>
.exclude(title__startswith='Why')
#############################################################

Using order_by()
You can order results by different fields using the order_by() method of the
manager. For example, you can retrieve all objects ordered by their title , as follows:
>>> Post.objects.order_by('title')
Ascending order is implied. You can indicate descending order with a negative sign
prefix, like this:
>>> Post.objects.order_by('-title')
###########################################################


Deleting objects
If you want to delete an object, you can do it from the object instance using the
delete() method:
>>> post = Post.objects.get(id=1)
>>> post.delete()

Note that deleting objects will also delete any dependent relationships for ForeignKey objects defined with on_delete set
to CASCADE.
###########################################################**********************************


"""
Creating model managers

You will create a custom manager to retrieve all posts with the
published status.
"""

###########################################################


There are two ways to add or customize managers for your models: you can
add extra manager methods to an existing manager, or create a new manager by
modifying the initial QuerySet that the manager returns. The first method provides
you with a QuerySet API such as Post.objects.my_manager() , and the latter
provides you with Post.my_manager.all() . The manager will allow you to
retrieve posts using Post.published.all() .


The first manager declared in a model becomes the default manager. You can use
the Meta attribute default_manager_name to specify a different default manager.
If no manager is defined in the model, Django automatically creates the objects
default manager for it. If you declare any managers for your model but you want
to keep the objects manager as well, you have to add it explicitly to your model.

---> refer modes.py
objects = models.Manager() # The default manager.
published = PublishedManager() # Our custom manager.


The get_queryset() method of a manager returns the QuerySet that will be
executed. You override this method to include your custom filter in the final
QuerySet.
You have now defined your custom manager and added it to the Post model; you
can use it to perform queries. Let's test it.

(blog_env) [Aps@aps mysite]$ ./manage.py shell
Python 3.8.5 (default, Aug 12 2020, 00:00:00)
[GCC 10.2.1 20200723 (Red Hat 10.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> Post.published.filter(title__startswith='who')
<QuerySet [<Post: who is the best>]>
>>> post = Post.published.filter(title__startswith='who')
>>> post
<QuerySet [<Post: who is the best>]>

To obtain results for this QuerySet, make sure that you set the published field to
True in the Post object whose title starts with Who .
###################################################################################

You can
learn more about defining URL patterns with regular expressions at https://docs.
djangoproject.com/en/3.0/ref/urls/#django.urls.re_path . If you haven't
worked with regular expressions before, you might want to take a look at the
Regular Expression HOWTO located at https://docs.python.org/3/howto/regex.
html first.

###################################################################################
reverse() method, which allows you to build URLs by their name and pass
optional parameters. You can learn more about the URLs utility functions at
https://docs.djangoproject.com/en/3.0/ref/urlresolvers/ .
###################################################################################
CREATING TEMPLATES

You can find more information
about the Django template language at https://docs.djangoproject.com/en/3.0/ref/templates/language/ .

###############################################################################################################


Django has a powerful template language that allows you to specify how data is
displayed. It is based on template tags, template variables, and template filters:
• Template tags control the rendering of the template and look like {% tag %}
• Template variables get replaced with values when the template is rendered
and look like {{ variable }}
• Template filters allow you to modify variables for display and look like {{
variable |filter }} .
You can see all built-in template tags and filters at https://docs.djangoproject.com/en/3.0/ref/templates/builtins/ .

####################################################################################
{% load static %} tells Django to load the static template tags that are provided
by the django.contrib.staticfiles application, which is contained in the
INSTALLED_APPS setting


####################################################################################

You can take a look at an introduction to class-based views at https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/ .
###################################################################################

Django comes with two base classes to build forms:
• Form : Allows you to build standard forms
• ModelForm : Allows you to build forms tied to model instances
####################################################################################
If you can't use an SMTP server, you can tell Django to write emails to the console
by adding the following setting to the settings.py file:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
By using this setting, Django will output all emails to the shell. This is very useful
for testing your application without an SMTP server.

######################################################################################

If you want to send emails but you don't have a local SMTP server, you can
probably use the SMTP server of your email service provider. The following sample
configuration is valid for sending emails via Gmail servers using a Google account:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
####################################################################################
Run the python manage.py shell command to open the Python shell and send
an email, as follows:
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'This e-mail was sent with Django.', 'your_
account@gmail.com', ['your_account@gmail.com'], fail_silently=False)

send_mail('Django mail', 'This e-mail was sent with django.', 'flyhieeofficial@gmail.com', ['amitoct9@gmail.com'], fail_silently=False)

####################################################################################
If you are sending emails using Gmail with the preceding configuration, you will
have to enable access for less secure applications at https://myaccount.google.com/lesssecureapps
####################################################################################
The related_name attribute allows you to name the attribute that you use for
the relationship from the related object back to this one. After defining this, you
can retrieve the post of a comment object using comment.post and retrieve all
comments of a post using post.comments.all() . If you don't define the related_
name attribute, Django will use the name of the model in lowercase, followed by _
set (that is, comment_set ) to name the relationship of the related object to the object
of the model, where this relationship has been defined.

You can learn more about many-to-one relationships at https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/ .
####################################################################################
you can
explicitly tell the framework which fields you want to include in your form using
a fields list, or define which fields you want to exclude using an exclude list of
fields.
#####################################################################################
The save() method is available for ModelForm but not
for Form instances, since they are not linked to any model.
#####################################################################################

You are using the Django ORM in the template, executing the QuerySet comments.
count() . Note that the Django template language doesn't use parentheses for calling
methods. The {% with %} tag allows you to assign a value to a new variable that
will be available to be used until the {% endwith %} tag.


The {% with %} template tag is useful for avoiding hitting the
database or accessing expensive methods multiple times.

######################################################################################
 [Aps@aps mysite]$ ./manage.py shell
Python 3.8.5 (default, Aug 12 2020, 00:00:00)
[GCC 10.2.1 20200723 (Red Hat 10.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> post = Post.objects.get(id=1)
>>> post.tags.add('music','jazz','django')
>>> post.tags.all()
<QuerySet [<Tag: django>, <Tag: jazz>, <Tag: music>]>
>>> post.tags.remove('django')
>>> post.tags.all()
<QuerySet [<Tag: jazz>, <Tag: music>]>
######################################################################################
You can discover more about many-to-many relationships at https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/ .

###############################################################################################
You can learn about aggregation at https://docs.djangoproject.com/en/3.0/topics/db/aggregation/ .
##############################################################################################
