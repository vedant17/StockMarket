
import pandas
import numpy


def fileParser(filename, parameter):
    data = pandas.read_csv(filename)
    return  data[parameter]

