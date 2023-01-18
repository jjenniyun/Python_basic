import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS #보내는 사람
msg["To"] = "" # 받는 사람 메일 주소

# 여러명에게 메일을 보낼 때
#msg["To"] = "" 여러명의 메일 주소 넣기
#to_list = [""] 여러명의 메일 주소 넣기
#msg["To"] = ", ".join(to_list)

# 참조 메일
#msg["Cc"] = ""

# 비밀 참조
#msg["Bcc"] = ""

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)