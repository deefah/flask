from flask import Flask
from api import driver
from configuration import route as rou
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





@app.route(rou.route_insert, methods=[rou.method])
def insert_the_driver(): return driver.insert_the_driver()


@app.route(rou.route_select, methods=[rou.method])
def select_the_driver(): return driver.select_the_driver()

@app.route(rou.route_delete, methods=[rou.method])
def delete_the_driver(): return driver.delete_the_driver()


@app.route(rou.route_update, methods=[rou.method])
def update_the_driver(): return driver.update_the_driver()


if __name__ == '__main__':
    app.run(host=rou.host, port=2544)
