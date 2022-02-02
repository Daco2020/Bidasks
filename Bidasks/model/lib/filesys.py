import csv

from model.BidAsk import BidAskModels


args = []
memory_args = []


def memory_data(arg):
    args.append(arg)
    if len(args) > 99:
        insert_file(args)
        args.clear()

    global memory_args
    memory_args = args


def insert_file(args):
    with open('bidasks.csv', 'a', newline='') as data:
        writer = csv.writer(data)
        writer.writerows(args)


def insert_db():
    data_list = []

    with open('bidasks.csv', 'r', encoding='utf-8') as data:
        data = csv.reader(data)
        for row in data:
            data_list.append(row)
        BidAskModels.insert_bulk(data_list)

    with open('bidasks.csv', 'w') as data:
        data.write("")


def select_bulk(code, bulk_cnt):
    file_rows = []

    memory_rows = [row for row in memory_args if row[0] == code][-bulk_cnt:]
    required_count = bulk_cnt - len(memory_rows)

    if required_count > 0:
        file_rows = select_file_bulk(code, required_count)

    result_rows = file_rows + memory_rows

    result = [{
        "cnt": i+1,
        "code": result_row[0],
        "volume": int(result_row[1]),
        "bid": int(result_row[2]),
        "ask": int(result_row[3]),
        "timestamp": result_row[4]
    } for i, result_row in enumerate(reversed(result_rows))]

    return result


def select_file_bulk(code, count):
    with open('bidasks.csv', 'r', encoding='utf-8') as data:
        data = csv.reader(data)

        rows = [row for row in data if row[0] == code]
        result_rows = rows[-count:]

        return result_rows
