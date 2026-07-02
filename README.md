# Galactic Chronicles: Algorithmic Problem-Solving Suite

Seven algorithmic solutions to a spacecraft navigation and resource-management scenario, built for **WIA2005 Algorithm Design and Analysis** at Universiti Malaya (Faculty of Computer Science and Information Technology).

Each part maps a story beat from a space-opera narrative onto a real algorithmic problem: pathfinding, filtering, probabilistic search, shortest paths, multi-constraint optimization, weighted scheduling, and cipher decryption.

## Overview

| Part | Problem | Algorithm(s) Used | Time Complexity |
|------|---------|-------------------|------------------|
| 1 | Asteroid Labyrinth — safe pathfinding through a debris field | Grid-based density analysis + BFS | O(n + m) |
| 2 | Market of Moira — filter and rank upgrade items | Brute-force filtering + Merge Sort | O(n log n) |
| 3 | Stowaway Protocol — probabilistic compartment search | Weighted likelihood scoring + sort | O(n log n) |
| 4 | Broken Stargate — shortest/safest route between gates | Modified Dijkstra (multi-criteria cost) | O(n²) |
| 5 | AI Override — select systems to restore under dual constraints | 2D Bounded Knapsack (Dynamic Programming) | O(n · P · T) |
| 6 | Ores Negotiation — maximize priority of non-overlapping dockings | Weighted Interval Scheduling (DP + binary search) | O(n log n) |
| 7 | Echoes of the Ancients — decode an encrypted signal | Brute-force Caesar cipher | O(n) |

## Tech Stack

- Python 3
- pandas, NumPy
- matplotlib (visualizations)
- heapq (priority queue for Dijkstra)
- Google Colab (development environment)

## Repository Structure

```
├── part1_asteroid_labyrinth/
|   ├── asteroid_pathfinding.py
│   ├── sample_output.png
│   └── Asteroid_Field_Data.csv
├── part2_market_of_moira/
│   ├── market_filter_sort.py
│   └── Moira_Market_Items.csv
├── part3_stowaway_protocol/
│   ├── stowaway_search.py
│   └── Compartment_Sensor_Data.csv
├── part4_broken_stargate/
│   ├── stargate_dijkstra.py
│   └── Stargate_Data.csv
├── part5_ai_override/
│   ├── ai_override_knapsack.py
│   └── AI_Override_System_Data.csv
├── part6_ores_negotiation/
│   ├── docking_scheduler.py
│   └── Docking_Requests_Dataset.csv
├── part7_echoes_of_ancients/
│   └── caesar_decode.py
├── requirements.txt
└── README.md
```

## My Contribution

I was individually responsible for **Part 1: The Asteroid Labyrinth**, combining grid-based density analysis with BFS to chart a safe navigation path through 300 simulated asteroids. Problem breakdown, pseudocode, and complexity analysis for this part are documented in the code comments and the section below.

The remaining parts were completed by teammates as part of a 6-person group project. Each folder here focuses on the algorithm and implementation rather than reproducing the full academic report, to keep the repository focused on code.

## Running the Code

```bash
pip install -r requirements.txt
python part1_asteroid_labyrinth/asteroid_pathfinding.py
```

Each part is self-contained and expects its corresponding CSV in the same folder.

## Team

Developed by Group 8 (Occurrence 2), WIA2005 Algorithm Design and Analysis, supervised by Dr. Uzair Iqbal, Faculty of Computer Science and Information Technology, Universiti Malaya.

| Member | Part(s) |
|--------|---------|
| Dennis Aimin Oon bin Jeffrey Oon (Me) | Part 1 — The Asteroid Labyrinth |
| Athiya Fahirah binti Ahmad Nafrawi | Part 2 — Market of Moira |
| Hani Nur 'Ain binti Norhazlan | Part 3 — The Stowaway Protocol |
| Yoonseo Han | Part 4 — The Broken Stargate |
| Mohammad Faris Ikhwan bin Jalali | Part 5 — AI Override |
| Muhammad Imran bin Ilias | Part 6 — The Ores Negotiation, Part 7 — Echoes of the Ancients |

## References

- GeeksforGeeks — BFS, Merge Sort, Dijkstra's Algorithm, Weighted Job Scheduling, Caesar Cipher
- pandas documentation — filtering and sorting DataFrames
- [Number of Trials to First Success](https://www.cut-the-knot.org/Probability/LengthToFirstSuccess.shtml)

## License

MIT
