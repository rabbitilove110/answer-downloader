# 책이름, 출판사, 링크

import time

data_dict = {}
with open("./database.txt", "r", encoding='UTF-8') as file:
    for line in file:
        key, value, data = line.strip().split(',')
        data_dict[(key, value.strip())] = data
for key, value in data_dict.items():
    data_dict[key] = value.strip()

print(''' ___                                 _                _       _                   _              _           
| . |._ _  ___ _ _ _  ___  _ _   ___| |_  ___  ___  _| |_   _| | ___  _ _ _ ._ _ | | ___  ___  _| | ___  _ _ 
|   || ' |<_-<| | | |/ ._>| '_> <_-<| . |/ ._>/ ._>  | |   / . |/ . \| | | || ' || |/ . \<_> |/ . |/ ._>| '_>
|_|_||_|_|/__/|__/_/ \___.|_|   /__/|_|_|\___.\___.  |_|   \___|\___/|__/_/ |_|_||_|\___/<___|\___|\___.|_|  
                                                                                                             
''')
print("ver.2.0 OBT\n\n문제집 이름과 출판사를 정확히 적어주세요.\n\n주의사항 : github 사이트를 참고해주세요.\n")
name = input("책이름을 입력해주세요 : ")
book = input("출판사를 입력해주세요 : ")

print("--------------------------------")
print("잠시만 기다려주세요. DB에서 데이터를 분석하고있습니다.")
time.sleep(1)

if (('데이터1', '데이터2') in data_dict) or (('데이터A', '데이터B') in data_dict) or (('데이터1-1', '데이터2-1') in data_dict):
    data3 = data_dict[(name, book) if ('데이터1', '데이터2') in data_dict else ('데이터A', '데이터B', '데이터1-1', '데이터2-1')]
    print("--------------------------------")
    print(data3 + " 을(를) 인터넷 주소창에 입력하시면 다운로드가 진행됩니다.\n1분뒤, 코드를 자동 종료합니다.")
    file.close()
    time.sleep(60)
    exit()
else:
    print("--------------------------------")
    print("DB에서 책을 찾지 못했습니다. github Issues로 등록하면 다음 업데이트에 반영됩니다.\n10초뒤, 코드를 자동 종료합니다.")
    file.close()
    time.sleep(10)
    exit()