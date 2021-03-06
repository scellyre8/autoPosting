import requests
# pip install requests
from datetime import datetime

import json
import xmltodict
import contentWrite

today = datetime.today()
year = today.year
mon = today.month
day = today.day

centerAd = """
<!-- 중간 -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-7987528933298369"
     data-ad-slot="8666138171"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""
infeed = """
<!-- 인피드? -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-7987528933298369"
     data-ad-slot="5980367997"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

print(centerAd)
print(infeed)
#print(content)

def autoWrite(data):
 
     tistoryUrl = 'https://www.tistory.com/apis/post/write?'

     print(len(data))
     cnt = 1
     html = ""
     thumTitle = ""
     for i in data:
          
          html += f"""
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><h2><a href={i[1]}>{i[0]}</a></h2></p>
<div style="width:550px; height:auto; text-align:center;"><img style="max-width:100%; max-height:100%;" src={i[2]}/></div>
<div class="box">
     <div class="content">{i[3]}</div>
</div>
"""
          # 첫 카운트 기사 제목 저장
          if cnt == 1:
               thumTitle = i[0]
          if cnt == 3:
               html += centerAd
          if cnt == len(data):
               html += infeed
          cnt += 1

     parameters = {
          'access_token': 'd3f25823c237dc088a66208479cc6568_25ea1642bae665bac4925e40cc8423dd',
          'blogName': 'movietrap',
          'title': str(year) + '년 ' + str(mon) + '월 ' + str(day) + '일 헤드라인 뉴스 모음/' + thumTitle,
          'content': '',
          'visibility': '3',
          'category': '1235081',
          'tag': 'news, naver news, headline news, 뉴스, 네이버뉴스, 헤드라인 뉴스, python, 티스토리 api',
          'acceptComment': '1'
     }

     response = requests.post(tistoryUrl, params=parameters)
     print(response.text)

     xmlData = response.text
     # xml형식 -> json으로 변환
     jsonStr = json.dumps(xmltodict.parse(xmlData), indent=4)
     # json -> dic으로 변환
     dict = json.loads(jsonStr)

     print(dict['tistory'])
     print(dict['tistory']['postId'])

     result = []
     result.append(dict['tistory']['postId'])
     result.append(html)
     
     contentWrite.editPosting(result)