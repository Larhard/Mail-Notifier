#!/bin/sh

PYTHON="/bin/env python3"
PROGNAME="mail_notify.py"
BASEDIR=$(dirname $(readlink -e "$0"))

$PYTHON "$BASEDIR/$PROGNAME" "$@"
