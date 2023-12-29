#!/usr/bin/env python3

import argparse

def count_bytes(file_content):
    return len(file_content)

def count_lines(file_content):
    return file_content.count('\n') + 1

def count_words(file_content):
    return len(file_content.split())

def count_characters(file_content):
    return len(file_content)

def main():
    parser = argparse.ArgumentParser(description='A simple version of wc command')
    parser.add_argument('filename', nargs='?', type=str, default=None, help='Name of the file or use stdin if not specified')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='Print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='Print the word counts')
    parser.add_argument('-m', '--characters', action='store_true', help='Print the character counts')

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r') as file:
            file_content = file.read()
    else:
        print("Please provide path to file")
        return

    num_lines, num_words, num_bytes, num_char = count_bytes(file_content), count_words(file_content), count_words(file_content), count_characters(file_content)

    if not any([args.bytes, args.lines, args.words, args.characters]):
        print(num_lines, num_words, num_bytes, args.filename, end=" ")
    else:
        if args.bytes:
            print(num_bytes, end=" ")
        if args.characters:
            print(num_char, end=" ")
        if args.lines:
            print(num_lines, end=" ")
        if args.words:
            print(num_words, end=" ")
        print(args.filename, end=" ")

if __name__ == "__main__":
    main()