import sys
import argparse

parser = argparse.ArgumentParser(description='python implementation of cat')

parser.add_argument('files', nargs='*', action='store', type=str)
args = parser.parse_args()

print(args)

line_number = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
#    if args.numbers:
#        for line in in_file.readlines():
#            print(f"\t{line_number}\t{line}", end="")
#            line_number += 1
#    else:
    print(in_file.read())
