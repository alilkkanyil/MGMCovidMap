import json

data=[]

with open('response.json','r') as infile:
    data=json.load(infile)

output={"type": "FeatureCollection","crs": {"type": "name","properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }}}

coord=[]
fealist=[]

for i in data:
    coord=[i['lat'],i['lng']]
    fealist.append({'type':'Feature','properties':i,'geometry':{'type':'Point','coordinates':coord}})

output['features']=fealist

with open('outmaps.json','w') as outfile:
    json.dump(output,outfile,indent=4)



