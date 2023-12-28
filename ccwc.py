#!/usr/bin/env python3

import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple command line wc tool.")
    parser.add_argument("filename", help="file name")
    parser.add_argument("--c", action="store_true", help="Number of bytes in file")
    parser.add_argument("--l", action="store_true", help="Number of lines in file")
    parser.add_argument("--w", action="store_true", help="Number of words in file")
    parser.add_argument("--m", action="store_true", help="Number of chars in file")

    args = parser.parse_args()

    # number of words and lines
    num_words = 0
    num_lines = 0
    with open(f'/Users/joshlin/Documents/wc_tool/{args.filename}','r') as file:
        for line in file:
            num_words += len(line.split())
            num_lines += 1

    # number of bytes
    file_stats = os.stat(f'/Users/joshlin/Documents/wc_tool/{args.filename}')
    num_bytes = file_stats.st_size

    if not args.c and not args.l and not args.w and not args.m:
        print(num_lines, num_words, num_bytes, args.filename, end=" ", flush=True)
    else:
        if args.c:
            print(num_bytes, end=" ", flush=True)
        if args.m:
            print(num_bytes, end=" ", flush=True)
        if args.l:
            print(num_lines, end=" ", flush=True)
        if args.w:
            print(num_words, end=" ", flush=True)
        print(args.filename, end=" ", flush=True)
    