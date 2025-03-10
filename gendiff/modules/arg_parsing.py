import argparse


def get_args() -> argparse.Namespace:
    """
    Parses command-line arguments for the 'gendiff' program.
    """ 
    parser = argparse.ArgumentParser(
            prog='gendiff',
            description='Compares two configuration files\
                and shows a difference.',
            usage='%(prog)s [-h] [-f FORMAT] first_file second_file'
        )
    parser.add_argument('first_file', type=str, help='Input first file')
    parser.add_argument('second_file', type=str, help='Input second file')
    parser.add_argument(
        '-f', '--format',
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help='Set format of output (default: stylish)'
    )
    return parser.parse_args()
