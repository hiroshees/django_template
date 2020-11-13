# django_template

# 設定手順
```
git clone git@github.com:hiroshees/django_template.git PROJECT_NAME
cd PROJECT_NAME
mv .env_origin .env
python manage.py shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# SECRETKEYの作成手順
```
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

# APIKEY
```
admin
APIKEYの設定
```

