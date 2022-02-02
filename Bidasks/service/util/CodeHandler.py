from model.code import CodeModels
from flask import jsonify


def insert_code(code):
    if CodeModels.select_one(code):
        raise ValueError
    CodeModels.insert(code)
    return True


def delete_code(code):
    if not CodeModels.select_one(code):
        raise ValueError
    CodeModels.delete(code)
    return True


def select_codes():
    return [i["code"] for i in CodeModels.select_all()]
