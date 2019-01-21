#!/bin/sh
uwsgi -d /var/uwsgi/uwsgi_demoapp.log /home/proj/uwsgi.ini
celery -A proj worker -l info