 Autonomous Mission Routing & Threat Detection System

## Overview
This project simulates a mission planning system using the A* pathfinding algorithm to calculate optimal routes while avoiding threat zones in a grid-based environment.

## Key Features
- A* pathfinding algorithm implementation
- Grid-based navigation system
- Obstacle (threat zone) avoidance
- Diagonal movement with weighted costs
- Visualized routing using matplotlib

## Demo Behavior
- Without threats → straight optimal path
- With threats → path dynamically reroutes
- Larger threat zones → longer alternative paths

## Tech Stack
- Python
- Matplotlib

## How to Run
```bash
pip install matplotlib
python main.py
