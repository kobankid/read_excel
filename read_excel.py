#!/usr/bin/python3

import pandas as pd

"""
This module is for reading data from excel file(xlsx)
"""

import os
import sys

def main():
    print("hello")
    print(pd.__version__)
    df = pd.read_excel('./test.xlsm', index_col=0)
    print(df)

    df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                      index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

    print(df)

    df.to_excel('./pandas_to_excel.xlsx', sheet_name='test1')

if __name__ == "__main__":

    main()