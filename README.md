# LMS

## setup on Linux machine
* Need to install on your system:
    - Python3.6
    - Sqllite3


* Create virtualenv and activate via using given command
    - virtualenv -p python3.6 venv
    - source venv/bin/activate
    
* Install all necessary depandencies
    - pip install -r requirment.txt

* create new database name as "mydb"
* Open taskman/app/app/settings.py file and change db credentials (according to your username/password)

* Apply migrations using given Commands:
    -  python manage.py makemigrations
    -  python manage.py migrate
 
* Run application 
    - python manage.py runserver

* Hit on browser http://localhost:8000
