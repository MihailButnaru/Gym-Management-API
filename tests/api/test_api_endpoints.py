# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Tests ensure endpoints implementation is working as expected, it 
will return the correct response code and response data based
on the parameters provided.
"""
from tests.mock_data import customer, employee, trainer

############################ => CUSTOMERS TESTS <= #############################

def test_get_customers(client):
    """
    Test ensures that the customers endpoint is working
    and the status must return the correct code
    """
    response = client.get('api/v1/customers')
    assert response.status_code == 200

def test_post_customer(client, customer):
    """
    Test ensures that creating a customer is
    successful and the data is stored in mongo
    database.
        Args: customer (dict) : customer data
    """
    response = client.post('api/v1/customers', json=customer)
    assert response.status_code == 201
    assert response.json['firstname'] == customer['firstname']
    assert response.json['address'] == customer['address']
    assert response.json == customer


def test_get_customer(client, customer):
    """
    Test ensures that details of the customer based on 
    customer id are correct.
        Args: customer (dict) : customer data
    """
    # Create a client
    response = client.post('api/v1/customers', json=customer)

    # Get the specific details based on the client unique id
    client_details = client.get('api/v1/customers/{}'.format(response.json['id']))
    assert client_details.status_code == 200
    assert client_details.json[0]['firstname'] == customer['firstname']
    assert client_details.json[0]['lastname'] == customer['lastname']
    assert client_details.json[0]['address'] == customer['address']


def test_edit_customer(client, customer):
    """
    Test ensures that details of the customer
    are edited successful and the new data is
    saved in mongo database
    """
    response = client.post('api/v1/customers', json=customer)

    # Customer name changed to George
    customer['firstname'] = 'George'
    client_details = client.put('api/v1/customers/{}'.format(response.json['id']),
            json=customer)
    
    assert client_details.status_code == 200
    assert client_details.json[0]['firstname'] == customer['firstname']


def test_delete_customer(client, customer):
    """
    Test ensures that a customer is deleted
    """
    # Creates a new customer
    response = client.post('api/v1/customers', json=customer)
    client_details = client.delete('api/v1/customers/{}'.format(response.json['id']))

    assert client_details.status_code == 200


############################ => EMPLOYEE TESTS <= #############################

def test_get_employees(client):
    """
    Test ensures that the employees endpoint is working
    and the status must return the correct code
    """
    response = client.get('api/v1/employees')
    assert response.status_code == 200


def test_post_employee(client, employee):
    """
    Test ensures that creating a employee is successful
    and the data is stored in mongo database.
        Args:
            employee (dict): employee data
    """
    response = client.post('api/v1/employees', json=employee)
    assert response.status_code == 201
    assert response.json['firstname'] == employee['firstname']
    assert response.json['address'] == employee['address']


def test_get_employee(client, employee):
    """
    Test ensures the details of the employee based on
    employee id are correct.
        Args:
            employee (dict) : employee data
    """
    # Create an employee
    response = client.post('api/v1/employees', json=employee)

    # Get the specific details based on employee unique id
    employee_details = client.get('api/v1/employees/{}'.format(response.json['id']))

    assert employee_details.status_code == 200
    assert employee_details.json[0]['firstname'] == employee['firstname']
    assert employee_details.json[0]['lastname'] == employee['lastname']


def test_edit_employee(client, employee):
    """
    Test ensures the details of the employee are edited
    successful and the new data is saved in mongo database.
    """
    response = client.post('api/v1/employees', json=employee)

    # Employee name changed to George
    employee['firstname'] = 'George'
    employee_details = client.put('api/v1/employees/{}'.format(
        response.json['id']), json=employee)

    assert employee_details.status_code == 200
    assert employee_details.json[0]['firstname'] == employee['firstname']


def test_delete_employee(client, employee):
    """
    Test ensures that an employee is deleted
    """
    # Create an employee
    response = client.post('api/v1/employees', json=employee)

    # Delete the employee created
    employee_details = client.delete('api/v1/employees/{}'.format(
        response.json['id']))

    assert employee_details.status_code == 200


############################ => TRAINER TESTS <= #############################

def test_get_trainers(client):
    """
    Test ensures that the trainer endpoint is working
    and the status must return the correct code
    """
    response = client.get('api/v1/trainers')
    assert response.status_code == 200


def test_post_trainer(client, trainer):
    """
    Test ensures that creating a new trainer
    is successful and the data is stored in mongo database
    """
    response = client.post('api/v1/trainers', json=trainer)
    assert response.status_code == 201
    assert response.json['position'] == trainer['position']


def test_get_trainer(client, trainer):
    """
    Test ensures that getting a specific trainer based on the ID
    is sucessful
    """
    response = client.post('api/v1/trainers', json=trainer)

    trainer_details = client.get('api/v1/trainers/{}'.format(response.json['id']))

    assert trainer_details.status_code == 200
    assert trainer_details.json[0]['position'] == trainer['position']

def test_delete_trainer(client, trainer):
    """
    Test ensures that a trainer with specific id is deleted
    """
    response = client.post('api/v1/trainers', json=trainer)

    trainer_details = client.delete('api/v1/trainers/{}'.format(response.json['id']))

    assert trainer_details.status_code == 200


def test_edit_trainer(client, trainer):
    """
    Test ensures trainers details are edited based on the id
    """
    response = client.post('api/v1/trainers', json=trainer)

    trainer['posiiton'] = 'New Position'

    trainer_details = client.put('api/v1/trainers/{}'.format(response.json['id']),
            json=trainer)

    assert trainer_details.status_code == 200