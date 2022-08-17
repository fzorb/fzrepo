sudo kill -9 $(sudo lsof -t -i:4350)
gunicorn --bind 0.0.0.0:4350 wsgi:app
