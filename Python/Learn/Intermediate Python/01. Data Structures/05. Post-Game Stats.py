players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    {"name": "Isiah Pacheco", "position": "Running Back", "jersey_number": 10 , "yards_gained": 1765, "touchdowns": 12},
    {"name": "Noah Grey", "position": "Tight End", "jersey_number": 83, "yards_gained": 640, "touchdowns": 4},
]

names = [player["name"]for player in players_data]
print("Players Names:", names)

positions = [player["position"] for player in players_data]
print("Player Positions:", positions)

players_data[0]["yards_gained"] += 50
players_data[0]["touchdowns"] += 1

average_yards = sum(player["yards_gained"] for player in players_data) / len(players_data)
average_touchdowns = sum(player["touchdowns"] for player in players_data) / len(players_data)
print("Average Yards Gained:", average_yards)
print("Average Touchdowns:", average_touchdowns)