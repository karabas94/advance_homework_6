##  First django project

--------
* Done:
  * created project
  * created catalog app
  * catalog app added to INSTALLED_APPS
  * created models Provider, City, Client, Product
  * created graph model
  ![my_project.png](my_project.png)
  * created requests for SQL!
--------
_Project used django, sqlparse and asgiref library_


**How to start project**
* install all from requirements.txt
* for start project write in terminal:
```
    
    $ python manage.py runserver
    
```
* for migration run:
```
    
    $ python manage.py migrate
    
```
* for create graph model:
```
    
    ./manage.py graph_models -a -I Provider, City, Product, Client -o my_project.png
    
```
--------
Project checked by flake8
