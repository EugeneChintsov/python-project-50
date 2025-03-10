#!usr/bin/env python3
from gendiff.modules.arg_parsing import get_args
from gendiff.main import generate_diff


def main():
    args = get_args()
    print(generate_diff(args.first, args.second, args.format))
    

if __name__ == "__main__":
    main()
