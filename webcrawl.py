#!/usr/bin/env python3
# 
# Orogianlly written by Seth Kenlon for plagiarism checking
# minor tweaks by Ajoy for using for web crawling

# This program is free software: you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at
# your option) any later version.

# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

# GPLv3
# Please check <http://www.gnu.org/licenses/>.

import sys
import random
from pathlib import Path
from googlesearch import search

# Read the line of the file data.txt
def Scrub(ARG):
    f = open(ARG, 'r')
    LINES = f.readlines()
    Search(LINES)

# Invoke websearch for exact line match
def Search(LINES):
    COUNT=0
   
    for LINE in LINES:
        COUNT += 1        
        PAUSE = random.randrange(1,4)

        if VERBOSE:
            print("Searching...")
           
        for ITEM in search(LINE, tld="com", num=1, stop=1, pause=PAUSE):
            if VERBOSE:
                print("SIMILAR MATCH:" + LINE + " -> " + ITEM)
            else:
                print("SIMILAR MATCH: line " + str(COUNT) + " -> " + ITEM)

if __name__ == "__main__":
    random.seed()
    n=1
   
    if sys.argv[1] == "--verbose" or sys.argv[1] == "-v":
        VERBOSE = True
        # shift 1
        n += 1
    else:
        VERBOSE = False
       
    f = Path(sys.argv[n])

    if not f.is_file():
        print("Provide a text file to check.")
        exit()
    else:
        Scrub(sys.argv[n])
