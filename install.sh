#!/bin/bash

sudo apt install pelican ghp-import
sudo -H pip3 install mdx-linkify markdown-del-ins pelican-neighbors pelican-related-posts beautifulsoup4
# sudo -H pip3 install pelican[markdown]
# python3 -m pip install pelican[markdown] typogrify

# To update, use "make github"
