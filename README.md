📖 MHD Auto Quran Bot
MHD Auto Quran Bot adalah sistem otomasi pengingat ayat Al-Quran berbasis serverless yang berjalan di atas infrastruktur GitHub Actions[cite: 1]. Bot ini dirancang untuk menyebarkan pesan inspiratif secara terjadwal ke berbagai platform media sosial secara otomatis[cite: 1].

🚀 Fitur Utama
Automated Scheduling: Penjadwalan posting 3x sehari (Subuh, Siang, Malam) tanpa intervensi manual[cite: 1].

Friday Special Logic: Sistem otomatis mendeteksi hari Jumat untuk membagikan ayat-ayat dari Surah Al-Kahfi[cite: 1].

Multi-Platform Broadcast: Distribusi konten secara simultan ke channel Telegram dan Facebook Pages melalui jalur enkripsi API[cite: 1].

Dynamic Content Engine: Integrasi real-time dengan Al-Quran Cloud API untuk data yang akurat[cite: 1].

🛠️ Arsitektur Sistem
Command Center (GitHub Actions): Bertindak sebagai otak yang memicu eksekusi kode sesuai parameter waktu yang ditentukan[cite: 1].

Core Processor (Python): Script cerdas yang mengambil data, memproses teks, dan merakit paket informasi dalam format HTML[cite: 1].

Distribution Bridge: Jalur distribusi privat yang menjembatani server pemroses dengan API sosial media (Facebook & Telegram)[cite: 1].

📂 Struktur Repositori
bot_quran.py: Script inti pemrosesan data dan logika distribusi[cite: 1].

.github/workflows/main.yml: Konfigurasi trigger otomatisasi[cite: 1].

requirements.txt: Daftar dependensi sistem[cite: 1].

⚙️ Konfigurasi Rahasia
Fork repositori ini.

Atur GitHub Secrets sebagai variabel lingkungan:

BOT_TOKEN: Akses kredensial bot.

MAKE_WEBHOOK_URL: Jalur distribusi privat (Bridge URL).

Aktifkan GitHub Actions untuk memulai operasi[cite: 1].

🛡️ Lisensi
Proyek ini dilindungi oleh lisensi MIT[cite: 1]. Digunakan untuk tujuan edukasi dan penyebaran konten positif.

Dibuat dengan semangat otomasi oleh Runtime Iman (MHD Warrior)[cite: 1].
