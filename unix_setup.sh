#!/usr/bin/env bash

echo 'Installing virtualenvwrapper'
pip install virtualenvwrapper
source `which virtualenvwrapper.sh`

echo 'Creating virtualenv: pfivev'
mkvirtualenv pfivev
workon pfivev

echo 'Installing python dependencies'
pip install -r requirements.txt

# TODO: setup local postgres database
