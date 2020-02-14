data = [
    {"name":"Sachin","avg":52.44,"50":95,"100":51,"teams":["Ind","MI","DD"]},
    {"name":"Smith","avg":53.44,"50":55,"100":23,"teams":["Aus","RR","SRH"]},
    {"name":"Kohli","avg":54.44,"50":76,"100":42,"teams":["Ind","RCB","DD"]},
    {"name":"Dhoni","avg":53.44,"50":79,"100":12,"teams":["Ind","CSK","PRS"]},
    {"name":"Root","avg":51.44,"50":39,"100":18,"teams":["Eng","KP","RR"]},
    {"name":"Yuvraj","avg":44.44,"50":45,"100":15,"teams":["Ind","KP","MI","RCB"]},
    {"name":"Shami","avg":19.44,"50":1,"100":0,"teams":["Ind","KKR"]},
    {"name":"Starc","avg":21.44,"50":0,"100":0,"teams":["Aus","RCB","MI"]},
    ]

'''
for i in range(len(data)):
    if data[i]['team'] == 'Ind':
        print(data[i])
'''

for i in range(len(data)):
    if 'MI' in data[i]['teams']:
        print(data[i])
