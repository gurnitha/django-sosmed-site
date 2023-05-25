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


#### 2.4 TEMPLATES, VIEWS AND URLS - Mengaktifkan django templates dan display 'hello world'

        modified:   README.md
        modified:   config/settings.py


#### 2.5 TEMPLATES, VIEWS AND URLS - Mengisi html template pada laman home

        modified:   README.md
        new file:   templates/app/post/index.html


## 3. STATIC DAN MEDIA FILES


#### 3.1 STATIC DAN MEDIA FILES - Membuat static files

        modified:   .gitignore << -- static files created, but git ignoring static
        modified:   README.md


#### 3.2 STATIC DAN MEDIA FILES - Membuat path untuk static dan media files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py


#### 3.3 STATIC DAN MEDIA FILES - Loading static files

        modified:   README.md
        modified:   config/settings.py << -- fixing static files path
        modified:   templates/app/post/index.html

        NOTE:

        Successfully load static files to home page :)


#### 3.4 STATIC DAN MEDIA FILES - Memodifikasi README.md files


## 4. BASE TEMPLATE AND TEMPLATE INHERITANCE


#### 4.1 BASE TEMPLATE AND TEMPLATE INHERITANCE - Laman home

        modified:   README.md
        new file:   templates/app/components/modals.html
        new file:   templates/app/components/navbar.html
        modified:   templates/app/post/index.html
        new file:   templates/base.html

        :)


#### 4.2 BASE TEMPLATE AND TEMPLATE INHERITANCE - Membuat laman about

        modified:   README.md
        modified:   app/post/urls.py
        modified:   app/post/views.py
        new file:   templates/app/post/about.html


#### 4.3 BASE TEMPLATE AND TEMPLATE INHERITANCE - Mentautkan laman home dan about

        modified:   README.md
        modified:   templates/app/components/navbar.html


#### 4.4 BASE TEMPLATE AND TEMPLATE INHERITANCE - Membuat laman account

        modified:   README.md
        modified:   app/post/urls.py << --- create new path
        modified:   app/post/views.py << --- create account_page view
        modified:   templates/app/components/navbar.html << --- add link
        new file:   templates/app/post/account.html << --- create new page
        modified:   templates/app/post/index.html << --- add link

        :)


## 5. AUTHENTICATION & AUTORIZATION


#### 5.1 AUTHENTICATION & AUTORIZATION - Create a new app called 'app/users'

        modified:   README.md
        new file:   app/users/__init__.py
        new file:   app/users/admin.py
        new file:   app/users/apps.py
        new file:   app/users/migrations/__init__.py
        new file:   app/users/models.py
        new file:   app/users/tests.py
        new file:   app/users/views.py


#### 5.2 AUTHENTICATION & AUTORIZATION - Register users app to settings.py

        modified:   README.md
        modified:   app/users/apps.py
        modified:   config/settings.py


#### 5.3 AUTHENTICATION & AUTORIZATION - Mengaktifkan django admin dan membuat superuser dan user

        modified:   README.md

        NOTE:

        1. Create and apply migratoions
        2. Create superuser and a test user


#### 5.4 AUTHENTICATION & AUTORIZATION - Membuat laman register

        modified:   README.md
        new file:   templates/app/users/register.html


#### 5.5 AUTHENTICATION & AUTORIZATION - Membuat register_page view

        modified:   README.md
        modified:   app/users/views.py


#### 5.6 AUTHENTICATION & AUTORIZATION - Membuat path

        new file:   app/users/urls.py
        modified:   config/urls.py


#### 5.7 AUTHENTICATION & AUTORIZATION - Rendering instance of the RegisterUserForm pada laman register

        modified:   README.md
        modified:   app/users/views.py
        modified:   templates/app/users/register.html

        NOTE:

        1. Successfully render instances of the RegisterUserForm to register page.
        2. But this form could not be used to register a new user.