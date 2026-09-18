import html
import os
import random
from datetime import datetime

import requests


API_URL = "https://api.alquran.cloud/v1/ayah"
WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")


def ambil_ayat():
    """Ambil satu ayat acak, dengan mode khusus Al-Kahfi setiap Jumat."""
    try:
        if datetime.now().weekday() == 4:
            nomor_ayat = random.randint(1, 110)
            endpoint = f"{API_URL}/18:{nomor_ayat}/editions/quran-uthmani,id.indonesian"
            header = "⚡ JUMAT BERKAH // SURAH AL-KAHFI"
        else:
            nomor_ayat = random.randint(1, 6236)
            endpoint = f"{API_URL}/{nomor_ayat}/editions/quran-uthmani,id.indonesian"
            header = "⚡ MHD DAILY QURAN // VERSE OF THE DAY"

        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("code") != 200:
            return None

        arab = html.escape(data["data"][0]["text"])
        arti = html.escape(data["data"][1]["text"])
        surah = html.escape(data["data"][0]["surah"]["englishName"])
        ayat = data["data"][0]["numberInSurah"]

        return (
            f"<b>╭─「 {header} 」</b>\n"
            "<b>│</b> <code>STATUS: ONLINE  •  SIGNAL: CLEAN</code>\n"
            "<b>╰────────────────────</b>\n\n"
            f"<i>{arab}</i>\n\n"
            f"<b>▸ TRANSLATION</b>\n<blockquote>{arti}</blockquote>\n"
            f"<b>⌁ SOURCE:</b> <code>QS. {surah} : {ayat}</code>\n\n"
            "<b>┌─[ MHD REMINDER ]</b>\n"
            "<b>│</b> 📡 <b>Channel:</b> t.me/autoposting_quran\n"
            "<b>│</b> 🌐 <b>Page:</b> fb.com/RuntimeIman\n"
            "<b>└────────────────────</b>\n\n"
            "<code>#AlQuran #SelfReminder #DailyVerse #RuntimeIman #MHDWarrior</code>"
        )

    except (requests.RequestException, KeyError, TypeError, ValueError) as error:
        print(f"[!] Gagal mengambil ayat: {error}")
        return None


def kirim_ke_webhook(pesan):
    if not WEBHOOK_URL:
        print("[!] MAKE_WEBHOOK_URL belum diatur.")
        return False

    try:
        response = requests.post(
            WEBHOOK_URL,
            json={"text": pesan},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        response.raise_for_status()
        print(f"[+] Webhook terkirim ({response.status_code}).")
        return True
    except requests.RequestException as error:
        print(f"[!] Pengiriman webhook gagal: {error}")
        return False


if __name__ == "__main__":
    print("\033[92m╭─[ MHD QURAN NODE ]────────────────╮\033[0m")
    print("\033[92m│  daily reminder service: ONLINE    │\033[0m")
    print("\033[92m╰────────────────────────────────────╯\033[0m")

    ayat_hari_ini = ambil_ayat()
    if ayat_hari_ini:
        kirim_ke_webhook(ayat_hari_ini)
    else:
        print("[!] Tidak ada konten yang bisa dikirim.")
