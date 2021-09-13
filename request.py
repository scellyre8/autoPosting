import requests
# pip install requests

tistoryUrl = 'https://www.tistory.com/apis/post/write?'

parameters = {
    'access_token': '5cdf432b969ce6d9197cefe1ed21cebc_7feada863ee0b7b8bec09804ab4195d1',
    'blogName': 'hellodoor',
    'title': '테스트 제목',
    'content': '테스느 내용',
    'visibility': '3',
    'category': '867576',
    'tag': '태그1, 태그2, 태그3',
    'acceptComment': '1'
}

response = requests.post(tistoryUrl, params=parameters)
print(response.reason)
print(response.json)


