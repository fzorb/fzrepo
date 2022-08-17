from flask import Flask, render_template, flash, request
from os import listdir
from os.path import isfile, join
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
  #list all items in static folder
  path = "static/"
  files = [f for f in listdir(path) if isfile(join(path, f))]
  folders = [f for f in listdir(path) if not isfile(join(path, f))]
  rand = randint(0,4)
  return render_template("index.j2", directory="root", files = files, folders = folders, rand = rand)


@app.route("/<directory>")
def dir(directory):
  if directory == "":
    directory == "root"
  path = "static/" + directory
  files = [f for f in listdir(path) if isfile(join(path, f))]
  folders = [f for f in listdir(path) if not isfile(join(path, f))]
  return render_template("index.j2", directory=directory, files = files, folders = folders)
