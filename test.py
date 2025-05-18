import requests

url = 'http://127.0.0.1:3500'

# Test: Roll initial stats
print("=== Rolling Initial Stats ===")
response = requests.post(f'{url}/roll_stats')
initial_stats = response.json()
print(initial_stats)

# Test: Reroll stat at index 2
print("\n=== Reroll Stat at Index 2 ===")
reroll_request = {
    "stat_values": initial_stats["stat_values"],
    "index": 2
}
response = requests.post(f'{url}/reroll_stat', json=reroll_request)
updated_stats = response.json()
print(updated_stats)

# Test: Generic dice roll
print("\n=== Generic Dice Roll ===")
response = requests.post(f'{url}/roll_dice')
single_dice_roll = response.json()
print(single_dice_roll)
