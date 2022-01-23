from flask import jsonify
import pythoncom


class Subscribe:
    def start(com_obj, event_obj, code):
        com_obj.SetInputValue(0, code)
        event_obj.set_params(com_obj)
        com_obj.Subscribe() #
        print(f"Subscribe 시작 : {code}")

    def stop(com_obj):
        com_obj.Unsubscribe()
        print(f"Subscribe 종료")

