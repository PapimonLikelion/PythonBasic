# +15593160287
# AC0abd69f18bfdcd5af23e126056e92de6
# 9d2a028d8ae09d79ff4013722b730948

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
#패키지에서 CLIENT 모듈 갖고옴


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0abd69f18bfdcd5af23e126056e92de6'
auth_token = '9d2a028d8ae09d79ff4013722b730948'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="이재현씨 안녕하세요! 새로운 핸드폰 개통을 축하드립니다. 이 문자는 애플 본사에서 핸드폰을 바꿔주신 몇몇의 고객님들의 한해 전송되는 축하문자로 이 문자를 받으셨다면 아마 남자친구가 애플에 신청하지 않았을까 합리적 추론이 가능합니다. 소감을 남자친구분께 알려주시면 좋아하실것 같습니다.",
                    from_='+15593160287',
                    to='+821029004869',
                )

print(message.sid)
