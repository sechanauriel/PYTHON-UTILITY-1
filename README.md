**Python Utility Collection**
- **Description:**: Kumpulan skrip utilitas sederhana untuk tugas sehari-hari (web scraping, rename file, countdown, password generator, weather lookup).

**Files Included**
- **`github_profile_scraper.py` (original name: `. Web Scraping (Foto Profil GitHub)`)**: Ambil URL foto profil GitHub pengguna; skrip awal menggunakan selector sederhana. Akan diperbarui untuk lebih robust.
- **`bulk_file_renamer.py` (original name: `Bulk File Renamer`)**: Ganti nama file di sebuah folder menjadi `img0.jpg`, `img1.jpg`, ... (ubah `path` di dalam skrip sebelum menjalankan).
- **`countdown_timer.py` (original name: `Countdown Timer`)**: Hitung mundur berbasis detik.
- **`password_generator.py` (original name: `Password Generator`)**: Hasilkan password acak (atur jumlah dan panjang pada prompt).
- **`weather_app.py` (original name: `Weather App`)**: Panggil OpenWeatherMap API dan tampilkan data mentah JSON (ganti `API_Key` dulu).

**Prerequisites**
- **Python:** Versi yang terpasang pada virtual environment workspace (di `.venv`).
- **Dependencies:** `requests`, `beautifulsoup4`, `pillow`, `pyzbar`, `qrcode` (beberapa skrip tidak memerlukan semua paket). Untuk memasang:

```powershell
Set-Location "D:\ISTN\SEMESTER_3\Rekayasa Perangkat Lunak Dan Desain Sistem\PTYHON_UTILITY_1"
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install requests beautifulsoup4 pillow pyzbar qrcode
```

**Menjalankan Skrip**
- Jika file belum diubah ke `.py` (nama file saat ini adalah nama deskriptif tanpa ekstensi), jalankan dengan path lengkap interpreter venv:

```powershell
& "D:/ISTN/SEMESTER_3/Rekayasa Perangkat Lunak Dan Desain Sistem/PTYHON_UTILITY_1/.venv/Scripts/python.exe" "Bulk File Renamer"
```

- Disarankan: ubah nama file ke ekstensi `.py` agar mudah dijalankan dan diedit. Contoh rename (PowerShell):

```powershell
Rename-Item -Path ".\Bulk File Renamer" -NewName "bulk_file_renamer.py"
Rename-Item -Path ".\Countdown Timer" -NewName "countdown_timer.py"
Rename-Item -Path ".\Password Generator" -NewName "password_generator.py"
Rename-Item -Path ".\Weather App" -NewName "weather_app.py"
Rename-Item -Path ".\. Web Scraping (Foto Profil GitHub)" -NewName "github_profile_scraper.py"
```

Setelah di-rename, jalankan misal:

```powershell
& ".\.venv\Scripts\python.exe" "github_profile_scraper.py"
```

**Catatan Khusus per Program**
- **`weather_app.py`**: Ganti `API_Key = 'masukkan_api_key_anda_disini'` dengan API key OpenWeatherMap Anda terlebih dahulu.
- **`bulk_file_renamer.py`**: Ubah variabel `path` ke folder target Anda sebelum menjalankan. Perhatian: operasi ini akan menimpa nama file — backup jika perlu.
- **`github_profile_scraper.py`**: GitHub mengubah struktur HTML secara berkala. Skrip awal memakai selector sederhana (`img[alt='Avatar']`) yang mungkin tidak selalu ditemukan. Akan diperbarui menjadi lebih robust (cek `meta[property="og:image"]`, `link[rel=image_src]`, atau elemen `.avatar-user`) dan menambahkan header `User-Agent` serta opsi untuk mengunduh gambar.

**Perbaikan yang Direncanakan**
- Update scraper supaya lebih andal: coba beberapa selector secara urut, tambahkan timeout, user-agent, dan opsi unduh file.
- Tambahkan validasi input untuk `bulk_file_renamer.py` dan konfirmasi sebelum menimpa file.

**Layanan & Lisensi**
- Skrip ini bersifat pembelajaran/utility kecil—gunakan dengan bijak. Tidak ada lisensi khusus ditambahkan.

Jika Anda ingin, saya bisa:
- A: Langsung mengganti nama file menjadi `.py` dan jalankan tes singkat.
- B: Memperbarui `github_profile_scraper.py` sekarang (selector + download) dan menjalankan test untuk username contoh.

Beritahu pilihan Anda atau instruksi lain.
