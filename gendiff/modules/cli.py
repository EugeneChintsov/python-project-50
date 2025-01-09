import argparse


def greet():
    parser = argparse.ArgumentParser(
            prog='gendiff',
            description='Compares two configuration files\
                and shows a difference.',
            usage='%(prog)s [-h] [-f FORMAT] first_file second_file'
        )
    parser.add_argument('first_file', type=str, help='Input first file')
    parser.add_argument('second_file', type=str, help='Input second file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()