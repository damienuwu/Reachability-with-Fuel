# EV Routing Simulation

A Python implementation of an electric vehicle routing algorithm that determines whether an EV can travel between two cities on a road network, given battery constraints and the availability of charging stations along the way.

---

## 🚗 Problem Overview

Given a directed road network, a starting city, a target city, and a maximum battery capacity, this algorithm finds whether a valid route exists where:

- Each road segment consumes a fixed amount of battery.
- The vehicle **cannot** traverse a road if it lacks sufficient charge.
- Certain cities have **charging stations** that instantly refill the battery to full capacity upon arrival.

---

## ⚙️ Algorithm

The solution uses a **modified Dijkstra's algorithm** with a max-heap priority queue, optimizing for **maximum remaining battery** rather than minimum cost.

### Key Design Decisions

| Concept | Detail |
|---|---|
| **Priority Queue** | Max-heap (simulated via negative values in Python's `heapq`) |
| **State Tracking** | `bestBatteryLevel[i]` — the highest battery level ever achieved on arrival at city `i` |
| **Pruning** | Paths arriving at a city with less battery than a previously recorded visit are discarded |
| **Charging** | If a city is in `chargingStations`, battery resets to `maxBattery` upon arrival |

### Complexity

- **Time:** `O((V + E) log V)` where `V` = number of cities, `E` = number of roads
- **Space:** `O(V + E)` for the adjacency list and state array

---

## 📁 Project Structure

```
ev-routing/
├── solution.py       # Core algorithm + test runner
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- No external dependencies (uses only the standard library `heapq`)

### Run the Tests

```bash
python solution.py
```

---

## 🧪 Test Cases

Three built-in scenarios validate the core logic:

### Test 1 — Reachable without charging

```
Cities: 1 → 2 → 3   |   Road costs: 2, 2   |   Max battery: 5   |   Chargers: none
Expected: True
```

The vehicle has enough charge to complete the journey without stopping.

### Test 2 — Reachable only via charging station

```
Cities: 1 → 2 → 3   |   Road costs: 4, 4   |   Max battery: 5   |   Chargers: {2}
Expected: True
```

The vehicle barely reaches city 2 (1 unit remaining), recharges to full, then completes the trip.

### Test 3 — Unreachable (first road exceeds battery)

```
Cities: 1 → 2 → 3   |   Road costs: 6, 1   |   Max battery: 5   |   Chargers: {2}
Expected: False
```

The first road costs 6 units — more than the maximum battery — so the vehicle is stranded immediately.

### Sample Output

```
Running test cases for EV Routing Simulation...

Test 1 (Expected True): True
Test 2 (Expected True): True
Test 3 (Expected False): False
```

---

## 🔌 API Reference

### `canReachTarget`

```python
canReachTarget(numCities, cityConnections, chargingStations, startCity, targetCity, maxBattery) -> bool
```

| Parameter | Type | Description |
|---|---|---|
| `numCities` | `int` | Total number of cities in the network |
| `cityConnections` | `dict` | Adjacency list: `{city: [(neighbor, cost), ...]}` |
| `chargingStations` | `set` | Set of city IDs that have a charging station |
| `startCity` | `int` | Departure city |
| `targetCity` | `int` | Destination city |
| `maxBattery` | `int` | Maximum battery capacity (also the starting charge) |

Returns `True` if the target is reachable, `False` otherwise.

---

### `buildMap`

```python
buildMap(numCities, roads) -> dict
```

Helper that constructs a directed adjacency list from a flat list of road tuples.

| Parameter | Type | Description |
|---|---|---|
| `numCities` | `int` | Total number of cities |
| `roads` | `list[tuple]` | List of `(start, end, batteryCost)` tuples |

---

## 📌 Extending the Solution

Some directions to take this further:

- **Bidirectional roads** — add a reverse edge in `buildMap` for undirected graphs.
- **Partial charging** — replace the binary full-recharge with a time/cost model.
- **Multiple vehicles** — run parallel simulations with different battery profiles.
- **Visualisation** — pipe `cityConnections` into `networkx` + `matplotlib` to render the map.