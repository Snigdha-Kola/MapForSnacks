from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
vending_machines = [
    {'id': 1, 'location': 'Building 1', 'items': ['Soda','Candy','Vegan Snacks']},
    {'id': 2, 'location': 'Building 2', 'items': ['Seltzer Drinks','Water','Snacks']}
]

# Home page route
@app.route('/home')

def home():
    return "<h1>Welcome to the Vending Machine API!"

# Use /api/vending-machines' to get the data
@app.route('/api/vending-machines', methods=['GET'])

def get_vending_machines():
    return jsonify(vending_machines)

# Use /api/vending-machines/<item> to get the filtered data
@app.route('/api/vending-machines/filter/<item>', methods=['GET'])

def filter_vending_machines(item):
    filtered_lst= [] 
    for vending_machine in vending_machines:
        for i in vending_machine['items']:
            if item.lower() == i.lower():
                filtered_lst.append(vending_machine) 
                break
    return jsonify(filtered_lst)

if __name__ == '__main__':
    app.run(debug=True)