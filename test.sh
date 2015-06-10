#!/bin/bash

# This sets the librato_ic directory as part of sys.path,
# so that tests run from this script finds it as an
# importable modules

# this runs pytest's test runner, py.test, with the provided
# command line.

# Suggested usage: ./test.sh tests

THIS_DIR=$(dirname $0)
export PYTHONPATH=$PYTHONPATH:$THIS_DIR

exec py.test $@
