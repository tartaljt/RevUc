import json
from flask import Flask, jsonify, request


providers = [{'specialty': 'Physician', 
              'name': 'Dr. ABC', 
              'email': 'email@mail.com', 
              'phone': '123-123-1234'}]

def get_provider():
    return jsonify(providers)

def get_provider_by_type(type):
    doc = get_provider(type)
    if doc is None:
        return jsonify({'error': 'Provider does not exist'}), 404
    return jsonify(doc)

def get_provider_by_name(name):
    doc = get_provider(name)
    if doc is None:
        return jsonify({'error': 'Provider does not exist'}), 404
    return jsonify(doc) 

def get_provider(type):
    return next((e for e in providers if e['specialty'] == type), None)

def get_provider(name):
    return next((e for e in providers if e['name'] == name), None)

def name_is_valid(doc):
    for key in doc.keys():
        if key != 'name':
            return False
        return True
    

#figure out how to implement
def email_is_valid(doc):
    for key in doc.keys():
        if key != 'email':
            return False
    
    
def phone_is_valid(doc):
    for key in doc.keys():
        if key != 'phone':
            return False
        return True
    
def create_provider():

    doc = json.loads(request.data)
    if not name_is_valid(doc):
        return jsonify({'error': 'Invalid provider properties.'}), 400
    
    if not email_is_valid(doc):
        return jsonify({'error': 'Invalid provider email.'})
    
    if not phone_is_valid(doc):
        return jsonify({'error': 'Invalid provider phone number.'}), 400
    
    providers.append(doc)

    return '', 201, {'location': f'/providers/{doc["name"]}'}

def update_provider(name):
    doc = get_provider_by_name(name)
    if doc is None:
        return jsonify({'error': 'Provider does not exist.'}), 404
    
    update_doc = json.loads(request.data)
    if not name_is_valid(doc):
        return jsonify({'error': 'Invalid provider properties.'}), 400
    
    if not email_is_valid(doc):
        return jsonify({'error': 'Invalid provider email.'})
    
    if not phone_is_valid(doc):
        return jsonify({'error': 'Invalid provider phone number.'}), 400
    
    doc.update(update_doc)

    return jsonify(doc)

def delete_provider(name):
    global providers
    doc = get_provider_by_name(name)
    if doc is None:
        return jsonify({'error': 'Provider does not exist.'}), 404
    
    providers = [e for e in providers if e['name'] != name]
    return jsonify(doc), 200
