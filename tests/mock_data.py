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


@pytest.fixture
def employee():
    data = {
        'firstname' : 'John',
        'lastname' : 'Smith',
        'dob' : '03/01/2000',
        'gender' : 'male',
        'address' : '120 Kensington',
        'postcode' : 'K1 1QP',
        'phoneNumber' : '020 1111 1111',
        'email' : 'asmith@hotmail.com'
    }
    return data


@pytest.fixture
def trainer():
    data = {
        'position' : 'Trainer',
        'salary' : 40000,
        'seniority' : 'Level 3'
    }
    return data