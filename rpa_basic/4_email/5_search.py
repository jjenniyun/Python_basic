from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #for msg in mailbox.fetch(): # 전체 메일 다 가져오기 # limit=4, reverse=True 갯수를 설정
        #print("[{}] {}".format(msg.from_, msg.subject))
    
    #for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 다 가져오기
        #print("[{}] {}".format(msg.from_, msg.subject))
        
    #for msg in mailbox.fetch('(FROM )', limit=3, reverse=True): # 특정인이 보낸 메일 다 가져오기
        #print("[{}] {}".format(msg.from_, msg.subject))
        
    #for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일 (제목, 본문)
        #print("[{}] {}".format(msg.from_, msg.subject))
        
    #for msg in mailbox.fetch('(SUBJECT "test mail")'): # 어떤 글자를 포함하는 메일 (제목만)
        #print("[{}] {}".format(msg.from_, msg.subject))
        
    #for msg in mailbox.fetch(limit=3, reverse=True): # 어떤 글자(한글)을 포함하는 메일 필터링(제목만)
        #if "테스트" in msg.subject:
            #print("[{}] {}".format(msg.from_, msg.subject))
            
    #for msg in mailbox.fetch('(SENTSINCE 18-JAN-2023)', reverse=True, limit=3): # 특정 날짜 이후의 메일
        #print("[{}] {}".format(msg.from_, msg.subject))
        
    #for msg in mailbox.fetch('(ON 18-JAN-2023)', reverse=True, limit=3): # 특정 날짜에 온 메일
        #print("[{}] {}".format(msg.from_, msg.subject))
    
    # 2가지 이상의 조건을 모두 만족하는 메일
    #for msg in mailbox.fetch('(ON 18-JAN-2023 SUBJECT "test mail")', reverse=True, limit=3):
        #print("[{}] {}".format(msg.from_, msg.subject))
    
    # 2가지 이상의 조건 중 하나라도 만족하는 메일(또는 조건)
    for msg in mailbox.fetch('(OR ON 18-JAN-2023 SUBJECT "test mail")', reverse=True, limit=3):
        print("[{}] {}".format(msg.from_, msg.subject))
        
# 참고 : https://pypi.org/project/imap-tools/