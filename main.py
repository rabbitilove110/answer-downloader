import json
import time

print("ver.3.0 OBT\n\n문제집 이름과 출판사를 정확히 적어주세요.\n\n주의사항 : github 사이트를 참고해주세요.\n")

def load_rules(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)["rules"]

def process_data(input1, input2, rules):
    for rule in rules:
        if rule["input1"] == input1 and rule["input2"] == input2:
            return rule["output"]
    return print("---------------------------\nDB에서 책을 찾지 못했습니다. github Issues로 등록하면 다음 업데이트에 반영됩니다.\n10초후 코드가 자동 종료됩니다.")

# JSON 파일에서 규칙 불러오기
rules = load_rules("database.json")

# 사용자 입력 받기
input1 = input("책이름을 입력해주세요 : ")
input2 = input("출판사를 입력해주세요 : ")

# 결과 처리 및 출력
result = process_data(input1, input2, rules)
if result == None:
    time.sleep(10)
    exit()

print(f"---------------------------\n{result} 을(를) 인터넷 주소창에 입력하시면 다운로드가 진행됩니다.\n1분뒤, 코드를 자동 종료합니다.")
time.sleep(60)
exit()