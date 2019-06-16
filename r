
pkill gunicorn;
gunicorn kaoshi.wsgi --worker-class=gevent -b 127.0.0.1:9001 --access-logfile /tmp/gun_kaoshi.access --error-logfile /tmp/gun_kaoshi.error

