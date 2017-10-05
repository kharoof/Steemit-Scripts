## Retrieve URLS for a tag from steemsql
## Currently this script takes quite a length of time to run.
## It serches for posts just based on tags, additional criteria could be added.
## The output is a list of links stored in json format
import pymssql
import pandas as pd
import csv
import json
import datetime
import re


website_data_path = "/home/path to home directory"
search_string = "photography"


print("Connecting to Steemsql")
conn = pymssql.connect(host ="sql.steemsql.com",database ="DBSteem",user="steemit",password="steemit")

cur = conn.cursor()

#######################################
## Update the output_file and the query
#######################################


output_file=website_data_path + "/urls.json"


query = """
SELECT    url, json_metadata
FROM    Comments (NOLOCK) 
WHERE        depth = 0
   and ISJSON(json_metadata) > 0
   and (
		JSON_QUERY(json_metadata, '$.tags') like '%"""+search_string+"""%'
	)
ORDER BY    created DESC
"""


query = query.replace('\n', ' ')

print("Running Query")
cur.execute(query)
 
output = cur.fetchall()
data = []




for i in range(0,output.__len__()):
    ## For some tags the SQL query above matches more than just the individual tag
    ## so here we perform a secondary search for the tag
    ## most relevant for short tags that contain sequences of letters that would appear in other words
    if search_string in json.loads(output[i][1])['tags']:
         data.append(output[i][0])

with open(output_file, 'w') as outfile:
    json.dump(data, outfile)
