#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Please supply a single argument of the new app name"
    exit 1
fi

# Make a Python-friendly version of the project name.
PY_PROJECT_NAME=$(echo $1 | tr '-' '_')

perl -i -pe "s/scaffold/$1/g;" app.yaml
perl -i -pe "s/scaffold/$PY_PROJECT_NAME/g;" manage.py scaffold/*.py

mv ./scaffold "$PY_PROJECT_NAME"
