import numpy
import pandas as pd
import os

def main():
    current = os.getcwd()
    if(os.path.isfile(current+"/microcystins.csv")):
        print("microcystin data exists")
        filepath0 = current + "/microcystins.csv"
        mcdata = pd.read_csv(filepath0, delimiter='\n', header=None)
        datapoints = mcdata.shape[0]
        print(mcdata)
    else:
        print("No microcystin data found")

    if(os.path.isfile(current+"/cylindrospermosin.csv")):
        print("cylindrospermosin data exists")
        filepath1 = current + "/cylindrospermosin.csv"
        csdata = pd.read_csv(filepath1, delimiter='\n', header=None)
        datapoints = csdata.shape[0]
        print(csdata)
    else:
        print("No cylindrospermosin data found")
    
main()


def getMean(data):
    count = 0
    datalen = len(data)
    for i in range(0,datalen):
        count  = count + data[0,i]
    return count

