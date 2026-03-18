# Graph Reachability with Fuel Constraints

A Python solution for determining whether a directed walk exists from a source vertex `s` to a target vertex `t` in a directed graph, subject to fuel capacity constraints and mid-path refill stations.

## Problem

Given a directed graph G = (V, E) where:
- Each edge has a nonnegative integer fuel cost `c(e)`
- Each vertex has a binary flag `r(v)` indicating whether it provides a full fuel refill
- You start at source `s` with a full tank of capacity `F`

Determine if a valid directed walk from `s` to `t` exists without running out of fuel.

## Approach

Uses a max-heap (modified Dijkstra) that tracks the **maximum remaining fuel** upon arriving at each vertex. A refill vertex instantly restores fuel to `F`. If the target `t` is ever popped from the heap, the answer is `True`.

## Usage

```bash
python main.py
```

Runs three built-in test cases and prints results to stdout.

## Function Reference

**`canReachTarget(numCities, cityConnections, chargingStations, startCity, targetCity, maxBattery)`**
Returns `True` if `t` is reachable from `s` under fuel constraints, `False` otherwise.

**`buildMap(numCities, roads)`**
Builds an adjacency list from a list of `(u, v, cost)` edge tuples.

## Test Cases

| Test | Scenario | Expected |
|------|----------|----------|
| 1 | Sufficient fuel, no refills needed | `True` |
| 2 | Reachable only via a refill vertex | `True` |
| 3 | First edge cost exceeds tank capacity `F` | `False` |

## Complexity

- **Time:** O((n + m) log n)
- **Space:** O(n + m)

## Requirements

Python 3.x — no external dependencies.