import win32com.client

from service.util import TimeStamp
from service.lib.Subscribe import Subscribe
from model.lib import filesys


class BidAskEvent:
    def set_params(self, com_obj):
        self.com_obj = com_obj

    def OnReceived(self):
        code = self.com_obj.GetHeaderValue(0)
        volume = self.com_obj.GetHeaderValue(2)
        bid = self.com_obj.GetHeaderValue(4)
        ask = self.com_obj.GetHeaderValue(3)
        time = self.com_obj.GetHeaderValue(1)
        timestamp = TimeStamp.hhmm_timestamp(time)

        result_list = [code, volume, bid, ask, timestamp]
        filesys.memory_data(result_list)
        print(result_list)


class BidAsk:
    def subscribe(code):
        Subscribe.start(bidask_obj, bidask_event_obj, code)

    def unsubscribe():
        Subscribe.stop(bidask_obj)

    def get_bidasks(code, bulk_cnt):
        if not bulk_cnt:
            raise ValueError
        result = filesys.select_bulk(code, bulk_cnt)
        return result


bidask_obj = win32com.client.Dispatch("DsCbo1.StockJpBid")
bidask_event_obj = win32com.client.WithEvents(bidask_obj, BidAskEvent)
