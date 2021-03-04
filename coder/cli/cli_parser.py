import argparse


def parse():
    parser = argparse.ArgumentParser(description='Encode and decode ASCII chars and ASCII numbers.',
                                     epilog='Safety first! :)')

    parser.add_argument('coding_type',
                        metavar='Coding_type',
                        type=str,
                        help='Use encode or decode argument to choose using type')

    parser.add_argument('input_string',
                        metavar='Input_string',
                        type=str,
                        help='Code and decode ASCII string')


    return parser.parse_args()
