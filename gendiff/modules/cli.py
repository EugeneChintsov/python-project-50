import argparse


def greet():
    parser = argparse.ArgumentParser(
            prog='gendiff',
            description='Compares two configuration files and shows a difference.',
            usage='%(prog)s [-h] first_file second_file'
        )
    parser.add_argument('first_file', type=str, help='Input first file')
    parser.add_argument('second_file', type=str, help='Input second file')
    args = parser.parse_args()
    print(args)