__author__ = 'thiagocastroferreira'

from Crawler.Crawling import *

messages = ["DAILY_INCREASE", "DAILY_DECREASE", "HOUR_VOLUME_INCREASE", "HOUR_VOLUME_DECREASE"]

def run(shares, shares_old):
    select_messages = []
    first = shares[0]
    last = shares[len(shares)-1]

    if len(shares_old) > 0:
        first_old = shares_old[0]
        last_old = shares_old[len(shares_old)-1]

        volume_old = (last_old.volume - first_old.volume) / float(first_old.volume)
        volume = (last.volume - first.volume) / float(first.volume)

        if volume > volume_old:
            select_messages.append("HOUR_VOLUME_INCREASE")
        elif volume < volume_old:
            select_messages.append("HOUR_VOLUME_DECREASE")

    if last.variation > 0:
        select_messages.append("DAILY_INCREASE")
    elif last.variation < 0:
        select_messages.append("DAILY_DECREASE")



    return select_messages