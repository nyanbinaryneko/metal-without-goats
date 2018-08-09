import json
import sys

class Band:
    def __init__(self):
       bandname = ""
       location = ""
       genres_unsanitized = ""
       active = ""

parsed = {}
fixed = {}
bandlist = []


with open(sys.argv[1], 'r', encoding="utf-8") as f:
    print(sys.argv[1])
    try:
        #print(f.read())
        parsed =  json.loads(f.read(),encoding="utf-8")
    except Exception as e:
        print(e)
    
    print(parsed.keys())
    num_of_bands = len(parsed["bands"])
    json_file = open("../fixed_json/"+sys.argv[1]+".json", "w+",encoding="utf-8")

    for iteration in range(0, num_of_bands):
        band = Band()
        html = parsed["bands"][iteration][0]
        html = html.split(">")[1]
        band.bandname = html.split("<")[0]
        band.location = parsed["bands"][iteration][1]
        band.genres_unsanitized = parsed["bands"][iteration][2]
        html = parsed["bands"][iteration][3]
        #print(html)
        html = html.split(">")[1]
        #print(html)
        band.active = html.split("<")[0]
        #fixed.setdefault(iteration, band)
        bandlist.append(band.__dict__)
    json_file.write(json.dumps(bandlist, ensure_ascii=False,indent=4),)


        # json_file.write(json.dumps(band.__dict__, ensure_ascii=False, indent=2, separators=(", ",": ")) ) 