from json_helper import load_list, dump_list

def remove_early_later(styles): # takes a string
    style_list = styles.strip('(later)') # strip later, split earlier
    genre_list = style_list.split(" (early), ")
    style_list = []
    for genre_string in genre_list:
        #print(style)
        genre_string = genre_string.strip()
        if '/' in genre_string:
            g = genre_string.split('/')
            style_list += append_metal(g)
    #print(style_list) # sanity check
    g_list = list(set(style_list) - set(genre_list)) #merge
    return g_list

def append_metal(style_list):
    s1= []
    for style in style_list:
        s = ' Metal'
        if not ' metal' in style.lower():
            print('no metal')
            if 'core' in style.lower() or 'punk' in style.lower() or 'rock' in style.lower() or 'djent' in style.lower() or 'hardcore' in style.lower() or 'crust' in style.lower():
                print("in this stupid control " + style)
                continue
            s1.append(style + s)
    
    genre_list = list(set(style_list) - set(s1)) #merge
    
    return genre_list

def genre_fixer(band_list):
    for i, band in enumerate(band_list):
        styles = band.get('style')
        if '(later)' in styles:
            genre_list = remove_early_later(styles)
        elif '/' in styles:
            genre_list = styles.split('/')
        else:
            genre_list = []
            genre_list.append(styles)
            #genre_list = append_metal(genre_list)
        band['genres'] = genre_list
        band_list[i] = band
        print('genre fixed for ' + band.get('name'))
    return band_list

def main():
    band_list = load_list('./json/items.json')
    #print(band_list) # sanity check
    band_list = genre_fixer(band_list)
    #print(band_list)
    dump_list('./json/test-fix.json', band_list)
    # remove_early_later(band_list) #refactored into taking a band for simplicity

if __name__ == '__main__':
    main()

