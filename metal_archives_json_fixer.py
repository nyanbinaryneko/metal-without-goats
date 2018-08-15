import json
import sys
from band import Band

parsed = {}
fixed = {}
bandlist = []


with open(sys.argv[1], 'r', encoding="utf-8") as f:
    try:
        parsed =  json.loads(f.read(),encoding="utf-8")
        print(len(parsed["bands"]))
    except Exception as e:
        print(e)
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
        html = html.split(">")[1]
        band.active = html.split("<")[0]
        band.genres_cleaned = ""
        bandlist.append(band.__dict__)
    json_file.write(json.dumps(bandlist, ensure_ascii=False,indent=4))


        # json_file.write(json.dumps(band.__dict__, ensure_ascii=False, indent=2, separators=(", ",": ")) ) 