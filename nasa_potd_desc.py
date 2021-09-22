"""Prints NASA's POTD title and description and saves the image."""

import argparse
import textwrap
from datetime import date, datetime, timedelta
from typing import Tuple

import requests
from diskcache import Cache


def get_nasa_apod_data(
    cache: Cache,
    curr_date: date = None,
    delta: int = 0
) -> Tuple[str, str, bytes]:
    """Return NASA's POTD title, description and image data.

    :param cache: cache object to use
    :type cache: Cache
    :param curr_date: date to use, defaults to None
    :type curr_date: date, optional
    :param delta: offset in days to decrease date by, defaults to 0
    :type delta: int, optional
    :return: title, description and image data
    :rtype: Tuple[str, str, bytes]
    """
    if curr_date is None:
        curr_date = datetime.utcnow().date()

    curr_date = curr_date - timedelta(days=delta)
    curr_date = curr_date.strftime('%Y-%m-%d')

    # Load cache, if cache is none or image data is none, load data again
    cache_out = cache.get(curr_date)
    if cache_out is not None:
        title, desc, img_data = cache_out
        if img_data is not None:
            return title, desc, img_data

    # Fetch data from API
    url = f"https://apodapi.herokuapp.com/api?date={curr_date}"
    obj = requests.get(url).json()

    # Extract title and description
    title = obj["title"]
    desc = "\n".join(textwrap.wrap(obj["description"].strip(), 50))

    # Saving Image
    # if hdurl is there, use that do dl image,
    # if not, check if url is image
    # if not, check if it is yt link
    # if not, use blank bg
    img_url = obj.get("hdurl") if obj.get(
        "hdurl") is not None else obj.get("url", "")
    if img_url.split(".")[-1] in ["jpg", "png", "jpeg"]:
        img_data = requests.get(img_url).content
    elif (img_url.startswith("https://www.youtube.com")
            or img_url.startswith("https://youtube.com")):
        vid_id = img_url.split("embed/")[1].split("?")[0]
        img_data = requests.get(
            f"https://i.ytimg.com/vi/{vid_id}/maxresdefault.jpg").content
    else:
        img_data = None

    # Update Cache
    cache[curr_date] = (title, desc, img_data)

    return title, desc, img_data


cache = Cache(".cache")

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--days', type=int, default=0, help="Days offset.")

args = parser.parse_args()

curr_date = datetime.utcnow().date()
title, desc, img_data = get_nasa_apod_data(cache, curr_date, args.days)

print("NASA Photo of The Day: " + title + "\n")

print(desc)

if img_data is None:
    raise ValueError(
        f"img_data for date {curr_date} and offset {args.days} not found.")

with open(f'{args.days}.jpg', 'wb') as handler:
    handler.write(img_data)

cache.close()
