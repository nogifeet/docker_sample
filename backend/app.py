import logging
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

host = os.environ.get('FLASK_HOST', '0.0.0.0')
port = int(os.environ.get('FLASK_PORT', 8080))

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='./logs/app.log', level=logging.INFO)

# Database configuration (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:helloWorld123@mysql-container/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)

# Create the database and tables if not present
with app.app_context():
    db.create_all()

@app.route('/store', methods=['POST'])
def store_customer():
    if request.method == 'POST':
        try:
            # Get data from the request
            data = request.get_json()
            name = data['name']
            age = data['age']
            email = data['email']
            country = data['country']

            # Create a new Customer object and add it to the database
            customer = Customer(name=name, age=age, email=email, country=country)
            db.session.add(customer)
            db.session.commit()

            # Log the incoming request and the response
            logging.info(f'Incoming request: POST /store - Data: {data}')
            logging.info('Response: Customer data stored successfully')

            return jsonify({'message': 'Customer data stored successfully'}), 201
        except Exception as e:
            logging.error(f'Error while processing request: {str(e)}')
            return jsonify({'error': str(e)}), 400

@app.route('/customers', methods=['GET'])
def get_customers():
    if request.method == 'GET':
        try:
            # Retrieve all customer data from the database
            customers = Customer.query.all()

            # Convert the result to a list of dictionaries
            customer_list = []
            for customer in customers:
                customer_dict = {
                    'id': customer.id,
                    'name': customer.name,
                    'age': customer.age,
                    'email': customer.email,
                    'country': customer.country
                }
                customer_list.append(customer_dict)

            # Log the incoming request and the response
            logging.info(f'Incoming request: GET /customers')
            logging.info(f'Response: {customer_list}')

            return jsonify({'customers': customer_list})
        except Exception as e:
            logging.error(f'Error while processing request: {str(e)}')
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app with a hardcoded host and port
    app.run(host=host, port=port)
