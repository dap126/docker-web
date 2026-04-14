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
   # Untuk menyalakan aplikasi
   docker compose up -d

   # Untuk menghentikan aplikasi
   docker compose down
