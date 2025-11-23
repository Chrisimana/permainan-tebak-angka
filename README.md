# 🎯 Permainan Tebak Angka

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Game](https://img.shields.io/badge/type-game-purple)

**Permainan tebak angka klasik dengan GUI modern, sistem statistik, dan penyimpanan history**

</div>

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Fitur](#-fitur)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Dokumentasi](#-dokumentasi)
- [Contoh Permainan](#-contoh-permainan)
- [FAQ](#-faq)

## 🚀 Gambaran Umum

**Permainan Tebak Angka** adalah evolusi modern dari permainan tebak angka klasik. Dibangun dengan Python dan Tkinter, game ini tidak hanya menyajikan gameplay yang menyenangkan tetapi juga dilengkapi dengan fitur-fitur canggih seperti sistem statistik, penyimpanan history, dan antarmuka yang menarik.

### ✨ Highlights

- 🎨 **GUI Modern** dengan tema warna yang eye-catching
- 📊 **Sistem Statistik** lengkap dengan persentase kemenangan
- 💾 **Penyimpanan Otomatis** riwayat permainan
- 🏆 **Leaderboard** permainan terakhir
- 🔄 **Gameplay Dinamis** dengan petunjuk tebakan
- 🎮 **Kontrol Keyboard** untuk pengalaman bermain yang smooth

## 🌟 Fitur

### 🎯 Core Gameplay
- **Tebak Angka 1-10** - Gameplay klasik yang sederhana namun menantang
- **3 Kesempatan** - Tantangan yang seimbang untuk pemain
- **Petunjuk Cerdas** - Sistem hint "lebih besar/lebih kecil"
- **Random Generator** - Angka acak yang benar-benar random setiap game

### 📈 Analytics & Statistics
- **Statistik Real-time** - Total permainan, menang, kalah
- **Persentase Kemenangan** - Track performa bermain
- **Rata-rata Tebakan** - Analisis efisiensi tebakan
- **History Visual** - Tampilan tebakan sebelumnya dengan status

### 💾 Data Management
- **Auto-save JSON** - Penyimpanan otomatis dalam format terstruktur
- **Multiple Sessions** - Kelola banyak sesi permainan
- **Data Persistence** - Data tetap tersimpan setelah aplikasi ditutup
- **Export Ready** - Struktur data siap untuk diekspor

### 🎨 GUI Features
- **Modern Interface** - Desain clean dan profesional
- **Color Coding** - Warna berbeda untuk status berbeda
- **Responsive Layout** - Tampilan optimal berbagai ukuran layar
- **Real-time Updates** - Update UI secara real-time
- **Visual Feedback** - Emoji dan ikon untuk pengalaman lebih hidup

### ⌨️ User Experience
- **Keyboard Support** - Input dengan Enter key
- **Input Validation** - Validasi otomatis untuk input tidak valid
- **Game State Management** - Management status permainan yang robust
- **Reset Instant** - Mulai game baru dengan satu klik

### Fitur Interaktif

```
🎯 Status Permainan:
Kesempatan tersisa: 3
Tebakan salah! Coba angka yang lebih besar

📊 Statistik:
Total Permainan: 15
Menang: 8
Kalah: 7
Persentase Menang: 53.3%

🕒 Permainan Terakhir:
14:30 🎉 MENANG
14:25 😞 KALAH
14:20 🎉 MENANG
```

## 📥 Instalasi

### Prerequisites

- Python 3.7 atau lebih tinggi
- Tkinter (biasanya sudah termasuk dalam instalasi Python)

### Verifikasi Python dan Tkinter

```bash
python --version
python -m tkinter
```

Jika muncul window tkinter, berarti siap digunakan!

### Step-by-Step Installation

1. **Download Project**
   ```bash
   git clone https://github.com/username/tebak-angka-super.git
   cd tebak-angka-super
   ```

2. **Buat Virtual Environment (Recommended)**
   ```bash
   python -m venv game_env
   # Windows
   game_env\Scripts\activate
   # Linux/Mac
   source game_env/bin/activate
   ```

3. **Jalankan Aplikasi**
   ```bash
   python main.py
   ```

### Quick Install (Windows)
```bash
# Download semua file ke satu folder
python main.py
```

## 🎮 Penggunaan

### Menjalankan Game

```bash
python main.py
```

### Basic Gameplay

1. **Memulai Permainan**
   - Game otomatis generate angka rahasia 1-10
   - Anda memiliki 3 kesempatan untuk menebak

2. **Cara Bermain**
   - Masukkan angka 1-10 di input field
   - Tekan `Enter` atau klik tombol "Tebak!"
   - Dapatkan petunjuk "lebih besar" atau "lebih kecil"
   - Tebak sampai benar atau kesempatan habis

3. **Status Permainan**
   - 🎉 **MENANG** - Tebakan benar dalam 3 kesempatan
   - 😞 **KALAH** - Kesempatan habis sebelum tebakan benar
   - 🔄 **BERMAIN** - Masih dalam permainan aktif

### Keyboard Controls

| Shortcut | Action |
|----------|--------|
| `Enter` | Submit tebakan |
| `Ctrl + R` | Reset game baru |
| `1-0` | Input angka langsung |

### Fitur Khusus

- **Input Validation** - Otomatis memvalidasi angka 1-10
- **Auto-focus** - Input field selalu siap untuk mengetik
- **Real-time Updates** - Statistik update secara real-time
- **Visual History** - Lihat semua tebakan sebelumnya dengan status ✓/✗

## 📚 Dokumentasi

### File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Entry point aplikasi, menjalankan GUI |
| `game_logic.py` | Core gameplay logic dan state management |
| `gui.py` | Antarmuka pengguna dengan Tkinter |
| `history_manager.py` | Management penyimpanan dan load history |
| `history_tebak_angka.json` | File penyimpanan data permainan |

## 💡 Contoh Permainan

### Scenario 1: Menang dalam 2 Tebakan
```
🎯 Status: BERMAIN
Kesempatan: 3

Tebakan 1: 5
➤ "Tebakan salah! Coba angka yang lebih besar"

Tebakan 2: 8  
➤ "Selamat! Tebakan Anda benar! Angka rahasia adalah 8"

📊 Statistik Update:
Total: 16, Menang: 9, Kalah: 7, Menang: 56.2%
```

### Scenario 2: Kalah dalam 3 Tebakan
```
🎯 Status: BERMAIN  
Kesempatan: 3

Tebakan 1: 3 ➤ "Lebih besar"
Tebakan 2: 7 ➤ "Lebih kecil" 
Tebakan 3: 5 ➤ "Game Over! Angka rahasia adalah 6"

📊 Statistik Update:
Total: 17, Menang: 9, Kalah: 8, Menang: 52.9%
```

### Scenario 3: Input Validation
```
Input: 0    ➤ "Masukkan angka antara 1-10!"
Input: 11   ➤ "Masukkan angka antara 1-10!" 
Input: abc  ➤ "Masukkan angka yang valid!"
```

## ❓ FAQ

### Q: Apakah perlu install library tambahan?
**A:** Tidak! Game ini menggunakan pure Python standard library saja.

### Q: Bagaimana cara reset semua statistik?
**A:** Hapus file `history_tebak_angka.json` dan restart aplikasi.

### Q: Bisakah diubah range angkanya?
**A:** Bisa! Edit di `game_logic.py` pada method `reset_game()`.

### Q: Apakah data tersimpan setelah aplikasi ditutup?
**A:** Ya! Semua data otomatis tersimpan di file JSON.

### Q: Bagaimana cara backup data permainan?
**A:** Backup file `history_tebak_angka.json` ke lokasi aman.

### Q: Bisakah dimainkan oleh beberapa pemain?
**A:** Saat ini single player, tapi bisa dikembangkan untuk multi-player.

### Q: Apakah support high scores?
**A:** Ya! Sistem statistik sudah mencatat semua history permainan.

## 🐛 Troubleshooting

### Common Issues

1. **Tkinter tidak terinstall**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3-tk
   
   # Windows (biasanya sudah included)
   ```

2. **File permission error**
   - Pastikan folder writable
   - Run sebagai administrator jika perlu

3. **JSON corruption**
   - Delete file `history_tebak_angka.json`
   - Aplikasi akan buat file baru


<div align="center">

## 🎯 Ready to Play?

**Mulai petualangan tebak angka Anda sekarang!**

```bash
python main.py
```

**⭐ Jangan lupa beri bintang jika Anda menyukai game ini! ⭐**

[Kembali ke Atas](#-permainan-tebak-angka)

</div>