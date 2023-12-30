### When you create a Django project with the startprojectcommand, certain apps are installed by default. These apps are listed in the INSTALLED_APPS section in the project’s settings.py file.

```
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
] 
```

The first step towards creating the table in the database is to run the ```makemigrations ``` command.
After you need to run the ```migrate`` command to apply the tasks in the migrations file to be performed.

Changing the namefield of the model run ```makemigrations``` again -> ```migrate``` again

 Run the ```showmigrations``` command to show unmigrated changes in the model:
 ```
 myapp
 [X] 0001_initial
 [X] 0002_person
 [ ] 0003_rename_name_person_person_name
 ```

The initial migration (file numbered 0001) has already migrated. The ```X``` mark is indicative of this. 
 After ```migrate``` command, both modifications will be reflected in the table structure.

 The ```sqlmigratecommand``` shows the SQL query or queries executed when a certain migration script is run.
 ```python3 manage.py sqlmigrate myapp 0001_initial```

 ```
 BEGIN;
--
-- Create model Menu
--
CREATE TABLE "myapp_menu" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "cuisine" varchar(100) NOT NULL, "price" integer NOT NULL);
COMMIT;
 ```