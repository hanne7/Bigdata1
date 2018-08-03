from gtts import gTTS

default_str = """안녕하세요. 나열심입니다. 스마트홈네트워크를 구동시키겠습니다.
오늘의 뉴스를 알려드리겠습니다.
홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며
MBN뉴스와 싸우고 있습니다. 뉴스 재미있어요? 그럼 안녕!"""
default_str = """아키텍쳐반 제자들아 안녕! 더운 날씨에 지각하지 않고 와줘서 고맙다. 오늘도 화이팅하자!"""
default_str = """나고객님 안녕하세요. 저희 아키쇼핑몰에 방문해 주셔서 감사합니다.
고객님의 최근 6개월간의 구매 패턴을 분석하여 최근 출시된 플레이스테이션 파이브를 
추천상품으로 권해드립니다.
해당 상품을 조회하실 의향이 있으시면 '네' 라고 말씀해주세요.
"""
emotion_str="안녕하세요. 안녕하세요? 안녕하세요! 안녕하세요.. 젠장. 젠장? 젠장!"

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("google_vocal_test.mp3")

    open('google_vocal_test.mp3')

speaker(default_str)
# speaker(emotion_str)