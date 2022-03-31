from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "hello Lilly to my website! nananana 123456"

if __name__ == "__main__":
    print("starting python Flask")
    app.run(port=5000)

#to run the flask app: python3 server.py