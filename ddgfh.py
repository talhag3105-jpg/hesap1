import time
from javascript import require, On
from keep_alive import keep_alive

# 7/24 aktif kalması için web sunucusunu başlatır
keep_alive()

# Mineflayer kütüphanesini yükle
mineflayer = require('mineflayer')

# BOT AYARLARI - Burayı kendi bilgilerinle kontrol et
bot = mineflayer.createBot({
    'host': 'Play.SaloonNetwork.com',
    'port': 25565,
    'username': 'beyzacetin', # Botun oyundaki adı
    'version': '1.21.11'       # Sunucu sürümü
})

print("Bot baslatiliyor... Lutfen bekleyin.")

@On(bot, 'spawn')
def handle_spawn(this, *args):
    print("Bot sunucuya ve dunyaya basariyla giris yapti!")
    
    # Sunucunun botu algılaması için 5 saniye bekleme
    time.sleep(5)
    
    # Otomatik komut gönderimi (Tek blok adana gitmesi için)
    bot.chat('/tekblok')
    print("Komut gonderildi: /tekblok")

@On(bot, 'chat')
def handle_chat(this, username, message, *args):
    # Eğer oyundan bota komut vermek istersen (sadece senin adınla yazılanları dinler)
    if username == "beyzacetin":
        if message.startswith("!yaz "):
            komut = message.replace("!yaz ", "")
            bot.chat(komut)
            print(f"Oyun icinden gelen komut uygulandi: {komut}")

@On(bot, 'kicked')
def handle_kicked(this, reason, *args):
    # Bot sunucudan atılırsa loglara yazar
    print(f"Bot sunucudan atildi! Sebep: {reason}")

@On(bot, 'error')
def handle_error(this, err, *args):
    # Herhangi bir hata oluşursa loglara yazar (Failed hatasını önlemek için önemli)
    print(f"Bir hata olustu: {err}")

# KRİTİK: Render'da 'EOFError' almamak için input("") satırı tamamen kaldırılmıştır.
# Bot artık kendi kendine otomatik bağlanacak.
