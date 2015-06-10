#!/bin/bash

DIR=$(dirname $0)

pylint --rcfile $DIR/../.pylintrc $DIR/prettypublictest
