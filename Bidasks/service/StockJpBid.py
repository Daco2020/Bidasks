import win32com.client
import pythoncom
import threading

from flask import jsonify
from model import BidAskModels
from service.util import CodeHandler, TimeStamp
from service.lib.Subscribe import Subscribe
from model.lib import filesys

class BidAskEvent:
    def set_params(self, com_obj):
        self.com_obj = com_obj

    def OnReceived(self):
        code = self.com_obj.GetHeaderValue(0)  # 종목코드
        volume = self.com_obj.GetHeaderValue(2)  # 거래량
        bid = self.com_obj.GetHeaderValue(4)  # 1차 매수 호가
        ask = self.com_obj.GetHeaderValue(3)  # 1차 매도 호가
        time = self.com_obj.GetHeaderValue(1)  # 시간
        timestamp = TimeStamp.hhmm_timestamp(time)  # 시간 형식 변환

        result_list = [code, volume, bid, ask, timestamp]
        # BidAskModels.insert(result_list)
        filesys.insert_file(result_list)
        print(result_list, threading.currentThread().getName())  # 콘솔 확인용


class BidAsk:
    def subscribe(code):
        Subscribe.start(bidask_obj, bidask_event_obj, code)

    def unsubscribe():
        Subscribe.stop(bidask_obj)

    def get_bidasks(is_bulk, code):
        if is_bulk:
            return jsonify(BidAskModels.select_bulk(code)), 200
        return jsonify(BidAskModels.select_one(code)), 20


bidask_obj = win32com.client.Dispatch("DsCbo1.StockJpBid")
bidask_event_obj = win32com.client.WithEvents(bidask_obj, BidAskEvent)



            # 모델로 가서 파일에 있는 값 불러오기
            # 값이 100개 보다 얼마나 모자른지 확인,
            # 모델로 가서 모자른 수 만큼 디비 최신 값 불러오기
            # 최종적으로 100개의 데이터를 제이슨으로 리턴하기


            # 모델로 가서 파일에 있는 값 불러오기
            # 파일에 값이 한 개도 없다면,
            # 모델로 가서 디비 최신 값 1개 불러오기
            # 최종적으로 1개의 데이터를 제이슨으로 리턴하기