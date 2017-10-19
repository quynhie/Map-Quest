# Quynh Le 27537272
# Project 3
import mapquest_input

class TOTAL_DISTANCE:
    def __init__(self,json:dict):
        self._json = json

    def find(self) -> None:
        '''finds the total distance in the json'''
        result = self._json['route']['distance']
        print()
        print('TOTAL DISTANCE:', round(result), 'miles')
        
class TOTAL_TIME:
    def __init__(self,json:dict):
        self._json = json
        
    def _convert(self, result: int) -> int:
        '''converts the seconds into minutes'''
        return round(result /60)
        
    def find(self):
        '''finds the total time in the json & prints it out'''
        result = self._json['route']['time']
        print()
        print('TOTAL TIME:', self._convert(result), 'minutes')

class STEPS:
    def __init__(self,json:dict):
        self._json = json
        
    def find(self) -> None:
        '''find the step by step directions in the json & prints in out.'''
        print()
        print('DIRECTIONS')
        for route in self._json['route']['legs']:
            for direction in route['maneuvers']:
                print(direction['narrative'])
       
class LATLONG:
    def __init__(self, latlng: list):
        self._latlng = latlng
        
    def _round_latlng(self) -> list:
        '''rounds the lats & longs to 4 decimal places'''
        result = []
        for l in self._latlng:
            result.append(round(l,4))
        return result
            
    def _format(self) -> str:
        '''adds the N or S to the latitudes, W or E to longitudes & formats it'''
        result = ''
        for l in range(len(self._latlng)):
            if l % 2 == 0:
                if self._latlng[l] > 0:
                    lat = '{:.2f}'.format(abs(round(self._latlng[l],2)))
                    result = result + lat + 'N' + ' '
                else:
                    lat = '{:.2f}'.format(abs(round(self._latlng[l],2)))
                    result = result + lat + 'S' + ' '
            else:
                if self._latlng[l] > 0:
                    lng = '{:.2f}'.format(abs(round(self._latlng[l],2)))
                    result = result + lng + 'E' + '\n'
                else:
                    lng = '{:.2f}'.format(abs(round(self._latlng[l],2)))
                    result = result + lng + 'W'+ '\n'          
        return result.strip('\n') 

    def find(self) -> None:
        '''prints out the formatted latlngs'''
        self._round_latlng()
        print()
        print('LATLONGS')
        print(self._format())

class ELEVATION:   
    def __init__(self, json:'list dict'):
        self._json = json
    
    def find(self) -> None:
        '''finds and prints out the elevation in the list of elevation jsons'''
        print()
        print('ELEVATIONS')
        for elevation_json in self._json: 
            for elevation in elevation_json['elevationProfile']:
                converted_elevation = round(elevation['height'])
            print(converted_elevation)
