#Importing the required libraries
import urllib2
import ast
import time

#Getting the first 100 similar tracks from the Last.fm API
response = urllib2.urlopen("http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=cher&track=believe&limit=100&api_key=509c347edf282ac07730bd4098028827&format=json")
data = response.read()
data = ast.literal_eval(data) 
newdata = []
for entry in data["similartracks"]["track"]:
	if "mbid" in entry.keys() and entry["mbid"] != "":
		newdata.append(entry)

response.close()

limit = 10
api_key = "509c347edf282ac07730bd4098028827"
format = "json"

new_similar_data = []

#Getting the 10 similar tracks for each of the 100 tracks obtained above
for entry in newdata:
	try:
		mbid = entry["mbid"]
		url = "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&mbid="+mbid+"&limit="+str(limit)+"&api_key="+api_key+"&format="+format
		response2 = urllib2.urlopen(url)
		similar_data = response2.read()
		similar_data = ast.literal_eval(similar_data)
		if "error" in similar_data.keys():
			continue
		val = similar_data["similartracks"]["track"]
		for e in val:
			if type(e) == str:
				continue
			if e["mbid"] != "":
				val = [mbid, e["mbid"]]
				val.sort()
				new_similar_data.append(val)
		response2.close()
		time.sleep(0.1)
	except:
		pass

#Removing duplicate entries from the list
new_new_similar_data = []
for elem in new_similar_data:
    if elem not in new_new_similar_data:
        new_new_similar_data.append(elem)
new_similar_data = new_new_similar_data

#Writing to first 100 tracks to "tracks.csv"
file1 = open("tracks.csv", "w")
file1.write("id,track_name,artist\n")

for entry in newdata:
	row = entry['mbid'] + ',' + entry['name'] + ',' + entry['artist']['name'] + '\n'
	row = row.encode('utf-8')
	file1.write(row)

file1.close()

#Writing to "track_id_sim_track_id.csv"
file2 = open("track_id_sim_track_id.csv", "w")
file2.write("source,target\n")

for [s, t] in new_similar_data:
	row = s + ',' + t + '\n'
	row = row.encode('utf-8')
	file2.write(row)

file2.close()






