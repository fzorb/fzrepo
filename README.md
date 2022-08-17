# repo
running the repo:
```sh
#(only for linux)
#make a venv and install flask
python -m venv env
#activate the venv
source env/bin/activate
#install flask and gunicorn
pip install flask gunicorn
#run the repo
gunicorn --bind 0.0.0.0:4350 wsgi:app
```
