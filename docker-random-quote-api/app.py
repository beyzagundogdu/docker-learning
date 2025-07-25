from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
   "Hayallerinin pesinden git.",
   "Basari sabir ister.",
   "Bugun bir adim at.",
   "Kucuk adimlar, buyuk sonuclar dogurur."
]

@app.route('/quote')
def random_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
