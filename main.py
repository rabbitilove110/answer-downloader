# 책이름, 출판사, 링크

import time

data_dict = {}
with open("./database.txt", "r", encoding='UTF-8') as file:
    for line in file:
        key, value = line.strip().split(',') # key,value 문제 있음
        data_dict[key] = value

print("Answer sheet downloader, ver.1.0dev\n\n문제집 이름과 출판사를 적어주세요.\n예시 : OO수학 - OO문고\n\n주의사항 : github 사이트를 참고해주세요.\n")
name = input("책이름을 입력해주세요 : ")
book = input("출판사를 입력해주세요 : ")

print("--------------------------------")
print("잠시만 기다려주세요. DB에서 데이터를 분석하고있습니다.")
time.sleep(3)

if (name in data_dict and book in data_dict) or (name + '-1' in data_dict and book + '-1' in data_dict):
    data_key = name if name in data_dict else name + '-1'
    data_key2 = book if book in data_dict else book + '-1'
    data3 = data_dict[data_key]
    
    dataurl = (f"{data_key}:", data3)
    print("--------------------------------")
    print(dataurl + "을(를) 인터넷 주소창에 입력하시면 자동 다운로드가 진행됩니다.\n1분뒤, 코드를 자동 종료합니다.")
    file.close()
    time.sleep(60)
    exit()
else:
    print("--------------------------------")
    print("DB에서 책을 찾지 못했습니다. github Issues로 등록하면 다음 업데이트에 반영됩니다.\n10초뒤, 코드를 자동 종료합니다.")
    file.close()
    time.sleep(10)
    exit()