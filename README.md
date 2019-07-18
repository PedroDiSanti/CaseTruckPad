[![Coverage Status](https://coveralls.io/repos/github/PedroDiSanti/PythonRestfulAPI/badge.svg?branch=master)](https://coveralls.io/github/PedroDiSanti/PythonRestfulAPI?branch=master)

# Python RESTfulAPI

***

## Technology
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Flask](https://palletsprojects.com/p/flask/)

***

## Configuration

First of all, clone this branch to your machine using the command `https://github.com/PedroDiSanti/PythonRestfulAPI.git`.

Before start the project, you have to check your environment file. You can find it in the main directory.
You'll have to rename the file from `.env.sample` to `.env` and change your configurations.

Here is a example:
```
###> Environment ###
FLASK_ENV=development
###< Environment ###

###> POSTGRESQL ###
POSTGRES_USER=truck
POSTGRES_PASSWORD=truck
POSTGRES_DB=truck
###< POSTGRESQL ###

###> Link to Database ###
DATABASE_URL=postgres://truck:truck@Postgres:5432/truck
DATABASE_URL_TEST=postgres://truck:truck@Postgres:5432/test
###< Link to Database ###
```
The `FLASK_ENV` **MUST** be `development` and the host from the `DATABASE_URL` **MUST** be `Postgres`.

***

## Installing dependecies
After completing the .env, we will be installing the dependecies of the project. Here is the list:

- [Git](https://github.com/) - `sudo apt-get install git`

- [Docker](https://www.docker.com/) - `sudo apt update` AND `sudo apt -y install docker.io`

- [Docker-Compose](https://docs.docker.com/compose/) - `sudo apt -y install docker-compose` and then use this command 
to remove the need to sudo every docker-compose operation `sudo usermod -aG docker $USER`

- [Postman](https://www.getpostman.com/) -  `sudo snap install postman`

***

## How to use

First of all, you will need to be inside the main folder with the `docker-compose-dev.yml` file. Then, you should execute this command: `docker-compose up -d --build`

With this command, you will build the machines necessary for the project.

***

## Running the migrations

First of all, you will need to be inside the docker machine from Flask to execute then, so make this command:`docker exec -it Flask bash`

Then, you can execute this commands:
`python manage.py db init`, `python manage.py db init migrate` and `python manage.py db init upgrade`. With these, your migration should be fine!
***

## Database

The database structure will be created automatically, so you don't need to worry about that.
object
To enter inside the machine to check the status from the data polling, you should execute this command:`docker exec -it Postgres bash`

After you're inside the machine, you must log inside the PostgreSQL terminal, use this command:`psql -U user -d database`

***

## Postman

First of all, go to the postman folder and import the .json found inside the folder `PythonRestfulAPi/postman`. With this done, all the routes should be
create automatically and you can test them.

Also, they already contain a body example. Just check your host and port so it can match!

***

## Testing

To run the test, first enter inside the Postgres's docker, with this command: `docker exec -it Postgres bash`.
After that, execute the command `psql -U (your user here)` enter in your database, create a new database called `test` using the command 
`create database test;` and exit the machine using the command `\q` and then `exit`.

Now, enter in the Flask machine using the command `docker exec -it Flask bash`. After that, just run the command `pytest --cov=src` and the test should starts.

We must do this, since the tests create and destroy the tables from the database and we could lose our data.                  

***

## Removing Docker, if you want (OPTIONAL)
After all tested, you can exit the docker machine using a `exit` command and just destroy the machines and docker would close all connections. Just execute this command:
`docker-compose down`.

After that, let's remove all the trace from docker from your machine. Just execute this commands:
```
dpkg -l | grep -i docker
sudo apt-get purge -y docker-engine docker docker.io docker-ce  
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce 
sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
```
You have removed Docker from the system completely.

***

## Why did I use this tools to build this test?
Well, it was something that I thought about before starting this project.

`Docker` is a must be in all my projects. An excellent tool that I plan to never stop using.

`Postgresql` is my default choice for database and personal favorite over MySQL.

Ok, but why `Flask` and its dependencies? 

In fact, I always programmed `Python` without any Framework. I really wanted to 
try something new and this were a great chance! :^)

After some study, I wanted to try `Flask` out over `Django`, 
because Flask is much simpler and easy to learn, use and adapt. A really good Framework. 

***

Developer: [Pedro Afonso Rotta Di Santi](https://www.linkedin.com/in/pedro-afonso-rotta-di-santi-8842a017b/)
