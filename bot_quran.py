import os
import telebot
import requests
import random
from datetime import datetime

# --- KONFIGURASI ---
TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = '@autoposting_quran'
BOT_USERNAME = 'mhd_pengingat_bot' 
# TEMPEL LINK
URL_MAKE = os.getenv('MAKE_WEBHOOK_URL')

bot = telebot.TeleBot(TOKEN)

def get_content():
    try:
        # Cek hari (4 = Jumat)
        hari_ini = datetime.now().weekday()
        
        if hari_ini == 4:
            # Mode Jumat: Al-Kahfi
            ayat_id = random.randint(1, 10)
            url = f"https://api.alquran.cloud/v1/ayah/18:{ayat_id}/editions/quran-uthmani,id.indonesian"
            prefix = "📖 <b>[ JUMAT BERKAH - AL-KAHFI ]</b>"
        else:
            # Mode Biasa: Ayat Acak
            ayat_id = random.randint(1, 6236)
            url = f"https://api.alquran.cloud/v1/ayah/{ayat_id}/editions/quran-uthmani,id.indonesian"
            prefix = "📖 <b>[ MHD DAILY QURAN ]</b>"
        
        response = requests.get(url)
        data = response.json()
        
        if data['code'] == 200:
            arab = data['data'][0]['text']
            arti = data['data'][1]['text']
            surah = data['data'][0]['surah']['englishName']
            nomor = data['data'][0]['numberInSurah']
            
            pesan = (
                f"{prefix}\n\n"
                f"<i>{arab}</i>\n\n"
                f"\"{arti}\"\n\n"
                f"📌 <b>QS. {surah} [{nomor}]</b>\n\n"
                f"📡 <b>Channel:</b> t.me/autoposting_quran\n"
                f"🌐 <b>Page:</b> fb.com/RuntimeIman\n\n"
                f"#AlQuran #SelfReminder #DailyVerse #RuntimeIman #MHDWarrior"
            )
            return pesan
    except Exception as e:
        print(f"Error: {e}")
    return None

if __name__ == "__main__":
    print("\033[92m[ MHD VIRTUAL WARRIOR ONLINE ]\033[0m")
    
    ayat = get_content()
    if ayat:
        # JALUR LAMA nonaktifkan
        # bot.send_message(CHANNEL_ID, ayat, parse_mode='HTML')
        
        # 2. KIRIM KE MAKE.COM (UNTUK FACEBOOK & TELEGRAM BARU)
        try:
            # Kita kirim variabel 'ayat' ke Webhook dengan nama field 'text'
            res = requests.post(URL_MAKE, json={"text": ayat})
            print(f">>> Status Webhook: {res.status_code}")
        except Exception as e:
            print(f">>> Gagal kirim ke Webhook: {e}")

        print(">>> Misi Berhasil: Pesan mendarat di target.")
    else:
        print(">>> Misi Gagal.")
