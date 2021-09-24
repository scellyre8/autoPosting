import requests
# pip install requests
from datetime import datetime

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
     for i in data:
          
          # <p data-ke-size="size16"><a href={i[1]}>{i[1]}</a>&nbsp;</p>
          
          html += f"""
               <p data-ke-size="size16">&nbsp;</p>
               <p data-ke-size="size16"><h2><a href={i[1]}>{i[0]}</a></h2></p>
               <p><img src={i[2]}/></p>
               <p data-ke-size="size16">&nbsp;</p>
               """
          if cnt == 3:
               html += centerAd
          if cnt == len(data):
               html += infeed
          cnt += 1

     print(html)

     parameters = {
          'access_token': '5cdf432b969ce6d9197cefe1ed21cebc_7feada863ee0b7b8bec09804ab4195d1',
          'blogName': 'hellodoor',
          'title': str(year) + '년 ' + str(mon) + '월 ' + str(day) + '일 뉴스 데일리 헤드라인',
          'content': html,
          'visibility': '3',
          'category': '974645',
          'tag': 'news, naver news, headline news, 뉴스, 네이버뉴스, 헤드라인 뉴스, python, 티스토리 api',
          'acceptComment': '1'
     }

     response = requests.post(tistoryUrl, params=parameters)
     print(response.reason)
     print(response.json)