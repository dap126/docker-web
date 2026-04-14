# Docker Web Counter
Proyek ini adalah contoh aplikasi web sederhana menggunakan Python Flask yang di-dockerize. Aplikasi ini menampilkan pesan dan menghitung jumlah kunjungan (counter) menggunakan Redis, dengan Nginx bertindak sebagai *reverse proxy*.

## Arsitektur
- **Web App**: Python Flask (Berjalan di port 5000 internal)
- **Database**: Redis Alpine (Menyimpan data counter, menggunakan volume persisten)
- **Web Server**: Nginx Alpine (Reverse proxy yang mengekspos aplikasi ke port 8080 eksternal)

## Prasyarat
- Docker terinstal di sistem Anda.
- Docker Compose terinstal.

## Cara Menjalankan Aplikasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/dap126/docker-web.git
   cd docker-web
   ```

2. Jalankan aplikasi menggunakan Docker Compose:
   ```bash
   docker compose up -d
   ```

3. Akses aplikasi melalui browser atau curl:
   Buka http://localhost:8080. Setiap kali Anda me-refresh halaman, angka counter akan bertambah.

4. Untuk menghentikan aplikasi:
   ```bash
   docker compose down
   ```

5. Tunggu hingga Docker selesai mengunduh image Alpine dan membangun aplikasi Anda. Setelah selesai, uji coba dengan membuka browser dan mengakses http://localhost:8080 atau gunakan curl di terminal:
   ```bash
   curl http://localhost:8080
   # Lakukan refresh (atau jalankan perintah curl beberapa kali) untuk melihat angka kunjungan bertambah.
   ```
