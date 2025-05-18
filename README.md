# Microservice-A
This microservice provides endpoints for simulating stat generation and dice rolling in a character creation or game mechanics context. 
It is designed to support:

- Initial stat value generation

- Selective re-rolling of a stat value

- Generic dice rolls for other systems (e.g., personality traits)

# How to Request and Receive Data from the Dice Rolling Microservice

The microservice provides multiple endpoints to simulate rolling dice for game mechanics, such as generating character stats or re-rolling specific values.

How to Programmatically REQUEST Data
To request data from the dice rolling microservice, use the Python requests library. Each endpoint accepts POST requests and responds with JSON. For example:
- To roll initial character stats, send a POST request to http://127.0.0.1:5000/roll_stats
- To re-roll a single stat value, send a POST request to http://127.0.0.1:5000/reroll_stat with a JSON body containing the existing stat values and the index of the value to replace
- For a single generic dice roll, use the /roll_dice endpoint.
Example requests are shown below:

# Initial stat roll
requests.post('http://127.0.0.1:5000/roll_stats')

# Reroll a stat value at index 2
requests.post('http://127.0.0.1:5000/reroll_stat', json={
    "stat_values": [15, 12, 9, 17, 6, 13],
    "index": 2
})

# Single dice roll
requests.post('http://127.0.0.1:5000/roll_dice')
