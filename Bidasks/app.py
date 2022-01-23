from socketserver import UDPServer
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


'''
<구현 사항>
1. flask 서버를 실행하면 DB에 저장된 종목 코드들의 실시간 호가 데이터를 받아온다.
   - 메모리에 데이터가 100개 이상이 되면 벌크로 파일에 저장한다.

2. bidask 요청을 하면 최근 데이터를 반환한다.(params : code, bulk)
   - 해당 종목의 최근 데이터를 bulk의 값(숫자) 만큼 가져온다.
   - 메모리에 반환할 데이터가 모자른 경우 파일 데이터를 가져와 함께 반환한다.

3. 매일 4시 5분이 되면 메모리와 csv파일에 있는 데이터를 모두 DB로 옮긴다.
   - apschedule을 활용하여 비동기적으로 해당 스케줄을 실행한다.
'''