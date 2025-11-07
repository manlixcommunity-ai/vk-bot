import os
import time
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = os.environ.get("VK_GROUP_TOKEN")
if not TOKEN:
    raise SystemExit("⚠️ VK_GROUP_TOKEN not set")

vk = VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)
api = vk.get_api()

print("✅ VK bot started")

for event in longpoll.listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.user_id
            text = event.text.lower()
            print(f"Message from {user_id}: {text}")

            if "привет" in text:
                reply = "Привет! 👋"
            else:
                reply = "Я тебя понял 🙂"

            api.messages.send(user_id=user_id, message=reply, random_id=0)
    except Exception as e:
        print("Error:", e)
        time.sleep(1)
