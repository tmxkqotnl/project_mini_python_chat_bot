#!/bin/sh

if [ "$1" == "server" ]
then
    python manage.py runserver 8080
elif [ "$1" == "migration" ]
then
    python manage.py makemigrations bot
    wait
    python manage.py migrate
else
    echo "no command found"
fi