from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the API
@app.route('/')
def get_name():
    # Your logic to fetch a name can go here
    name = "John Doe"
    
    # Returning the name in JSON format
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
