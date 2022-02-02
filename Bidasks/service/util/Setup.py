import pythoncom
from service.util import CodeHandler


def start_subscribe(object):
    pythoncom.CoInitialize()
    codes = CodeHandler.select_codes()
    objects = []

    for i in range(len(codes)):
        objects.append(object)
        objects[i].subscribe(codes[i])

    pythoncom.PumpMessages()
