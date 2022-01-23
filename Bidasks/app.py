import pythoncom

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify, json
from json.decoder import JSONDecodeError

from service import BidAsk, CodeHandler, Setup
from model.lib import filesys


# ------
# 스케줄 실행 코드
def scheduler():
    Setup.start_subscribe(BidAsk)


def storage():
    filesys.insert_db()


cron = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
cron.add_job(scheduler)
cron.add_job(storage, 'cron', hour='16', minute='5')
cron.start()
# ------


app = Flask(__name__)


@app.route("/subscribe/<code>", methods=["POST", "DELETE"])
def subscribe(code):
    if request.method == "POST":
        return jsonify(CodeHandler.insert_code(code))
    elif request.method == "DELETE":
        return jsonify(CodeHandler.delete_code(code))


@app.route("/bidask", methods=["GET"])
def bidask():
    try:
        bulk_cnt = json.loads(request.args.get("bulk", 0))
        code = request.args.get("code", 0)
        return BidAsk.get_bidasks(code, bulk_cnt)

    except JSONDecodeError as e:
        return jsonify(e.msg), 400


if __name__ == "__main__":
    app.debug = True
    app.run()
    pythoncom.PumpMessages()
