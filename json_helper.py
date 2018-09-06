import json

def load_list(path):
    with open(path, "r") as read_file:
       band_list = json.load(read_file)
    return band_list

def dump_list(path, band_list):
    with open(path, "w+") as write_file:
        json.dump(band_list, write_file, indent=2) 