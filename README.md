# team22_project

Prerequisite software:
* Python 3.8
* django
* psycopg2
* postgresql

Database setup:
Open the postgres sql shell and copy paste the contents of `dbsetup.sql`, this should now enable the project to use a database.
Then in commandline type the following:
(substitute python for python3 on linux/mac os)
```
cd student_board
python manage.py migrate    
python manage.py runserver
```
This will open a server that can be accessed in the links: https://localhost:8000 .