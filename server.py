#!/usr/bin/env python3

from bottle import route, run, static_file, template
import requests
from datetime import datetime
import locale

r = requests.get("https://backend.yituliu.site/api/find/stage/t3?expCoefficient=0.625")
data = r.json()["data"]

locale.setlocale(locale.LC_ALL, "zh_CN.UTF-8")
today = datetime.today().strftime("%x")


@route("/static/<filename>")
def serve_static(filename):
    return static_file(filename, root="./static")


@route("/")
def root():
    return template("material", item_id=30063, data=data, today=today)


run(host="localhost", port=8080)
