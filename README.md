# django-sosmed-site
Membuat aplikasi sosmed menggunakan Django v3.2.2


## 1. DJANGO RROJECT DAN APP


#### 1.1 DJANGO RROJECT DAN APP - Membuat virtual environmenet dan install django

        modified:   .gitignore
        modified:   README.md
        new file:   requirements.txt


#### 1.2 DJANGO RROJECT DAN APP - Membuat djang proyek 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        

#### 1.3 DJANGO RROJECT DAN APP - Membuat django app 'app/post'

        new file:   app/post/__init__.py
        new file:   app/post/admin.py
        new file:   app/post/apps.py
        new file:   app/post/migrations/__init__.py
        new file:   app/post/models.py
        new file:   app/post/tests.py
        new file:   app/post/views.py
        

#### 1.4 DJANGO RROJECT DAN APP - Register app post pada settings.py

        modified:   README.md
        modified:   app/post/apps.py
        modified:   config/settings.py


## 2. TEMPLATES, VIEWS AND URLS


#### 2.1 TEMPLATES, VIEWS AND URLS - Membuat laman home

        modified:   README.md
        new file:   templates/app/post/index.html


#### 2.2 TEMPLATES, VIEWS AND URLS - Membuat home view

        modified:   README.md
        modified:   app/post/views.py


#### 2.3 TEMPLATES, VIEWS AND URLS - Membuat path

        modified:   README.md
        new file:   app/post/urls.py
        modified:   config/urls.py