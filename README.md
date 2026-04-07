# Hungry in the Dark

Game arcade sederhana berbasis Python dan Pygame. Pemain harus mengumpulkan item, bertahan dari ghost yang mengejar, dan naik level setiap kali semua item berhasil diambil. Game ini memakai sistem menu, game over, skor, level, serta pathfinding BFS untuk pergerakan ghost.

## Fitur

- Menu awal dengan tombol Start Game dan Exit
- Ghost mengejar pemain menggunakan BFS pathfinding
- Sistem skor dan level
- Item berubah antara apple dan banana saat level naik
- Efek suara, musik latar, dan screen shake saat pemain terkena ghost
- Game over menu dengan opsi main lagi atau keluar

## Teknologi

- Python
- Pygame

## Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Install dependency Pygame:

```bash
pip install pygame
```

3. Jalankan game dari folder proyek:

```bash
python main.py
```

## Kontrol

- Tombol arah: bergerak ke atas, bawah, kiri, kanan
- Enter: memilih menu
- Mouse: klik tombol menu
- Close window: keluar dari game

## Alur Permainan

1. Game dimulai dari menu utama.
2. Pemain muncul di dekat pintu rumah.
3. Pemain mengambil item di map untuk menambah skor.
4. Saat semua item habis, level naik dan item baru muncul.
5. Setiap level baru menambah ghost yang ikut mengejar pemain.
6. Jika pemain menyentuh ghost, game over.

## Struktur Proyek

```text
.
├── app/
├── assets/
├── config.py
├── gameover_menu.py
├── ghost.py
├── hero.py
├── main.py
├── maze.py
├── menu.py
├── pathfinding.py
├── README.md
└── score.py
```

## Catatan Teknis

- `maze.py` menyimpan layout map dan objek visual seperti tree dan house.
- `hero.py` menangani pergerakan pemain dan deteksi tabrakan.
- `ghost.py` menggerakkan ghost menuju pemain.
- `score.py` mengatur item, skor, dan level progression.
- `menu.py` dan `gameover_menu.py` menangani tampilan menu.

## Arsitektur OOP

- `Entity` di `config.py` berperan sebagai class induk.
- `Player` di `hero.py` mewarisi `Entity` (`class Player(Entity)`).
- `Ghost` di `ghost.py` mewarisi `Entity` (`class Ghost(Entity)`).
- `Item` dan `ScoreSystem` di `score.py` saat ini berdiri sendiri (tidak mewarisi class lain).

## Kebutuhan

- Python 3
- Pygame

## Pengembangan Berikutnya

- Menambah lebih banyak level dan variasi map
- Menambah sound effect untuk aksi tertentu
- Menambah sistem nyawa
- Membuat AI ghost lebih agresif atau adaptif

## Lisensi

Proyek ini dibuat untuk pembelajaran dan pengembangan game sederhana dengan Python.
