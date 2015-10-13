import csv
import haversine

with open('market_data.csv', 'rU') as market_data:
	reader = csv.reader(market_data)
	market_list = list(reader)
	market_list = [map(float, i) for i in market_list]
	
with open('match_data.csv', 'rU') as match_data:
	reader = csv.reader(match_data)
	match_list = list(reader)
	match_list = [map(float, i) for i in match_list]
	
#print market_list[0]
#print match_list

def distance(point1, point2):	 
	start = ((point1[0],  0,  0),  (point1[1], 0, 0))  
	end = ((point2[0], 0, 0),  (point2[1], 0, 0))  
	return haversine.points2distance(start,  end)

def min_position(location):

	distances = []
	
	for i in match_list:
		d = distance(location, i)
		distances.append(d)
	

	minimum = min(distances)

	position = distances.index(minimum)	
	
	return position + 1 # because excel starts at 1 instead of 0

def key_maker():
	position_key = []

	for i in market_list:
		m = min_position(i)
		position_key.append([m])
	
	return position_key
	
market_position_array = key_maker()

with open("position_of_markets.csv",'wb') as position_of_markets:
	writer = csv.writer(position_of_markets)
	writer.writerows(market_position_array)

		
	
