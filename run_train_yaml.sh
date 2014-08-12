#!/bin/bash

PYTHONPATH=$PYTHONPATH:$(pwd)/.. ../pylearn2/pylearn2/scripts/train.py $1
