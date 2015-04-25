#!/bin/env python3

import argparse
import sys

import watcher


def main(argv):
    parser = argparse.ArgumentParser('mail_notify')
    parser.add_argument('maildir')
    args = parser.parse_args(argv)

    watcher.watch_maildir(args.maildir)


if __name__ == '__main__':
    main(sys.argv[1:])