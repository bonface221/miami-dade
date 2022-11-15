## A django app
## Miami-dade
An application where it can:
* User Authentication
* scrapping




## Getting Started

*   Set up a virtual environment in the project folder
```
$ pipenv shell
```

### Prerequisites

*get pipenv

```
Debian- sudo apt install pipenv
```
```
Windows- pip install --user pipenv
```

### Locate python interpreter

```
$ pipenv --py
```

/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python



*get all requirements in the Pipfile.lock

```
$ pipenv install
```

### Installing


Now run the following command

```
python3.9 manage.py runserver
```

And view the site at the port provided which is most likely 127.0.0.1:8000


## using pipienv 
 I was using Postgress you can use any sql backend of your choice
 try using Sqlite3 database...
Doesn't need reconfiguring ......... I have already configured ....it can work though sqlite is a lightweight database not to be used in production

### If using macbook use this command to install pipenv 
```
$ pip install --user pipenv
```
### use pipenv to re install dependancies ..... 
```
$ pipenv install
```
### That's all also remmember to use the scrapper to populate the database and make sure the server is running..... 
``` 
python manage.py runserver
```
### the scrapper is using virtual env so it is a matter of re-installing from the requirements .txt file ....its using pip ....
 so run this command 
 ```
 $pip install -r requirements.txt
 ```
### Run the spiders using 
``` $spider crawl miami 
``` 
and the next one is 
```
spider crawl advanced
```
 .. miami and advanced are names of spiders.....
##### Goodluck

## Running the tests

To run the automated tests for this system, run the following command

```
python3.9.12 manage.py test base

```
## Built With

* Python Programming Language
* Django Web Framework
* Scrappy

## Versioning

Find all the versions used in the pipfile
