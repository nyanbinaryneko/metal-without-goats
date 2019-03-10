import json
import argparse

# TODO: add formatters for location, and other metadata returned by scrape
# TODO: add scraper into project
# TODO: add more file support
# TODO: multifile support

def theme_formatter(band_list):
    for i, band in enumerate(band_list):
        lyrical_themes = band.get("lyrical_themes")
        themes = lyrical_themes.split(", ")

        for theme in themes:
            if " and " in theme or " / " in theme:
                if " and " in theme:
                    themes_split = theme.split(" and ")
                else:
                    themes_split = theme.split(" / ")
                themes.remove(theme)
                themes += themes_split  # combine lists

        band['themes'] = themes  # add themes to dict
        band_list[i] = band  # update in place

        print("fixed themes for: " + band.get("name"))
    return band_list


def remove_early_later(styles):  # takes a string
    style_list = styles.strip('(later)')  # strip later, split earlier
    genre_list = style_list.split(" (early), ")
    style_list = []
    for genre_string in genre_list:
        #print(style)
        genre_string = genre_string.strip()
        if '/' in genre_string:
            g = genre_string.split('/')
            style_list += append_metal(g)
    g_list = list(set(style_list) - set(genre_list))  # merge
    return g_list


def append_metal(style_list):
    s1 = []
    for style in style_list:
        s = ' Metal'
        if not ' metal' in style.lower():
            print('no metal')
            # jesus christ, refactor THIS line.
            if 'core' in style.lower() or 'punk' in style.lower(
            ) or 'rock' in style.lower() or 'djent' in style.lower(
            ) or 'hardcore' in style.lower() or 'crust' in style.lower():
                print("in this stupid control " + style)
                continue
            s1.append(style + s)

    genre_list = list(set(style_list) - set(s1))  # merge

    return genre_list


def genre_formatter(band_list):
    for i, band in enumerate(band_list):
        styles = band.get('style')
        if '(later)' in styles:
            genre_list = remove_early_later(styles)
        elif '/' in styles:
            genre_list = styles.split('/')
        else:
            genre_list = []
            genre_list.append(styles)
        band['genres'] = genre_list
        band_list[i] = band
        print('genre fixed for ' + band.get('name'))
    return band_list

