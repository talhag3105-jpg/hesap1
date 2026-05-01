from flask import Flask
from threading import Thread

# Flask uygulaması oluşturuyoruz
app = Flask('')

@app.route('/')
def home():
    # Bu yazı UptimeRobot linkine tıkladığında ekranda görünecek
    return "Bot su an aktif ve 7/24 calisiyor!"

def run():
    # Sunucuyu 8080 portunda (Replit/Render standartı) baslat
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    # Sunucuyu ana koddan bagimsiz bir kolda (thread) calistir
    t = Thread(target=run)
    t.start()