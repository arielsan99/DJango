Django version 3.0.3
desde la ubicacion de manage.py ejecutar => python manage.py runserver 8080

O su preferencia de puerto

---------------------------------------------------------------------------

Pasos para crear un proyecto:

1. Crear el proyecto con el comando => django-admin startproject nombre, y ejecutarlo con => python manage.py runserver 8080
2. Crear los archivos y directorios minimos para trabajar con django (carpeta model, carpeta templates, carpeta static, archivo views.py)
3. Configurar en el archivo settings.py la ubicacion de nuestros templates
4. Crear un template basico index.html y asociar los archivos estaticos (no olvidar configurar el la direccion en el archivo settings.py)
4. Crear en el archivo views.py una nueva vista y renderizar un template 
5. Crear en el archivo urls.py una nueva direccion asociada a una vista