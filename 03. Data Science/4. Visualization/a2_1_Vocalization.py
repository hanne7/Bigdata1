import urllib.request
client_id = ""
client_secret = ""
default_str = """안녕하세요. 나열심입니다. 스마트홈네트워크를 구동시키겠습니다.
오늘의 뉴스를 알려드리겠습니다.
홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며
MBN뉴스와 싸우고 있습니다. 뉴스 재미있어요? 그럼 안녕!"""
default_str = """나고객님 안녕하세요. 저희 아키쇼핑몰에 방문해 주셔서 감사합니다.
고객님의 최근 6개월간의 구매 패턴을 분석하여 최근 출시된 플레이스테이션 파이브를 
추천상품으로 권해드립니다.
해당 상품을 조회하실 의향이 있으시면 '네' 라고 말씀해주세요.
"""
emotion_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"
# encText = urllib.parse.quote(emotion_str)
encText = urllib.parse.quote(default_str)
data = "speaker=jinho&speed=0&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode == 200):
    print('TTS mp3 저장')
    response_body = response.read()
    with open('naver_vocal_test.mp3', 'wb') as f:
        f.write(response_body)
else:
    print('Error Code:' + rescode)