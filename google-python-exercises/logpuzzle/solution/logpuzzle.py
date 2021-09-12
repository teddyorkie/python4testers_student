#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021

import re
import sys
import pathlib
from urllib.request import urlretrieve

"""Logpuzzle exercise
Cho một logfile của apache, tìm các urls và download ảnh của câu đố.

Một url của câu đố sẽ trông như sau:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_sort_key(url):
  """Used to order the urls in increasing order by 2nd word if present."""
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

  # Extract the hostname from the filename
  underbar = filename.rfind('_')
  host = filename[underbar + 1:]

  # Store the ulrs into a dict to screen out the duplicates
  url_dict = {}

  with open(filename) as f:
    for line in f:
      # Find the path which is after the GET and surrounded by spaces.
      match = re.search(r'"GET (\S+)', line)
      # Above uses \S (upper case S) which is any non-space char
      # Alternately could use square brackets: "GET ([^ ]+)"
      # or the ? form: "GET (.+?) "

      if match:
        path = match.group(1)
        # Add to dict if it's a special "puzzle" url
        # (could combine this 'puzzle' check with the above GET extraction)
        if 'puzzle' in path:
          url_dict['http://' + host + path] = 1

  return sorted(url_dict.keys(), key=url_sort_key)


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # import os
  # if not dest_dir.exists():
  #   os.makedirs(dest_dir)

  dest_dir.mkdir(parents=True, exist_ok=True)
  with open(dest_dir / 'index.html', 'w') as index:
    index.write('<html><body>\n')

    for i, img_url in enumerate(img_urls):
      local_name = f'img{i}'
      print('Retrieving...', img_url)

      urlretrieve(img_url, dest_dir / local_name)
      index.write(f'<img src="{local_name}">')

    index.write('\n</body></html>\n')

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    result_path = pathlib.Path.cwd() / todir
    download_images(img_urls, result_path)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
