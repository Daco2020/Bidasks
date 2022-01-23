
from unittest import IsolatedAsyncioTestCase
import pythoncom
import threading
import time

from flask import Flask, request, jsonify, json
from json.decoder import JSONDecodeError
from service import BidAsk, CodeHandler, Setup

from model.lib import filesys 


app = Flask(__name__)


@app.route("/subscribe/<code>", methods=["POST", "DELETE"])
def subscribe(code):
    if request.method == "POST":
        return jsonify(CodeHandler.insert_code(code))
    elif request.method == "DELETE":
        return jsonify(CodeHandler.delete_code(code))


@app.route("/unsubscribe", methods=["GET"])
def unsubscribe():
    BidAsk.unsubscribe()
    return jsonify("Success"), 200


@app.route("/bidask", methods=["GET"])
def bidask():
    try:
        is_bulk = json.loads(request.args.get("bulk", 0))
        code = request.args.get("code", 0)
        return BidAsk.get_bidasks(is_bulk, code)

    except JSONDecodeError as e:
        return jsonify(e.msg), 400


@app.route("/")
def start(): 
    thread = threading.Thread(target=Setup.start_subscribe, args=(BidAsk,))
    thread.start()
    return "Success", 200


@app.route("/ping")
def test():
    while True:
        result_list = ['A005930', '9910903', '77200', '77300', '2022-01-14']
        time.sleep(1)
        print(result_list)
        filesys.insert_file(result_list)
    return "pong"


if __name__ == "__main__":
    app.debug = True
    app.run()
    pythoncom.PumpMessages()

    
