# django
```
python3 manage.py createsuperuser
```

## Create User

```
>>> python3 manage.py shell
>>> from django.contrib.auth.models import User
>>> usr=User.objects.create_user("testuser", "test@abc.com", "pass123")
>>> usr.is_staff=True
>>> usr.save()
```

## Create a superuser
```
python3 manage.py createsuperuser --username=jhon --email="john@meta.com"
```

## the special variables user and perms are available inside the template language blocks. 

```
<html> 
<body> 
{% if user.is_authenticated %} 
         {#  to be rendeed if the user has been authenticated  #} 
    {% endif %}	 
<body> 
</html>
```

## permissions can be checked inside the template with perms.name syntax. 

```
<html> 
<body> 
{% if perms.myapp.change_category %} 
  {#  To be rendered for users having required permission #} 
   {% endif %} 
<body> 
</html>
```

## Enforcing permissions in URL patterns

```
from django.conf.urls import url 
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [ 
    url(r'^users_only/', login_required(myview)), 

    url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview))
]
```