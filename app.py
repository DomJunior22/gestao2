import mysql.connector
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)


@app.get("/")
def homepage():
    return "homepage.html"



if __name__ == '__main__':
    app.run(debug=True)

