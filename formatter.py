import json
import argparse
import logging
import re

logger = logging.getLogger('formatter')

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

        logger.debug("fixed themes for: " + band.get("name"))
    return band_list


def remove_seps(styles):  # takes a string
    '''
    style_list = styles.strip('(later)')  # strip later, split earlier
    genre_list = style_list.split(" (early), ")
    style_list = []
    '''
    logger.debug(f'styles before: {styles}')
    logger.debug('remove contents of parens & strip:')
    styles = re.sub(r'\([^)]*\)', '', styles).strip("()") # matches parens
    logger.debug(f'{styles}')
    logger.debug('replace "/" with ",", and split into tokens')
    styles = re.sub(r'([//])', ',', styles).split(',')
    logger.debug(f'{styles}')
    return append_metal(styles)


def append_metal(style_list):
    for idx, style in enumerate(style_list):
        style.strip()
        s = ' Metal'
        if not s.lower() in style.lower():

            logger.debug(f'no metal {style}')
            # jesus christ, refactor THIS line.
            if 'core' in style.lower() or 'punk' in style.lower(
            ) or 'rock' in style.lower() or 'djent' in style.lower(
            ) or 'hardcore' in style.lower() or 'crust' in style.lower():
                logger.debug("in this stupid control " + style)
            else:
                logger.debug("appending metal")
                style = style + s
                logger.debug(f"{style}")
        style_list[idx] = style.strip()
    logger.debug(f'style_list: {style_list}')
    return style_list


def genre_formatter(band_list):
    for i, band in enumerate(band_list):
        styles = band.get('style')
        styles = remove_seps(styles)
        band['genres'] = styles
        band_list[i] = band
        logger.debug('genre fixed for ' + band.get('name'))

    return band_list
