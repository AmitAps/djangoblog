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
