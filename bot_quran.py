import os
import telebot
import requests
import random
from datetime import datetime

# --- KONFIGURASI ---
TOKEN = os.getenv('BOT_TOKEN')
URL_MAKE = os.getenv('MAKE_WEBHOOK_URL')

bot = telebot.TeleBot(TOKEN)

def get_content():
    try:
        # Ambil angka hari (0=Senin, 3=Kamis, 4=Jumat)
        hari_ini = datetime.now().weekday()
        
        if hari_ini == 4:
            # Mode Jumat: Al-Kahfi (Ayat 1-110)
            ayat_id = random.randint(1, 110)
            url = f"https://api.alquran.cloud/v1/ayah/18:{ayat_id}/editions/quran-uthmani,id.indonesian"
            prefix = "📖 <b>[ JUMAT BERKAH - AL-KAHFI ]</b>"
        else:
            # Mode Biasa: Ayat Acak dari seluruh Al-Quran
            ayat_id = random.randint(1, 6236)
            url = f"https://api.alquran.cloud/v1/ayah/{ayat_id}/editions/quran-uthmani,id.indonesian"
            prefix = "📖 <b>[ MHD DAILY QURAN ]</b>"
        
        # Tambahkan timeout 10 detik agar tidak hang jika API lambat
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('code') == 200:
            arab = data['data'][0]['text']
            arti = data['data'][1]['text']
            surah = data['data'][0]['surah']['englishName']
            nomor = data['data'][0]['numberInSurah']
            
            # Menyusun pesan dengan format rapi
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
        print(f"Error saat mengambil konten: {e}")
    return None

if __name__ == "__main__":
    print("\033[92m[ MHD VIRTUAL WARRIOR ONLINE ]\033[0m")
    
    # Ambil konten ayat
    ayat = get_content()
    
    if ayat:
        # KIRIM KE MAKE.COM
        try:
            # Gunakan header JSON agar Make.com membaca datanya
            headers = {'Content-Type': 'application/json'}
            payload = {"text": ayat}
            
            res = requests.post(URL_MAKE, json=payload, headers=headers, timeout=10)
            
            if res.status_code == 200:
                print(f">>> Status Webhook: {res.status_code} (Berhasil Dikirim)")
                print(">>> Misi Berhasil: Pesan mendarat di target.")
            else:
                print(f">>> Webhook Diterima tapi bermasalah: {res.status_code}")
                print(f">>> Respon: {res.text}")
                
        except Exception as e:
            print(f">>> Gagal kirim ke Webhook: {e}")
    else:
        print(">>> Misi Gagal: Variabel ayat kosong.")
