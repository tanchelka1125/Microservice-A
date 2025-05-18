from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Roll initial stats
@app.route('/roll_stats', methods=['POST'])
def roll_stats():
    """Returns 6 random stat values between 1 and 18."""
    rolls = [random.randint(1, 18) for _ in range(6)]
    return jsonify({'stat_values': rolls})


# Re-roll a specific stat value
@app.route('/reroll_stat', methods=['POST'])
def reroll_stat():
    """Rerolls one value in the list of stats based on the given index."""
    data = request.get_json()
    stats = data.get('stat_values')
    index = data.get('index')

    # Validate stat_values
    if not stats or len(stats) != 6:
        return jsonify({'error': 'stat_values must be a list of six numbers.'}), 400
    if not all(type(x) == int for x in stats):
        return jsonify({'error': 'All stat values must be integers.'}), 400

    # Validate index
    if type(index) != int or not (0 <= index < 6):
        return jsonify({'error': 'index must be an integer between 0 and 5.'}), 400

    # Perform reroll
    stats[index] = random.randint(1, 18)
    return jsonify({'updated_stat_values': stats})


# Roll a single die
@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    """Returns a single random value between 1 and 18."""
    result = random.randint(1, 18)
    return jsonify({'roll': result})


if __name__ == '__main__':
    app.run(port=3500)
