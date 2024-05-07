import datetime, os, sys, time

import numpy  as np
import pandas as pd
import xarray as xr

import matplotlib.pyplot as plt

lmap    = lambda fun_, iter_: list(map(   fun_, list_))
lfilter = lambda fun_, iter_: list(filter(fun_, list_))


