\# ⚽ Football League Simulator



A modular Python project that simulates a mini football league with teams, players, matches, and statistics.



\---



\## 📁 Project Structure



```

.

├── main.py            # Entry point — loads data and launches the menu

├── data\_manager.py    # Loads players/teams from files and calculates team power

├── match\_engine.py    # Handles match logic, scoring, and winner determination

├── statistics.py      # Tracks top scorers and updates match statistics

├── ui.py              # Displays the main menu and handles user input

├── players.txt        # Player data (name, team, power, goals)

└── teams.txt          # Team data (name, players, power, wins, losses, draws)

```



\---



\## 👥 Teams \& Players



The league has \*\*4 teams\*\*, each with \*\*5 players\*\*:



| Team    | Players                                      |

|---------|----------------------------------------------|

| Phoenix | Ali, Reza, Armin, Navid, Sina                |

| Titans  | Amir, Milad, Kian, Yasin, Erfan              |

| Dragons | Parsa, Mahdi, Pouya, Nima, Omid              |

| Wolves  | Arya, Shayan, Mohammad, Ashkan, Saman        |



Each player has a \*\*power rating\*\* (69–92) that contributes to their team's overall strength.



\---



\## 🧩 Modules



\### `data\_manager.py`

\- `load\_players(path)` — reads `players.txt` and returns a list of player dictionaries

\- `load\_teams(path)` — reads `teams.txt` and returns a list of team dictionaries

\- `calculate\_team\_power(teams, players)` — sums up player power ratings per team and updates each team's power field



\### `match\_engine.py`

\- `play\_match()` — runs a match between two teams \*(Phase 2)\*

\- `calculate\_win\_probability()` — computes win odds based on team power \*(Phase 2)\*

\- `determine\_match\_winner()` — decides the result \*(Phase 2)\*

\- `generate\_match\_score()` — produces a realistic scoreline \*(Phase 2)\*

\- `select\_goal\_scorers()` — picks which players scored \*(Phase 2)\*



\### `statistics.py`

\- `get\_top\_scorer()` — returns the player with the most goals \*(Phase 2)\*

\- `update\_statistics()` — updates win/loss/draw records after a match \*(Phase 2)\*



\### `ui.py`

\- `show\_main\_menu(options)` — prints the main menu and captures the user's choice



\---



\## ▶️ How to Run



```bash

python main.py

```



Make sure `players.txt` and `teams.txt` are in the same directory as `main.py`.



\---



\## 📋 Menu Options



```

1 : Display teams information

2 : Display players information

3 : Play a match

4 : Top scorer

5 : Exit

```



\---



\## 🗺️ Development Phases



| Phase | Status | Description |

|-------|--------|-------------|

| Phase 1 | ✅ Done | Project structure, data loading, team power calculation, UI skeleton |

| Phase 2 | 🔄 In Progress | Match simulation, statistics, full menu functionality |



\---



\## 👨‍💻 Contributors



| Module         | Owner             |

|----------------|-------------------|

| `data\_manager` | Amirali Khajouei  |

| `match\_engine` | Radin Rezazadeh   |

| `statistics`   | MZAZ              |

| `ui`           | Parsa Bagheri     |



\---



\## 📄 Data Format



\*\*players.txt\*\* — one player per line, comma-separated key:value pairs:

```

name:Ali,team:Phoenix,power:92,goals:0

```



\*\*teams.txt\*\* — one team per line:

```

name:Phoenix,players:\[Ali|Reza|Armin|Navid|Sina],power:None,wins:0,loses:0,draws:0

```

