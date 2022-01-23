import datetime


def hhmm_timestamp(hhmm):
    return datetime.datetime.today().replace(hour=hhmm // 100, minute=(hhmm % 100))
    # return datetime.datetime.today().replace(hour=hhmm // 100, minute=(hhmm % 100)).timestamp() * 1000

# def hhmmss_timestamp(hhmmss):
#     return datetime.datetime.today().replace(hour=hhmmss // 10000, minute=(hhmmss % 10000) // 100,
#                                              second=(hhmmss % 100), microsecond=0).timestamp() * 1000
# def current_timestamp():
#     return  datetime.datetime.today().timestamp() * 1000
