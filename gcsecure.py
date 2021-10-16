import aminofix
import time
from gtts import gTTS
import requests

client=aminofix.Client()

client.login(email="cedes75547@specialistblog.com",password="pagal0")

print("logged in.....")

cid="31519183"
cidy=31519183

subclient=aminofix.SubClient(comId=cid,profile=client.profile)

print("inside community")
@client.event("on_avatar_chat_start")
def on_avatar_start_chat_start(data):
	if data.comId==cidy:
		if subclient.get_chat_thread(data.message.chatId).title!=None:
			try:
				subclient.send_message(chatId=data.message.chatId,message=f"Ghost message by <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
				subclient.kick(userId=data.message.author.userId,chatId=data.message.chatId,allowRejoin=True)
				print(f"Someone spamed gc")
			except Exception as e:
				print(e)