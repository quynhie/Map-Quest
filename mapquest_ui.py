# Quynh Le 27537272
# Project 3
import mapquest_input
import mapquest_output

API_KEY = 'F6U1Lu2NLhX9PsbsneSAh4vwLZ2dJcfk'

def num_location() -> int:
    '''asks the user for the number of location they want'''
    while True:
        try: 
            location = int(input())

            if location >=  2:
                return location
            else:
                print('Please type in a number greater than or equal to 2')            
        except ValueError:
            print('Please type in a number')

def location_names() -> list:
    '''asks the user for the names of their location(s)'''
    locations = num_location()
    location_names = []    
    for name in range(locations):
        name = input().strip()
        location_names.append(name)
    return location_names

def num_output() -> int:
    '''asks the user how many outputs they want'''
    while True:
        try:
            output = int(input())

            if output >= 1:
                return output
            else:
                print('Please type in a number greater or equal to 1')
        except ValueError:
            print('Please type in a number')

def name_output() -> list:
    '''asks the user for the names of their outputs'''
    output_names = []
    output = num_output()   
    for name in range(output):
        name = input().upper().strip()
        output_names.append(name)
    return output_names

def get_latlng_not_rounded(json:dict) -> list:
    '''grabs the unrounded latlng from the json'''
    latlng = []
    for l in json['route']['locations']:
        lng = l['latLng']['lng']
        lat = l['latLng']['lat']
        latlng.append(lat) 
        latlng.append(lng)
    return latlng

def get_elevation_urls(latlng: list) -> list:
    '''creates elevation url(s) corresponding to however many pairs of lats & lngs'''
    result = []
    for l in range(len(latlng) -1):
        if l % 2 ==0:
            elevation = [latlng[l], latlng[l+1]]
            elevation_url = mapquest_input.elevation_url(elevation)
            result.append(elevation_url)
    return result        

def get_elevation_jsons(elevation_urls: list) -> [dict]:
     '''takes a list of elevation URLs and returns a list of
        Python dictionary representing theparsed JSON response'''
     json = []
     for elevation_url in elevation_urls:
        json.append((mapquest_input.get_response(elevation_url)))
     return json 
     
def route_check(json: dict)-> bool:
    '''checks to see if the route is found; returns True if it is not found & False if is.'''
    for x in json['info']['messages']:
        if x =='We are unable to route with the given locations.':
            return True
        else:
            return False
        
def output_generator(outputs: list, json: dict) -> None:
    '''generates the output and prints in out'''
    element = []
    for output in outputs:
        #if output == 'TOTALDISTANCE' or  output == 'TOTALTIME' or  output == 'STEPS' or  output == 'LATLONG' or  output == 'ELEVATION':
        if output == 'TOTALDISTANCE':
            distance = mapquest_output.TOTAL_DISTANCE(json)
            element.append(distance)
        elif output == 'TOTALTIME':
            time = mapquest_output.TOTAL_TIME(json)
            element.append(time)
        elif output == 'STEPS':
            step = mapquest_output.STEPS(json)
            element.append(step)
        elif output == 'LATLONG':
            latlng_list = get_latlng_not_rounded(json)
            latlng = mapquest_output.LATLONG(latlng_list)
            element.append(latlng)
        elif output == 'ELEVATION':
            latlng_list = get_latlng_not_rounded(json)
            elevation_urls = get_elevation_urls(latlng_list)
            elevation_json_list = get_elevation_jsons(elevation_urls)
            elevation = mapquest_output.ELEVATION(elevation_json_list)
            element.append(elevation)
        else:
            print('INVALID INPUT')
            return 
            
    for r in element:
        r.find()

def map_quest() -> None:
    '''implements the whole program'''
    try:
        location = location_names()
        output = name_output()
        url = mapquest_input.direction_url(location)
        json = mapquest_input.get_response(url)
        if route_check(json) == True:
            print()
            print('NO ROUTE FOUND')
        else:
            output_generator(output, json)
    except:
        print()
        print('MAPQUEST ERROR')       
    finally:
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')

if __name__ == '__main__':
    map_quest()
