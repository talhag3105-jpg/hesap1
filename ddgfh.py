from javascript import require, On
import time
import threading # Terminal girdisi için gerekli

mineflayer = require('mineflayer')

# --- AYARLAR ---
IP_ADRESI = 'Play.SaloonNetwork.com'
BOT_ADI = 'beyzacetin'
SIFRE = 'a818A939'
SURUM = '1.21.11' 
# ---------------

bot = mineflayer.createBot({
    'host': IP_ADRESI,
    'username': BOT_ADI,
    'version': SURUM
})

# --- TERMİNALDEN KONTROL FONKSİYONU ---
def terminal_control():
    while True:
        komut = input("") # Terminale yazdığın şeyi bekler
        if komut:
            bot.chat(komut) # Yazdığın her şeyi oyuna iletir
            print(f"📡 Komut gönderildi: {komut}")

# Terminal dinlemeyi ayrı bir kolda (thread) başlat
threading.Thread(target=terminal_control, daemon=True).start()

@On(bot, 'spawn')
def handle_spawn(*args):
    print(f"✅ {BOT_ADI} sunucuya girdi! Terminalden komut yazabilirsin.")
    
    # Otomatik giriş süreci
    time.sleep(5)
    bot.chat(f'/login {SIFRE}')
    
    time.sleep(8)
    bot.chat('/tekblok')
    
    time.sleep(12)
    bot.chat('/home')

@On(bot, 'chat')
def handle_chat(this, username, message, *args):
    # Oyundaki konuşmaları terminalde görmen lazım ki ne olduğunu bilesin
    print(f"💬 [{username}]: {message}")

@On(bot, 'kicked')
def handle_kicked(this, reason, *args):
    print(f"❌ Atıldık! Sebep: {reason}")

@On(bot, 'error')
def handle_error(this, err, *args):
    print(f"⚠️ Hata: {err}")