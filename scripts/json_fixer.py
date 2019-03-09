from json_helper import load_list, dump_list
from themes_fixer import theme_fixer
from genre_fixer import genre_fixer

def main():
    band_list = load_list('./json/test.json')
    band_list = theme_fixer(band_list)
    band_list = genre_fixer(band_list)
    #print(band_list)
    dump_list('./json/test-fix.json', band_list)

if __name__ == '__main__':
    main()