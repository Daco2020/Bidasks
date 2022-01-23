from model.code import CodeModels
from flask import jsonify


def insert_code(code):
    if CodeModels.select_one(code):
        return 0
    CodeModels.insert(code)
    return 1


def delete_code(code):
    if not CodeModels.select_one(code):
        return 0
    CodeModels.delete(code)
    return 1


def select_codes():
    return [i["code"] for i in CodeModels.select_all()]