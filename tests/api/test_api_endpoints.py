# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Tests ensure endpoints implementation is working as expected, it 
will return the correct response code and response data based
on the parameters provided.
"""
from tests.mock_data import customer

############################ => CUSTOMERS <= #############################

def test_get_customers(client):
    """
    Test ensures that the customers endpoint is working
    and the status must return the correct code
    """
    response = client.get('api/v1/customers')
    assert response.status_code == 200

def test_post_customer(client, customer):
    """
    Test ensure that a customer is created and
    stored in the mongo database
    """
    response = client.post('api/v1/customers', json=customer)
    assert response.status_code == 201
    assert response.json['firstname'] == customer['firstname']
    assert response.json['address'] == customer['address']
    assert response.json == customer


def test_get_customer(client, customer):
    """
    Test ensure that details of the customer are correct
    if the specified id is passed as a parameter
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
    Test ensure that customers details could be edit
    and the new details are saved in mongo database
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
