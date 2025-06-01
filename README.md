# Microservice-A
This microservice provides endpoints for simulating stat generation and dice rolling in a character creation or game mechanics context. 
It is designed to support:

- Initial stat value generation

- Selective re-rolling of a stat value

- Generic dice rolls for other systems (e.g., personality traits)

The microservice provides multiple endpoints to simulate rolling dice for game mechanics, such as generating character stats or re-rolling specific values.

# How to Access and Run the Microservice
1. Download the zipped code archive to your computer, extract its contents, and move the files to your preferred coding directory. Alternatively, you can copy the microservice_a.py and the test.py scripts directly into your preferred code editor. 
2. Ensure you have Python 3.x installed on your system (by running python --version in console or an equivalent thereof).
3. Install the Flask dependency by using pip install flask command. 
4. Run the microservice and the test program by executing python microservice_a.py and python test.py 

5. The Flask server will start at:
http://127.0.0.1:3500
The microservice must be running to accept requests.

# How to Programmatically REQUEST Data
To request data from the dice rolling microservice, use the Python requests library. Each endpoint accepts POST requests and responds with JSON. For example:
- To roll initial character stats, send a POST request to http://127.0.0.1:3500/roll_stats; no input is required 
- To re-roll a single stat value, send a POST request to http://127.0.0.1:3500/reroll_stat with a JSON body containing the existing stat values and the index of the value to replace (example input: json={
    "stat_values": [16, 11, 8, 13, 9, 15],
    "index": 2}
  )
- For a single generic dice roll, send a POST request to http://127.0.0.1:3500/roll_dice endpoint; no input is required 
# Example requests are shown below:

# Initial stat roll
response = requests.post('http://127.0.0.1:3500/roll_stats')

# Reroll a stat value at index 2
response = requests.post('http://127.0.0.1:3500/reroll_stat', json={
    "stat_values": [16, 11, 8, 13, 9, 15],
    "index": 2
})

# Single dice roll
response = requests.post('http://127.0.0.1:3500/roll_dice')

# How to Programmatically RECEIVE Data
To receive data from the microservice, access the response object from the POST request and convert it into a Python dictionary using the .json() method. This way, you can retrieve values such as the full set of stat rolls, the updated stats after a re-roll, or the result of a single die roll. Example usage is shown below:

# Get initial stat values
stats = requests.post('http://127.0.0.1:5000/roll_stats').json())

# Reroll one value in the stats list
updated_stats = requests.post('http://127.0.0.1:3500/reroll_stat', json={
    "stat_values": stats["stat_values"],
    "index": 2
}).json())

# Roll one generic die
single_roll = requests.post('http://127.0.0.1:3500/roll_dice').json())

# UML Diagram
![Microservice A UML](https://github.com/user-attachments/assets/c1af4cea-968e-42ec-afaf-fa72da8fa437)

