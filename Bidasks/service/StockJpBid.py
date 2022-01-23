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
        # filesys.insert_file(result_list) # csv에 바로 입력할 경우
        filesys.memory_data(result_list) # 메모리에 입력할 경우
        print(result_list)  # 콘솔 확인용


class BidAsk:
    def subscribe(code):
        Subscribe.start(bidask_obj, bidask_event_obj, code)

    def unsubscribe():
        Subscribe.stop(bidask_obj)

    def get_bidasks(code, bulk_cnt):
        if not bulk_cnt:
            return jsonify('Invalid Value'), 400
        return jsonify(filesys.select_bulk(code, bulk_cnt)), 200

# 수정 예정
bidask_obj = win32com.client.Dispatch("DsCbo1.StockJpBid")
bidask_event_obj = win32com.client.WithEvents(bidask_obj, BidAskEvent)
