"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr5rgu9tun42u5l41g-a.oregon-postgres.render.com",
        database="todo_0uyj",
        user="todo_0uyj_user",
        password="1e2Pfi3DQhZKnGIpaeZ576RPCPEHb9M4")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
