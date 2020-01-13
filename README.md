# Alpha_Poker

2019년 2학기 오픈소스 기초설계 과목 2조 프로젝트 'Alpha Poker' 입니다.

본 과목에서는 라즈베리파이, ev3, 브레드보드를 이용하여 무언가를 만드는 것을 목표로 기말 프로젝트를 진행했습니다.
언어는 오직 Python 만을 사용해야 했습니다.

2조는 '실제 포커 카드, 칩을 이용해 인공지능과 게임을 하는 것'을 목표로 프로젝트를 진행했습니다.
본 프로젝트에서는 다양한 포커게임 종류 중에서 서양권에서 주로 플레이 하는 '텍사스 홀덤'을 선택했습니다.

==============================


0. 포커 엔진

포커 엔진은 오픈소스인 PyPokerEngine 을 사용하였습니다.
PyPokerEngine은 인공지능 학습을 위해 파이썬으로 만들어진 포커 엔진입니다.


==============================


1. tts ( PyPokerEngine-master/pypokerengine/engine/tts.py )

본 프로젝트에서는 플레이어가 모니터 화면을 보지 않고 음성으로 게임 진행 상황을 전달받기를 원했습니다.
그래서 텍스트를 음성으로 읽어주는 TTS (Text to Speech) 를 도입했습니다.

TTS로 전달받는 내용은 아래와 같습니다
- 라운드의 시작, 끝을 알림 ( eg : 1라운드가 시작되었습니다 )
- 라운드 중에서 특정 단계에 들어섰을 때 이를 알림 ( eg : River입니다 )
- 게임의 승패를 알려줌 ( eg : 인공지능의 승리입니다. 인공지능의 패는 투페어, 플레이어의 패는 원페어입니다. )
- 인공지능의 결정을 알려줌 ( eg : 인공지능이 폴드를 선언했습니다 )
- 플레이어에게 지시를 함 ( eg : 폴드, 콜, 레이즈 중에 선택해주세요 )
- 카메라로 카드를 입력받을 때 딜러에게 지시를 함 ( eg : 플레이어의 카드를 입력시켜주세요 )
- 게임 진행을 위해 필요한 간단한 안내, 지시사항들

TTS 서비스는 네이버 클로바를 이용했습니다.
국내 서비스이기 때문에 한국어 발음에 최적화 되어있고 1000자당 4원으로 저렴한 가격 때문에 선택하였습니다.

게임의 진행을 담당하는 round_manger.py, 인공지능을 담당하는 honest_player.py, 플레이어를 담당하는console_player.py 등 
tts 호출이 필요한 각각의 파일에서 tts.py 의 requestTts 함수를 호출하여 tts를 받아오도록 합니다.
mp3 형태로 요청한 tts 파일을 네이버 서버에서 받아오고, 이를 playTts 에서 재생하도록 하였습니다.


==============================


2. QR코드 인식 ( PyPokerEngine-Master/engine/qrReader.py )

PyPokerEngine 상에서 게임을 진행할 때 본래는 컴퓨터 내에서 난수를 발생시켜 카드를 배분해주도록 되어있습니다.

본 프로젝트에서는 실제 카드로 게임을 하기 원했기 때문에 실제 카드 정보를 카메라를 통해 입력받아야 했습니다.
따라서 카드에 'C9' (클로버 9), 'DT' (다이아 10) 등의 정보가 담긴 QR코드를 붙이고 라즈베리파이에 연결 된 카메라를 통해 이를 입력받도록 하였습니다.

작동 방식은 아래와 같습니다.

매 라운드가 시작될 떄 round_manager( PyPokerEngine-Master/engine/round_manager.py )에서 qrReader의 returnCardList 함수를 호출합니다.
returnCardList 에서 csvClean 함수를 호출하여 카메라를 통해 읽은 카드 리스트를 저장하는 csv 파일을 초기화 시킵니다.
이후 총 9장의 카드를 입력받는데, 1-2번째 카드는 인공지능의 카드, 3-4번째는 카드는 플레이어의 카드, 나머지 카드는 순서대로 공개되는 커뮤니티 카드가 됩니다.
이때 딜러가 이를 인지할 수 있도록 "인공지능의 카드를 입력시켜 주세요." 따위의 안내 음성을 재생시킵니다.

입력이 제대로 이루어졌는지 checkCSV 함수를 호출하여 확인하고 입력이 제대로 이루어지지 않았다면 "다시 입력시켜주세요." 라는 음성을 출력시키도록 합니다.

9장의 카드가 모두 입력되어 csv 파일에 저장이 된다면 이를 list 형태로 return 합니다.
round_manager.py 에서는 return 받은 list를 이용해 게임을 진행시킵니다.


==============================


3. 인공지능 커스터마이징 ( PyPokerEngine-Master/players/honest_player.py )

PyPokerEngine의 기본 인공지능 중 'Honest Player'를 상대 측 인공지능으로 사용하였습니다.
Hoenst Player는 자신의 패와 공개된 커뮤니티 카드 정보를 받아들인 후 
상대방의 패와 아직 공개되지 않은 커뮤니티 카드를 랜덤으로 분배하여 1,000번 시뮬레이션 돌리고
그때의 예상 승률을 기반으로 플레이를 하도록 짜여져 있습니다.

기본 옵션은 예상 승률이 50% 이상일 때 call을, 50% 미만일 때 fold를 하도록 되어있었으나
게임의 재미를 위해서 아래와 같이 수정하였습니다.

0% ~ 50% : fold
50% ~ 70% : call
70% ~ 80% : 배팅 가능 최소치만큼 raise
80% ~ 90% : 최소치 x 0.8 + 최대치 x 0.2 만큼 raise
90% ~ 95% : 최소치 x 0.6 + 최대치 x 0.4 만큼 raise
95% ~ 97.5% : 최소치 x 0.4 + 최대치 x 0.6 만큼 raise
97.5% ~ 99% : 최소치 x 0.2 + 최대치 x 0.8 만큼 raise
99% ~ 100% : allin

이때 raise를 하게 된다면 플레이어를 도발하는 대사 중 하나를 랜덤으로 tts를 이용해 음성 출력하도록 하였습니다.

또한 인공지능이 정직하게만 게임을 하면 곤란하므로 일정 확률로 '블러핑'을 하도록 수정했습니다.


==============================


4. 플레이어 준비 ( PyPokerEngine-Master/players/console_player.py )

PyPokerEngine은 기본적으로 인공지능 사이의 게임을 위해 만들어진 엔진이지만
플레이어가 직접 콘솔창을 통해 게임에 참가할 수 있도록 'Console Player' 옵션이 준비되어 있습니다.

본 프로젝트에서는 모니터가 아닌 실제 포커 테이블을 보며 게임을 하기 원했기 때문에
불필요하게 큰 키보드로 입력을 받는 대신, 작은 숫자패드로 입력을 받길 원했습니다.

따라서 원래 fold 옵션은 (f), call 옵션은 (c), raise 옵션은 (r)으로 입력을 받도록 되어있는 것을
숫자패드상에 일렬로 있는 키인 (/), (*), (-) 으로 받도록 수정했습니다.


==============================


5. 포커칩 발사

인공지능과 플레이어 양쪽 모두 배팅을 했을 때 자동으로 포커칩을 발사하도록 설계했습니다.
원통에 칩을 쌓아두고 인공지능이나 플레이어가 n개만큼 배팅을 선언했을 때
원통 아래에 있는 바퀴가 돌아가며 원하는 갯수만큼 칩을 뱉어내도록 하였습니다.

이떄 칩의 하중에 따라 똑같이 1개의 칩을 뱉을 때에도 바퀴가 돌아가는 시간이 다른 문제가 생겼습니다.
그래서 칩 보관함 위에 무게추를 두어 하중을 가능한 일정하게 고정시켰습니다.


==============================


6. EV3 - 라즈베리파이 연결 문제

칩을 발사하는 역할을 담당하는 EV3가 라즈베리파이와 네트워크를 통해 통신하도록 할 계획이였습니다.
그러나 지급받은 라즈베리파이 모델이 통신에 문제가 있어 EV3에 연결할 수 없었습니다.

라즈베리파이가 EV3에 전달해줘야 할 정보는 "칩을 몉개를 뱉어내야 하는가" 인데
이 정보를 LED를 통해 전달하기로 하였습니다.

전달해주어야 할 정보는 "칩을 몉 개를 뱉어야 하는가" 에서 "바퀴를 몇 초동안 회전시켜야 하는가" 로 바꾸었습니다.
칩을 n개 뱉고자 한다면 라즈베리파이에서 n개를 뱉기 위한 시간 동안 LED에 불이 들어오도록 하였습니다.
LED에 불이 들어오는걸 EV3에서 광센서를 통해 인식하고, 이 시간동안 바퀴를 회전시켜 칩을 뱉어냅니다.

이때 칩을 뱉어내는 과정에서 하중이 변하기 때문에 n개를 뱉어내기 위한 필요한 시간이 ( n * 1개를 뱉어내기 위해 필요한 시간 ) 과 일치하지 않음을 발견했습니다.
예를들어 1개를 뱉어내기 위해 0.5초를 회전해야 하는데, 5개를 뱉어내기 위해서는 2.3초만 회전해야 하는 식의 문제입니다.
이 문제를 해결하기 위해 1개부터 20개까지 일일이 필요한 시간을 측정하여 입력시켰습니다.


==============================


7. 테이블 설계

우드락과 아크릴 판을 이용하여 테이블을 직접 제작하였습니다.

- 포커칩을 보관하는 곳
- 각 플레이어가 포커칩을 받는 측면부
- 카드를 올려두고 카메라를 통해 인식하는 중앙부
- 중앙부 아래에 라즈베리파이, 스피커, LED, 케이블 등을 고정-보관하는 부분
