#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Please supply a single argument of the new app name"
    exit 1
fi

perl -i -pe "s/scaffold/$1/g;" app.yaml manage.py
perl -i -pe "s/scaffold/$1/g;" scaffold/*.py

mv ./scaffold "$1"
