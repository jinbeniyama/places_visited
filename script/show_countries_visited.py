#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Show countries visited. 
"""
from argparse import ArgumentParser as ap
import pandas as pd
from core import (
    plot_countries_visited, plot_countries_visited_2)


if __name__ == "__main__":
    parser = ap(description="Show countries visited.")
    parser.add_argument(
        "f", type=str, nargs="*",  
        help="Input file with countries and cities visited.")
    parser.add_argument(
        "--city", action="store_true", default=False,
        help="Show cities.")
    parser.add_argument(
        "--out", type=str, default="countires_visited.pdf",
        help="Output filename.")
    args = parser.parse_args()

    print("")
    if len(args.f) == 0:
        print("  Not implemented. No input file.")
    elif len(args.f) == 1:
        df1 = pd.read_csv(args.f[0], sep=",")
        print("  Plot countries visited for 1 person.")
        plot_countries_visited(df1, args.out, city=args.city)
    elif len(args.f) == 2:
        df1 = pd.read_csv(args.f[0], sep=",")
        df2 = pd.read_csv(args.f[1], sep=",")
        col = ["blue", "red", "purple"]
        print("  Plot countries visited for 2 persons.")
        plot_countries_visited_2(df1, df2, col, out=args.out)
    else:
        print("  Not implemented. Input files are two much.")
    print("")
    
