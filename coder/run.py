from coder.cli.cli_parser import parse
from coder.core.handle_data import *

def run(args):

    if args.coding_type == "encode":
        validate_to_encoding(args.input_string)
        result = encoding(args.input_string)
        print(result)
    elif args.coding_type == "decode":
        validate_to_decoding(args.input_string)
        result = decoding(args.input_string)
        print(result)
    else:
        raise SyntaxError("First argument must be 'encode' or 'decode'")


if __name__ == "__main__":
    run(parse())