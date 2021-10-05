import json
import xmltodict
import pyautogui

position = pyautogui.position()

print(pyautogui.size())
print(position.x)
print(position.y)

#before = "1번줄\n2번줄"
before = """
'[서울=뉴시스] 전진환 기자 = 문재인 대통령이 5일 서울 그랜드 워커힐호텔에서 열린 제15회 세계한인의 날 기념식에서 기념사를 하고 있다. 2021.10.05. amin2@newsis.com\n\n청와대는 5일 야당의 ‘대장동  
개발 사업’ 의혹 특검 요구에 대해 “엄중하게 지켜보고 있다”고 했다. 청와대가 대장동 의혹과 관련해 입장을 낸 것은 이번이 처음이다.\n\n청와대 관계자는 이날 청와대 춘추관에서 기자들과 만나 ‘문재인 대통령이 대장동 개발 사업 관련 의혹
에 침묵하고 있다’는 야당의 공세에 대한 입장을 묻는 질문에 이같이 답했다.\n\n청와대 관계자는 “현재 시점에서 드릴 수 있는 건 청와대는 엄중하게 생각하고 지켜보고 있다는 말씀”이라며 “문자 그대로 이해해달라”고 했다.\n\n앞서 김기현  
국민의힘 원내대표는 “정의, 공정을 기치로 외치던 문 대통령이 침묵하고 있다”며 대장동 의혹 진상 규명을 위해 특검을 수용하라고 촉구했다.\n\n김 원내대표는 지난 3일에도 문 대통령을 향해 “여당의 유력 대권 후보와 그 측근들이 대거 연루
된 권력형 비리 사건의 구린내가 펄펄 나는데도 ‘선택적 침묵’으로 일관하며 아예 국정을 외면하고 있다”며 “침묵해 주는 대가로 퇴임 후를 보장이라도 받겠다는 암묵적 생각은 설마 아니실 것으로 믿고 싶다”고 했다.'
"""
#articleContent.replace("\", "\\")
after = before.replace('\n',"<br>")
#print(tmp)
print(after)


""" 
xmlCode = '<tistory><status>200</status><postId>186</postId><url>https://hellodoor.tistory.com/186</url></tistory>'

jsonStr = json.dumps(xmltodict.parse(xmlCode), indent=4)

print(jsonStr)

dict = json.loads(jsonStr)
print(dict)

print(dict['tistory'])
print(dict['tistory']['postId'])
"""