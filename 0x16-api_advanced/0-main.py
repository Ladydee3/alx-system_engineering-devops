#!/usr/bin/python3
import sys
from subs import number_of_subscribers

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-main.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))


