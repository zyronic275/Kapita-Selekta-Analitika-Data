# Panduan Sederhana: GitHub dengan Visual Studio Code

Dokumen ini menjelaskan alur kerja dasar mulai dari membuat repository di GitHub, menghubungkannya ke VS Code, hingga mengirim perubahan kembali ke GitHub.

---

## Bagian 1: Membuat Repository di GitHub

Langkah pertama adalah menyiapkan "wadah" untuk proyek Anda di situs GitHub.

1.  **Login ke Akun GitHub Anda.** Buka `github.com`.
2.  **Buat Repository Baru.** Klik ikon `+` di pojok kanan atas, lalu pilih **New repository**.
3.  **Isi Detail Repository:**
    * **Repository name:** Beri nama yang singkat dan jelas untuk proyek Anda (misalnya, `latihan-git`).
    * **Description (optional):** Beri deskripsi singkat tentang proyek Anda.
    * Pilih **Public** agar bisa dilihat semua orang, atau **Private** jika hanya untuk Anda.
    * **Sangat disarankan:** Centang kotak **Add a README file**. Ini akan memudahkan proses selanjutnya.
4.  **Selesaikan.** Klik tombol hijau **Create repository**.
5.  **Salin URL Repository.** Setelah repository dibuat, klik tombol hijau **<> Code**. Di bawah tab **HTTPS**, salin URL yang tersedia. URL ini akan kita gunakan di VS Code.

---

## Bagian 2: Menghubungkan Repository ke VS Code

Sekarang kita akan mengambil repository dari GitHub dan membukanya di komputer lokal menggunakan VS Code. Proses ini disebut *cloning*.

1.  **Buka VS Code.**
2.  **Buka Command Palette.** Tekan `Ctrl+Shift+P` (atau `Cmd+Shift+P` di Mac).
3.  **Pilih Git: Clone.** Ketik `Git: Clone` di Command Palette dan tekan Enter.
4.  **Tempel (Paste) URL.** Masukkan URL repository yang sudah Anda salin dari GitHub, lalu tekan Enter.
5.  **Pilih Lokasi Folder.** VS Code akan meminta Anda memilih folder di komputer untuk menyimpan salinan proyek ini. Pilih lokasi yang Anda inginkan.
6.  **Buka Repository.** Setelah proses *cloning* selesai, VS Code akan menampilkan notifikasi di pojok kanan bawah. Klik **Open** untuk membuka folder proyek tersebut.

Sekarang, proyek Anda dari GitHub sudah ada di komputer lokal dan terbuka di VS Code.

---

## Bagian 3: Membuat dan Menerapkan Perubahan

Ini adalah siklus kerja yang akan sering Anda lakukan: membuat perubahan, menyimpannya secara lokal (commit), dan mengirimkannya ke GitHub (push).

1.  **Buat Perubahan pada File.** Buka salah satu file (misalnya `README.md`) dan tambahkan atau ubah beberapa baris teks. Simpan file tersebut (`Ctrl+S`).
2.  **Buka Tab Source Control.** Di panel sebelah kiri VS Code, klik ikon yang terlihat seperti percabangan jalan (biasanya ikon ketiga dari atas). Di sini Anda bisa melihat semua file yang telah diubah.
3.  **Stage Perubahan.** Di bawah judul "Changes", Anda akan melihat file yang baru saja Anda ubah. Arahkan kursor ke nama file dan klik ikon `+` (Stage Changes). Ini memberitahu Git bahwa Anda ingin menyertakan perubahan ini dalam simpanan (commit) berikutnya.
4.  **Buat Pesan Commit.** Di bagian atas panel Source Control, ada kotak teks. Tulis pesan yang menjelaskan perubahan yang Anda buat (misalnya, "Memperbarui deskripsi pada README"). Pesan ini berfungsi sebagai catatan.
5.  **Commit Perubahan.** Klik ikon centang (✓) di atas kotak pesan untuk menyimpan perubahan tersebut secara lokal di riwayat Git Anda.
6.  **Push ke GitHub.** Setelah melakukan *commit*, tombol biru di bagian bawah kiri (status bar) akan berubah menjadi **Sync Changes** (biasanya dengan ikon awan/panah). Klik tombol tersebut untuk mengirim semua *commit* yang sudah Anda simpan ke repository di GitHub.

Selesai! Sekarang jika Anda membuka kembali halaman repository Anda di situs GitHub dan me-refresh halaman, Anda akan melihat perubahan yang baru saja Anda kirim dari VS Code.