# Quynh Le 27537272
# Project 3
import json
import urllib.request
import urllib.parse

API_KEY = 'F6U1Lu2NLhX9PsbsneSAh4vwLZ2dJcfk'
MAP_BASE_URL = 'http://open.mapquestapi.com' 

def direction_url(locations: list) -> str:
    '''creates the direction url'''
    query_parameters = [
        ('key', API_KEY), ('from', locations[0])
        ]   
    for location in locations[1:]:
        query_parameters.append(('to', location))

    return MAP_BASE_URL + '/directions/v2/route?' + urllib.parse.urlencode(query_parameters)

def elevation_url(latlng:list) -> str:
    '''creates the elevation url'''
    result = ''
    query_parameters = [
        ('key', API_KEY), ('shapeFormat', 'raw') ,('unit', 'f')]
    for l in latlng[:-1]:
        result = result + str(l) + ','
        
    new_result = result + str(latlng[-1])
    query_parameters.append(('latLngCollection', new_result))
    return MAP_BASE_URL + '/elevation/v1/profile?' + urllib.parse.urlencode(query_parameters)

def get_response(url: str) -> dict:
    '''takes the URL and returns a Python dictionary representing the
    parsed JSON response'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode (encoding = 'utf8')
        return json.loads(json_text)
    
    except urllib.error.HTTPError as e:
        print('MAPQUEST ERROR')
        print()

    finally:
        if response != None:
            response.close()
