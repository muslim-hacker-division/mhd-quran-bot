import os
import telebot
import requests
import random

# --- KONFIGURASI SAFE ---
TOKEN = os.getenv('BOT_TOKEN') # Kunci rahasianya
CHANNEL_ID = '@autoposting_quran'
bot = telebot.TeleBot(TOKEN)

# --- FUNGSI AMBIL AYAT ACAK (API QURAN) ---
def get_random_quran():
    try:
        # Ambil nomor ayat acak antara 1 sampai 6236
        ayat_id = random.randint(1, 6236)
        # Pakai API alquran.cloud (stabil & gratis)
        url = f"https://api.alquran.cloud/v1/ayah/{ayat_id}/editions/quran-uthmani,id.indonesian"
        
        response = requests.get(url)
        data = response.json()
        
        if data['code'] == 200:
            arab = data['data'][0]['text']
            indo = data['data'][1]['text']
            surah = data['data'][0]['surah']['englishName']
            no_surah = data['data'][0]['surah']['number']
            no_ayat = data['data'][0]['numberInSurah']
            
            return {
                "teks": f"<b>[ MHD DAILY QURAN ]</b>\n\n"
                        f"<code>{arab}</code>\n\n"
                        f"<i>\"{indo}\"</i>\n\n"
                        f"📌 <b>QS. {surah} [{no_surah}:{no_ayat}]</b>\n"
                        f"🛡️ @autoposting_quran"
            }
    except Exception as e:
        print(f"Error API: {e}")
        return None

# --- HANDLER: /start ---
@bot.message_handler(commands=['start'])
def sapa_user(message):
    salam = (
        "<b>[ ACCESS GRANTED ]</b>\n\n"
        "Assalamu'alaikum, bross! 🛡️\n"
        "Bot MHD Aktif. Ketik /kirim buat tes kirim ayat acak ke channel @autoposting_quran."
    )
    bot.reply_to(message, salam, parse_mode='HTML')

# --- COMMAND KHUSUS ADMIN: /kirim ---
@bot.message_handler(commands=['kirim'])
def kirim_ke_channel(message):
    print(">>> Menjalankan perintah kirim ayat acak...")
    data_quran = get_random_quran()
    if data_quran:
        bot.send_message(CHANNEL_ID, data_quran['teks'], parse_mode='HTML')
        bot.reply_to(message, "✅ Berhasil kirim ayat acak ke channel!")
    else:
        bot.reply_to(message, "❌ Gagal mengambil data API.")

if __name__ == "__main__":
    print("\033[92m[ MHD VIRTUAL WARRIOR ONLINE ]\033[0m")
    
    # Ambil ayat acak
    data_ayat = get_random_quran()
    
    if data_ayat:
        # Kirim ke channel
        bot.send_message(CHANNEL_ID, data_ayat['teks'], parse_mode='HTML')
        print(">>> Misi Sukses: Ayat sudah mendarat di channel!")
    else:
        print(">>> Misi Gagal: Gagal ambil data dari API.")
