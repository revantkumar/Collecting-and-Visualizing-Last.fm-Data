#Python Script for adding column "type" with value "Undirected" in the file "track_id_sim_track_id.csv". 
#The new file made is "track_id_sim_track_id_type.csv"
import csv
import os

dir = os.path.dirname(__file__)
filename1 = os.path.join(dir, 'track_id_sim_track_id.csv')
filename2 = os.path.join(dir, 'track_id_sim_track_id_type.csv')

with open(filename1,'r') as csvinput:
    with open(filename2, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = reader.next()
        row.append('type')
        all.append(row)

        for row in reader:
            row.append('Undirected')
            all.append(row)

        writer.writerows(all)