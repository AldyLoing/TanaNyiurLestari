# 🌴 Tana Nyiur Lestari - Sistem Manajemen Bank Sampah

![Django](https://img.shields.io/badge/Django-5.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistem manajemen bank sampah berbasis web yang komprehensif dengan fitur gamifikasi poin dan sistem multi-level untuk koordinasi antara yayasan, bank induk, bank unit, dan nasabah.

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Teknologi](#-teknologi)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Struktur Role](#-struktur-role)
- [Sistem Poin](#-sistem-poin)
- [Screenshot](#-screenshot)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

## 🎯 Tentang Proyek

**Tana Nyiur Lestari** adalah platform digital yang dirancang untuk mengelola ekosistem bank sampah dengan sistem poin reward. Aplikasi ini memfasilitasi pengelolaan sampah berkelanjutan dengan memberikan insentif kepada masyarakat yang berkontribusi dalam daur ulang sampah.

### Tujuan

- 🌍 Mendorong kesadaran lingkungan melalui daur ulang sampah
- 💰 Memberikan nilai ekonomi dari sampah melalui sistem poin
- 📊 Menyediakan dashboard monitoring real-time untuk pengelola
- 🗺️ Memetakan lokasi bank sampah untuk kemudahan akses
- 🤝 Menghubungkan berbagai stakeholder dalam satu platform

## ✨ Fitur Utama

### 👥 Manajemen Pengguna Multi-Level
- **Role-based Access Control** (4 level: Admin Yayasan, Admin Induk, Admin Unit, Member)
- Registrasi dan autentikasi pengguna
- Manajemen profil dengan foto
- Sistem aktivasi/deaktivasi akun
- CRUD operations lengkap

### ♻️ Manajemen Transaksi Sampah
- Input transaksi dengan 5 kategori sampah:
  - 🥤 Plastik (10 poin/kg)
  - 📄 Kertas (5 poin/kg)
  - 🔩 Logam (15 poin/kg)
  - 🍃 Organik (2 poin/kg)
  - 🛢️ Minyak Jelantah (20 poin/kg)
- Kalkulasi poin otomatis
- Filter dan pencarian transaksi
- Export data ke CSV
- Riwayat transaksi lengkap

### 💎 Sistem Poin & Reward
- Akumulasi poin dari setiap transaksi
- Penukaran poin ke uang (1 poin = Rp 1.000)
- Sistem approval penukaran poin
- Riwayat penukaran dengan status
- Real-time balance checking

### 📊 Dashboard & Analytics
- Statistik real-time (nasabah, bank, poin, sampah)
- Grafik per kategori sampah
- Laporan bulanan dan tahunan
- Export laporan ke CSV
- Monitoring pending tasks

### 🗺️ Pemetaan Lokasi
- Integrasi Google Maps
- Marker lokasi bank sampah
- Pencarian bank terdekat
- Detail informasi bank sampah

### 🏢 Manajemen Konten
- Sistem posting/blog dengan gambar
- Image slider untuk homepage
- Manajemen informasi (Profil, Visi-Misi, Program)
- Link management untuk program eksternal
- Manajemen mitra/partner

### 🔐 Keamanan
- Django authentication system
- Role-based permissions
- CSRF protection
- Session management
- Secure password validation

## 🛠️ Teknologi

### Backend
- **Framework**: Django 5.1
- **Language**: Python 3.10
- **Database**: SQLite3
- **ORM**: Django ORM

### Frontend
- **Template Engine**: Django Templates
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Maps**: Google Maps API

### Libraries
```
Django==5.1
Pillow  # Image processing
django-humanize  # Humanize data
```

## 📥 Instalasi

### Prerequisites
- Python 3.10 atau lebih tinggi
- pip (Python package manager)
- Git

### Langkah-langkah Instalasi

1. **Clone repository**
```bash
git clone https://github.com/AldyLoing/TanaNyiurLestari.git
cd TanaNyiurLestari
```

2. **Buat virtual environment**
```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

3. **Install dependencies**
```bash
cd Blog
pip install -r requirements.txt
```

4. **Jalankan migrasi database**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Buat superuser (admin)**
```bash
python manage.py createsuperuser
```

6. **Jalankan development server**
```bash
python manage.py runserver
```

7. **Akses aplikasi**
```
http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/
```

## 🚀 Penggunaan

### Untuk Admin Yayasan

1. Login ke admin panel
2. Akses dashboard untuk melihat statistik keseluruhan
3. Kelola bank sampah unit dan admin
4. Monitor dan approve penukaran poin
5. Kelola konten website (slider, mitra, informasi)

### Untuk Admin Bank Sampah Unit

1. Login dengan akun admin unit
2. Kelola nasabah di bank sampah Anda
3. Input transaksi sampah nasabah
4. Monitor statistik bank sampah unit
5. Approve penukaran poin nasabah

### Untuk Nasabah/Member

1. Daftar akun baru atau login
2. Lihat saldo poin Anda
3. Cek riwayat transaksi sampah
4. Ajukan penukaran poin
5. Lihat status penukaran poin

## 👤 Struktur Role

| Role | Akses | Fungsi Utama |
|------|-------|--------------|
| **Admin Yayasan** | Full access | Kelola seluruh sistem, approve semua penukaran, kelola konten |
| **Admin Bank Induk** | Manage units | Kelola bank sampah unit dan monitoring |
| **Admin Bank Unit** | Own bank only | Kelola nasabah, input transaksi, approve penukaran |
| **Member/Nasabah** | Limited | Lihat transaksi, tukar poin, cek saldo |

## 💰 Sistem Poin

### Kalkulasi Poin

Poin dihitung otomatis berdasarkan:
```
Poin = Berat (kg) × Rate per Kategori
```

### Rate per Kategori
- Minyak Jelantah: **20 poin/kg**
- Logam: **15 poin/kg**
- Plastik: **10 poin/kg**
- Kertas: **5 poin/kg**
- Organik: **2 poin/kg**

### Penukaran Poin
- Minimum penukaran: **50 poin**
- Kelipatan: **50 poin**
- Nilai tukar: **Rp 1.000 per poin**
- Contoh: 100 poin = Rp 100.000

### Alur Penukaran
1. Nasabah request penukaran
2. Status: **Pending**
3. Admin review dan approve/reject
4. Status: **Approved** → Poin dikurangi, uang dicairkan
5. Status: **Rejected** → Poin dikembalikan

## 📸 Screenshot

### Homepage
![Homepage](docs/homepage.png)

### Dashboard Admin
![Dashboard](docs/dashboard.png)

### Transaksi Sampah
![Transaksi](docs/transaksi.png)

### Pemetaan Bank Sampah
![Maps](docs/maps.png)

## 📁 Struktur Proyek

```
TanaNyiurLestari/
├── Blog/                      # Main project directory
│   ├── Blog/                  # Project settings
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py           # Main URL configuration
│   │   └── wsgi.py           # WSGI configuration
│   ├── posting/              # Main app
│   │   ├── models.py         # Database models
│   │   ├── views.py          # View functions
│   │   ├── forms.py          # Django forms
│   │   ├── urls.py           # App URLs
│   │   └── admin.py          # Admin configuration
│   ├── template/             # HTML templates
│   │   ├── base.html         # Base template
│   │   ├── posting/          # Posting templates
│   │   ├── users/            # User management
│   │   ├── transactions/     # Transaction pages
│   │   └── profile/          # Profile pages
│   ├── static/               # Static files (CSS, JS, images)
│   ├── media/                # User uploaded files
│   ├── manage.py             # Django management script
│   ├── requirements.txt      # Python dependencies
│   └── db.sqlite3           # SQLite database
├── env/                      # Virtual environment
└── README.md                 # Documentation
```

## 🔧 Konfigurasi

### Environment Variables

Untuk production, buat file `.env`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url

# Google Maps API
GOOGLE_MAPS_API_KEY=your-api-key
```

### Google Maps API

1. Dapatkan API key dari [Google Cloud Console](https://console.cloud.google.com/)
2. Aktifkan Maps JavaScript API
3. Tambahkan API key ke settings.py atau .env

## 🧪 Testing

Jalankan tests:
```bash
python manage.py test
```

## 📦 Deployment

### Persiapan Production

1. **Update settings.py**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

2. **Collect static files**
```bash
python manage.py collectstatic
```

3. **Setup database** (PostgreSQL/MySQL untuk production)

4. **Deploy ke platform**
   - Heroku
   - Railway
   - PythonAnywhere
   - DigitalOcean
   - AWS

### Contoh Deploy ke Heroku

```bash
# Install Heroku CLI dan login
heroku login

# Buat app baru
heroku create tana-nyiur-lestari

# Setup database
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Jalankan migrasi
heroku run python manage.py migrate

# Buat superuser
heroku run python manage.py createsuperuser
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

### Guidelines

- Ikuti Python PEP 8 style guide
- Tulis docstring untuk fungsi/class
- Tambahkan tests untuk fitur baru
- Update dokumentasi jika perlu

## 🐛 Bug Reports

Jika menemukan bug, silakan [buat issue](https://github.com/AldyLoing/TanaNyiurLestari/issues) dengan:
- Deskripsi detail bug
- Langkah reproduksi
- Expected vs actual behavior
- Screenshot (jika perlu)
- Environment (OS, Python version, dll)

## 📝 TODO List

- [ ] Implement notification system
- [ ] Add email verification
- [ ] Mobile responsive improvements
- [ ] API REST untuk mobile app
- [ ] Real-time chat dengan admin
- [ ] Integration dengan payment gateway
- [ ] Multi-language support (EN/ID)
- [ ] Advanced analytics dashboard
- [ ] PWA (Progressive Web App)
- [ ] Export laporan ke PDF

## 📄 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Author

**Aldy Loing**

- GitHub: [@AldyLoing](https://github.com/AldyLoing)
- Email: [your-email@example.com]

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Maps API](https://developers.google.com/maps)

## 📞 Support

Jika Anda memiliki pertanyaan atau butuh bantuan:

- 📧 Email: [your-email@example.com]
- 💬 GitHub Issues: [Create an issue](https://github.com/AldyLoing/TanaNyiurLestari/issues)
- 📱 WhatsApp: [Your WhatsApp Number]

---

⭐ **Jika proyek ini bermanfaat, berikan star di GitHub!**

Made with ❤️ for a sustainable environment 🌱
