# PARALLEL PROGRAMMING ON PYTHON

The dataset that will be used in this exercise comes from Berkeley Earth data (available on Kaggle). The dataset shows
the temperature records around the world since 1750. More information and a detailed
description can be found here.
Considering the file “GlobalLandTemperaturesByCity.csv” of the dataset, create a python parallel
program (in one or several scripts) that :

1. Calculates and show the global average temperature for each country (Use the
"AverageTemperature" column values)
2. For each country, display the highest temperature as well as the name of the city and the date this record was made.

Your program must be able to do this for x (x > 0 and to choose according to the performance and
capacity of your computer) countries at the same time. To do this, you will use a python
multiprocessing library (https://docs.python.org/3/library/multiprocessing.html for example any
other you choose).
Output. For this exercise, you must provide the source code and a short report presenting the
different libraries used, what you have learned and the difficulties encountered.
