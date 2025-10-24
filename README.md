# Places visited 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Developer
- Jin BENIYAMA [mail](mailto:jinbeniyama@gmail.com)

## Overview
Visualize your journey, from countries to cities.
A simple, intuitive tool to map and plot all the places you've visited.
Perfect for anyone who wants to see their travels at a glance.
Currently under development by J.B.

## Structure
```
places_visited/
  README.md
  notebooks/
    countries_visited.ipynb # Plot countries visited ever
    countries_visited.png   # Example of output
    countries_visited_2.png   # Example of output
```

## Input files 
Input files should be as follows.
See `data/countries_visite_1.txt` for details.
```
country,city,note
Japan,Osaka,1996-05
China,Hongkong;Makau,2017
Taiwan,Taipei,2018
South Korea,Seoul,2018
```

## Examples
```python
# Countiries visited, for one person
python script/show_countries_visited.py data/countries_visited_1.txt --out fig/countries_visited.png
```
<p align="center">
  <img src="/fig/countries_visited.png" width="600"/><br>
  <em>Countries visited (for one person)</em>
</p>


```python
# Countiries visited, for two person
python script/show_countries_visited.py data/countries_visited_1.txt data/countries_visited_2.txt --out fig/countries_visited_2.png
```
<p align="center">
  <img src="/fig/countries_visited_2.png" width="600"/><br>
  <em>Countries visited (for two persons)</em>
</p>


```python
# Countiries and cities visited, for one person
python script/show_countries_visited.py data/countries_visited_1.txt --city --out fig/countries_cities_visited.png
```
<p align="center">
  <img src="/fig/countries_cities_visited.png" width="600"/><br>
  <em>Countries and cities visited</em>
</p>

## Dependencies
This repository is depending on `Python`, `NumPy`, `geopandas`, `matplotlib`.

## LICENCE
This software is released under the MIT License.
