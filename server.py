from flask import Flask, request, jsonify
from sql_connection import get_sql_connection


import products_dao

connection = get_sql_connection() 

app = Flask(__name__)

@app.route("/")


def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("starting python Flask")
    app.run(port=5000)

#to run the flask app: python3 server.py