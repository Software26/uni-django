#https://docs.djangoproject.com/en/3.0/ref/models/fields/
#https://docs.djangoproject.com/en/3.0/howto/custom-model-fields/

#Antes de empezar la leccion borrar el archivo sqlite3 para ahora trabajar con postregresql 

#instalar postgresql:
python -m pip install psycopg2

#crea base de datos django_db en pgadmin, sin nada mas

#configurar postregresql en archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'postgres',
        'PASSWORD': 'contrasena agregada en la bd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
-------------------------------------------------------------------------------------------------------

despues de agregar todo la coneccion a la base de datos 
debemos deber al subir el servidor pide algunas migraciones 

para ver las migraciones sessions

|----installar extenxion------------|
|--python -m pip install psycopg2 --|
|-----------------------------------|



|-----------------------------------------------------------------------------
|----migracion pendiente------------|
|--python manage.py showmigrations--|
|-----------------------------------|

admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
webapp
|-----------------------------------------------------------------------------------------------------

|----Subir las migracione------------|
|--python manage.py showmigrations--|
|-----------------------------------|

----crear app--- 

comando
|--------------crear otra aplicacion
python manage.py startapp persona