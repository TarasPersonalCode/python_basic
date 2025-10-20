import datetime, os, pathlib, sys, time

import numpy  as np
import pandas as pd
import xarray as xr

lmap    = lambda fun_, list_: list(map(   fun_, list_))
lfilter = lambda fun_, list_: list(filter(fun_, list_))

mkdir = lambda dirname: pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)

def hard_assert(cond, msg=''):
    if not cond:
        raise AssertionError(msg)

def dates_between(start_date_str, end_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
    end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

    hard_assert(start_date <= end_date)

    dates_in_range = []
    current_date = start_date
    while current_date <= end_date:
        dates_in_range.append(current_date.strftime('%Y%m%d'))
        current_date += datetime.timedelta(days=1)
    return dates_in_range

def day_of_week(date_str):
    return datetime.datetime.strptime(date_str, '%Y%m%d').strftime('%A')
