# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
import pytest

@pytest.fixture
def customer():
    data = {
        'id' : '507f191e810c19729de860ea',
        'firstname' : 'Andrew',
        'lastname' : 'Smith',
        'dob' : '03/01/2004',
        'gender' : 'male',
        'address' : '120 Kensington',
        'postcode' : 'K1 2QP',
        'phoneNumber' : '020 1111 3212',
        'email' : 'asmith@hotmail.com'
    }
    return data