#!/bin/sh

if [ "$1" == "server" ]
then
    python manage.py runserver "$2"
elif [ "$1" == "migration" ]
then
    python manage.py makemigrations cralwer
    wait
    python manage.py migrate
elif [ "$1" == "up" ]
then
    docker-compose up -d
elif [ "$1" == "down" ]
then
    docker-compose down -v
else
    echo "no command found"
fi