import datetime


def hhmm_timestamp(hhmm):
    return datetime.datetime.today().replace(hour=hhmm // 100, minute=(hhmm % 100))
