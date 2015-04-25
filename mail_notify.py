#!/bin/env python3

import argparse
import sys
import os

import watcher
import config


def main(argv):
    parser = argparse.ArgumentParser('mail_notify')
    parser.add_argument('maildir')
    parser.add_argument('--config', '-c', help="configuration file")
    args = parser.parse_args(argv)

    basedir = os.path.dirname(__file__)
    config.override(os.path.join(basedir, 'default_config'))
    if args.config:
        config.override(args.config)

    watcher.watch_maildir(args.maildir)


if __name__ == '__main__':
    main(sys.argv[1:])
