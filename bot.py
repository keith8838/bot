import asyncio
from telethon import TelegramClient

# API ID ve API Hash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Telefon numaranız
phone_number = 'YOUR_PHONE_NUMBER'

# Mesajlar (görsel, metin ve link içeren mesajlar)
messages = [
    {"text": "Mesaj 1: İlk mesaj içeriği", "photo": "https://example.com/image1.jpg", "link": "https://example.com"},
    {"text": "Mesaj 2: İkinci mesaj içeriği", "photo": "https://example.com/image2.jpg", "link": "https://example.com/2"},
    {"text": "Mesaj 3: Üçüncü mesaj içeriği", "photo": "https://example.com/image3.jpg", "link": "https://example.com/3"},
    {"text": "Mesaj 4: Dördüncü mesaj içeriği", "photo": "https://example.com/image4.jpg", "link": "https://example.com/4"},
    {"text": "Mesaj 5: Beşinci mesaj içeriği", "photo": "https://example.com/image5.jpg", "link": "https://example.com/5"}
]

# Gruplar (group_id'leri girmeniz gerekebilir)
groups = [
    'GROUP_ID_1',  # 1. Grup
    'GROUP_ID_2',  # 2. Grup
    'GROUP_ID_3',  # 3. Grup
    'GROUP_ID_4',  # 4. Grup
    'GROUP_ID_5'   # 5. Grup
]

# Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

async def send_scheduled_messages():
    for i in range(len(messages)):
        group_id = groups[i]
        message = messages[i]

        text = message["text"]
        photo_url = message["photo"]
        link = message["link"]
        
        # Görsel, metin ve linki gönderiyoruz
        await client.send_message(group_id, f"{text}\n{link}")
        await client.send_file(group_id, photo_url, caption=text)
        
        print(f"Mesaj {i + 1} gönderildi: {text} - Gruplara gönderiliyor...")

        # 2 saat bekle
        await asyncio.sleep(7200)

async def main():
    # Telegram Client'ı başlat
    await client.start(phone_number)
    
    # Mesajları zamanlayarak gönder
    await send_scheduled_messages()

# Botu başlatıyoruz
with client:
    client.loop.run_until_complete(main())