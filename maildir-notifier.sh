#!/bin/sh

PYTHON="/bin/env python3"
PROGNAME="mail_notify.py"
BASEDIR=$(dirname $(readlink -e "$0"))
LOCAL_CONFIG_FILE="$HOME/.maildir-notifier.rc"
ARGS=""

if [ -e "$LOCAL_CONFIG_FILE" ]; then
    ARGS="$ARGS -c $LOCAL_CONFIG_FILE"
fi

$PYTHON "$BASEDIR/$PROGNAME" ${ARGS} "$@"
