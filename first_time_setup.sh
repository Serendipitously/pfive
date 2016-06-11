#!/usr/bin/env bash

echo 'Creating virtualenv: pfive'
virtualenv pfive
source pfive/bin/activate

echo 'Installing Django'
pip install django

echo 'Installing Django Rest Framework'
pip install djangorestframework

# TODO: setup local postgres database
