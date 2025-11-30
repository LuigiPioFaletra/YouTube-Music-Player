# MusicPlayerYT: YouTube-Based Music Player

This repository contains **MusicPlayerYT**, a Python-based music player that allows users to create and play playlists using YouTube links.  
The project was developed as part of the **Algorithms and Data Structures** course at the University of Enna “Kore”.

---

## Repository Structure

```
main_repository/
│
├── implementation/
│   ├── binary_tree.py
│   ├── center.py
│   ├── decision_tree.py
│   ├── double_linked_list.py
│   ├── empty.py
│   ├── file_reader.py
│   ├── hash_map_base.py
│   ├── heap.py
│   ├── linked_binary_tree.py
│   ├── linked_deque.py
│   ├── map_base.py
│   ├── positional_list.py
│   ├── priority_queue_base.py
│   ├── probe_hash_map.py
│   ├── queue1.py
│   ├── reproduction.py
│   ├── request_data.py
│   ├── shuffle_playback.py
│   ├── songs.txt
│   ├── sorted_priority_queue.py
│   ├── statistics.py
│   ├── structures_filler.py
│   ├── tk_genres.py
│   ├── tk_queue.py
│   ├── top_100.py
│   ├── tree.py
│   └── unsorted_table_map.py
│
├── description.pdf
├── README.md
└── LICENSE
```

---

## Project Overview

MusicPlayerYT allows users to:

1. **Play music by creating immediate playlists**  
   - Choose songs based on genre, personal selection, or top 100 ranking  
   - Supports random playback with priorities based on user preferences  

2. **Navigate playlists dynamically**  
   - Forward and backward song selection  
   - Pause and resume functionality  

3. **Interact through a graphical interface**  
   - Genre selection and song selection interfaces  

4. **Use multiple data structures for efficient playlist management**  
   - Positional lists, queues, priority queues, heaps, maps, hash tables, and trees

---

## Data Structures Used

- **Queue** – manages manual song navigation (forward/backward).  
- **Positional List** – stores YouTube links for easy access by position.  
- **Binary Tree / Decision Tree** – guides user interaction through yes/no questions.  
- **Priority Queue** – handles random playback based on song priority.  
- **Heap** – organizes Top 100 songs by popularity metrics.  
- **Map** – links songs to names and genres for playlist generation.  
- **Hash Table** – retrieves songs by genre efficiently.

---

## Installation & Setup

1. Install **VLC 64-bit**.  
2. Install Python dependencies:
```bash
pip install json requests youtube-dl pafy
```
3. Modify the Pafy backend:
   - In `pafy/backend_youtube_dl.py`, set `self._dislikes = 0` at line 54.

---

## Execution

From the root folder:
```bash
python implementation/decision_tree.py
```

Follow on-screen prompts to:
- Select whether to play music
- Choose songs manually, by genre, or from the Top 100
- Enable random playback
- Interact with the graphical interface

---

## Notes

- Songs are represented via YouTube links; no local downloads are required.
- Playlist creation is immediate and dynamic.
- Data structures ensure efficient management of song selection, playback order, and priority.
- Threads are used to manage concurrent operations like playback and interface updates.

---

### License

This project is licensed under the terms of the MIT license. You can find the full license in the `LICENSE` file.
