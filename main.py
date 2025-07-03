import os
import sys
import datetime
import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 🎯 한국 공휴일 목록 (YYYY-MM-DD 형식)
HOLIDAYS = {
    "2025-01-01",  # 신정
    "2025-03-01",  # 삼일절
    "2025-05-06",  # 대체공휴일
    "2025-10-07",  # 추석연휴
    "2025-10-09",  # 한글날
    "2025-12-25",  # 크리스마스
}

# 📆 오늘 날짜 가져오기
today = datetime.date.today().strftime("%Y-%m-%d")

# 🚫 오늘이 공휴일이면 실행하지 않고 종료
if today in HOLIDAYS:
    print(f"📢 오늘({today})은 공휴일이므로 실행하지 않습니다.")
    sys.exit(0)

# 환경 변수에서 Slack 토큰 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"⚠️ Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n"
            f"\n\n"
            f"투명하고 정확한 컬리 자산 관리를 위해 *<https://static.wixstatic.com/media/50072f_f952f1f91caf42909fb376a73cbcc167~mv2.png|[부서별 자산 담당자]>* 와 *[자산관련 준수사항]* 에 대해 공유 드립니다.\n"
            f"\n"
            f"구성원 여러분들의 많은 도움과 협조를 통해 건강하고 안전한 우리 클러스터가 되도록 부탁드립니다.\n"
            f"\n"
            f"\n"
            f"📌 *자산관련 준수사항*\n"
            f"1️⃣ 자산 (아래 취급품목 참고)에 대해서 *위치 이동이 필요할 경우 [부서별 자산 담당자] 내용 공유*:bangbang:\n"
            f"2️⃣ 자산 품목에 대해 *라벨 스티커 훼손 금지*:x:\n"
            f"3️⃣ 자산 *임의 해체 및 낙서/덧붙임 등 금지*:x:\n"
            f"\n"
            f"\n"
            f" :ck11: * <https://static.wixstatic.com/media/50072f_ea6f09357fe44c53a5b8e4fcd2805d61~mv2.png|자산 취급 품목 리스트>*\n\n"
            f" :ck11: * <https://static.wixstatic.com/media/50072f_df6ebbab79f741ae89d27bed689e2bc8~mv2.png|자산 취급 주의 사항>*\n\n"
            f" :ck11: * <https://static.wixstatic.com/media/50072f_524d17c8b9a244148d97038df010aaae~mv2.png|자산 분해,훼손 금지 안내>*\n\n"
            f"\n\n"
            f":phone: *문의사항* : 총무/시설_담당자 <@U05NUU65F19> <@U05P7L4MY1F> 및 각 부서별 자산 담당자 \n\n"
            f"감사합니다.  😊\n"
            f"\n"
        )
 
# 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
