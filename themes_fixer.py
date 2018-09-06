from json_helper import load_list, dump_list

# refactor when i don't suck at regex, also slow works for now
# scale later
def fix_themes(band_list):
    for i, band in enumerate(band_list):
        lyrical_themes = band.get("lyrical_themes")
        themes = lyrical_themes.split(", ")
        for theme in themes:
            if " and " in theme:
                themes_split = theme.split(" and ")
                themes.remove(theme)
                themes += themes_split # combine lists
        
        band['themes'] = themes # add themes to dict
        band_list[i] = band # update in place
        
        print("fixed themes for: " + band.get("name"))
    return band_list

# for testing
def main():
    band_json = load_list('./json/test.json') # load JSON file set as env variable later
    band_list = fix_themes(band_json)
    dump_list('./json/test_fix.json', band_list)

if __name__ == '__main__':
    main()