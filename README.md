# django
## Create a user
 ```
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('testuser', 'test@abc.com', 'pass123')
```
## Create stuff user
```
>>>usr.is_staff=True
>>>usr.save()
```
## Create a superuser
```
python manage.py createsuperuser --username=john --email=john@mail.com
```
