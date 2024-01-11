# django

## Install MySQL DB API Driver

```
$ brew install mysql pkg-config
$ pip3 install mysqlclient
```

### Enable MySQL
 ```
 DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'mydatabase',   
        'USER': 'root',   
        'PASSWORD': 'db_pass',   
        'HOST': 'localhost',   
        'PORT': '3306',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
        }   
    }   
} 
 ```

## The other optional parameters include: 

```
**sql_mode:** The session SQL mode will be set to the given string. It defaults to 'STATIC_TRANS_TABLES' to prevent invalid or missing values from being stored in the database.

**default-character-set:** The character set to be used. Default is utf8.

**read_default_file:** MySQL configuration file to read.

**init_command:** Initial command to issue to the server upon connection.
```