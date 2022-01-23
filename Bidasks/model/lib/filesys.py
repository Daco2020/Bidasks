from os import linesep
import sys, time

from black import os
from model.BidAsk import BidAskModels


def insert_db():
    with open('bidasks.csv') as data:
        data_list = []

        for line in data.readlines(): 
            data_list.append(line.split()) 

        BidAskModels.insert_bulk(data_list)

        data_list.clear()

        # os.remove('bidasks.csv') 
        # 다른 프로세스가 파일을 사용 중이기 때문에 프로세스가 액세스 할 수 없습니다
        # 지금 해결해야하는 문제는 저장 후 파일을 초기화 해야하는 것
        # 빠른 반환을 위해 캐쉬, 즉 메모리에는 100개 저장하고 있을 것 

def insert_file(args):
    with open('bidasks.csv','a') as data:

        for i in args:
            data.write(i+" ")

        data.write("\n")




# args = ["test", 1, 2, 3]
# file_db(args)

    # for i in args:
    #     f.write(str(i)+",")
    # f.write("\n")


# def asd():
# with open('bidasks.csv') as data:
#     a = []
#     for line in data.readlines(): 
#         a.append(line.split()) # 스플릿이 있어야 \n이 제외됨
#         if len(a) == 100:
#             print("100개가 찼습니다!, 디비에 입력합니다.")
#             insert_all(a)
#             a.clear()


# sys.stdout = open('bidasks.csv','w') # 생성 및 쓰기
# sys.stdout 


# while True:
#     print('A005930', '9910903', '77200', '77300', '2022-01-14 15:43:57')
#     time.sleep(1)

# def asd():

#     sys.stdout = open('bidasks.csv','w') # 생성 및 쓰기
#     sys.stdout 

# print(1,2,3,"asdasd","zxc")

# # open('output.txt','a') # 이어쓰기

# # open('folder/output.txt','w') # 경로 설정하기

# # python test.py > output.txt # 터미널에서 실행 명령어

# # python test.py >> output.txt # 터미널에서 이어 쓰기

# # python test.py > folder/output.txt # 터미널에서 경로설정

# # python test.py > "some folder/output.txt" # 폴더명에 공백이 있는 경우

# # https://opentutorials.org/module/2980/17643


# filename = 'dump.csv'
# with open(filename) as data:
#     lines = data.readlines()
 
# # # print(lines)

# # # for line in lines:
# # #     a = line.split()
# # # print(a)

# numbers=[]
# for line in lines:
#     numbers.append(line.split())
# print(numbers)

# with open(filename) as data:
#     numbers = [[i for i in line.split()] for line in data.readlines()]
#     print(numbers)



# def file_db(args):
#     f = open('bidasks.csv','a')
#     sys.stdout = f # stdout을 이용하면 프린트를 저장할 수 있음, 단 열려있는동안 모든 프린트가 저장되고 콘솔에 찍히지 않음
#     print(
#         args[0],
#         args[1],
#         args[2],
#         args[3],
#     )
#     sys.stdin = f
#     pass









'''
파일에 데이터를 저장한다.
요청이 오면 파일에 있는 데이터를 모두 디비로 저장한다.
디비에서 원하는 만큼 값을 불러온다.
'''