import argparse

def get_arg_parser():
    parser = argparse.ArgumentParser(
        description='Parser for partitioning experiments.')

    # input file
    parser.add_argument('-if', '--input-file',
                        help='the full path to the benchmark of interest',
                        type=str, required=True)
    
    # path to partitioner
    parser.add_argument('-p', '--partitioner',
                        help='the full path to the partitioner executable', type=str, default="")

    # specify whether to dump unsat cores
    parser.add_argument('-duc', '--dump-unsat-cores', action='store_true',
                        help='indicates that unsat cores should be dumped')

    # specify where to dump unsat cores
    parser.add_argument('-df', '--dump-file', type=str, default="",
                        help='indicates that unsat cores should be dumped')

    # solver options, this is not used in cube collection
    parser.add_argument('-opts', '--options',
                    help='code for which options to use', type=str, default='default')
    
    # Specify number of checks before partitioning
    parser.add_argument('-cbp', '--checks-before-partitioning',
                        help='number of checks before partitioning', type=int, default=140000)

    return parser
