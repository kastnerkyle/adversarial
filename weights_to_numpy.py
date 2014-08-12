from sklearn.externals.joblib import dump
import sys
from pylearn2.utils import serial

model = serial.load(sys.argv[1])
all_weights = []
for l in model.generator.mlp.layers:
    all_weights.append(l.get_weights())
from IPython import embed; embed()
