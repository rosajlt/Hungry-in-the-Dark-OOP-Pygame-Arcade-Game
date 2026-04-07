from collections import deque

def bfs_path(start, goal, maze): # FUNGSI BFS UNTUK MENCARI PATH DARI START KE GOAL DI MAZE
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([start]) # queue untuk menyimpan tile yang akan dieksplorasi, diinisialisasi dengan tile start
    visited = set([start]) # set untuk menyimpan tile yang sudah dikunjungi, diinisialisasi dengan tile start
    parent = {}

    directions = [(1,0), (-1,0), (0,1), (0,-1)] # arah gerak: kanan, kiri, bawah, atas

    while queue:
        x, y = queue.popleft() # ambil tile pertama dari queue untuk dieksplorasi

        if (x, y) == goal:
            break

        for dx, dy in directions: # cek keempat arah dari tile saat ini
            nx, ny = x + dx, y + dy

            if 0 <= nx < cols and 0 <= ny < rows: # cek batas maze
                if maze[ny][nx] == 0 and (nx, ny) not in visited: #cek 0 bukan tembok dan belum dikunjungi
                    queue.append((nx, ny)) 
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    if goal not in parent: #
        return []

    path = []
    cur = goal # mulai dari goal, telusuri parent sampai ke start untuk membentuk path yang benar

    while cur != start: # tambahkan tile ke path, lalu lanjut ke parent tile tersebut
        path.append(cur)
        cur = parent[cur]

    path.reverse() # balik path karena tadi dibentuk dari goal ke start, sekarang jadi start ke goal
    return path