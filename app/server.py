from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# retrieve recs from pkl
model_path = os.path.join(os.path.dirname(__file__), '../scr/recommendations.pkl')
with open(model_path, 'rb') as file:
    recs_pop = pickle.load(file)

valid_user_ids = range(1, 205177)

# define response for GET
@app.route('/predict', methods=['GET'])
def predict():

    user_id = request.args.get('user_id')
    k = int(request.args.get('k', 10))  # default to 10

    #check for valid user_id
    if user_id.isdigit() and int(user_id) in valid_user_ids:

        user_recommendations = recs_pop[:k]
        response = {
            'user_id': user_id,
            'items': user_recommendations
        }

        return jsonify(response)
    else:
        return 'Invalid user_id, please enter integer values from 1 to 205176'

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')

