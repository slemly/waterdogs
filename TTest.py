'''
@author Samuel Lemly
EGR 361 Analysis of Engineering Data, Water Dogs
@March 2019
Python v. 3.7.2
'''
import os
from ttestfuncs import *

def main():
    current = os.getcwd()
    if(os.path.isfile(current+"/microcystins.csv")):
        print("microcystin data exists")
        filepath0 = current + "/microcystins.csv"
        mcdata = pd.read_csv(filepath0, delimiter='\n', header=None)
        mcdrkEPA = 0.3 #   <--   Change these values to adjust standards. Add new test instances for more.
        mcdrkWHO = 1 #     <--
        mcLrecWHO = 10 #   <--
        mcHrecWHO = 50 #   <--
        DOF = len(mcdata) - 1 # degrees of freedom
        print("************************************************************************************")
        mcdata = np.transpose(mcdata) # transposing data for display purposes, make sure to undo this step
        print("Microcystin data:")
        print(mcdata)
        mcdata = np.transpose(mcdata)
        print("T-Test results:")
        print("0.3 microgram/litre: EPA Microsystin Drinking standard, child")
        print(runTTest(mcdata,mcdrkEPA))
        print("1 microgram/litre: WHO Microcysistin Drinking Standard")
        print(runTTest(mcdata,mcdrkWHO))
        print("10 microgram/litre: WHO Microcysistin Recreation standard, allergenic effects")
        print(runTTest(mcdata,mcLrecWHO))
        print("50 microgram/litre: WHO Microcysistin Recreation standard, moderate health effects")
        print(runTTest(mcdata,mcHrecWHO))
        print("Degrees of freedom: " + str(DOF))
        print("************************************************************************************")
        print("\n \n")
    else:
        print("No microcystin data found")

    if(os.path.isfile(current+"/cylindrospermosin.csv")):
        print("cylindrospermosin data exists")
        filepath1 = current + "/cylindrospermosin.csv"
        csdata = pd.read_csv(filepath1, delimiter='\n', header=None)
        
        csEPAchild = 0.7 # EPA standard for micrograms of cylindrospermosin/litre for drinking water. No recreational EPA number given. No WHO data available.
        csEPAadult = 1.6 # EPA Adult cylindrospermosin standard
        csCArec = 4 # EPA cylindrospermosin recreational standard
        DOF = len(csdata) - 1
        print("************************************************************************************")
        print("Cylindrospermosin data:")
        csdata = np.transpose(csdata) # transpose for viewing purposes
        print(csdata)
        csdata = np.transpose(csdata)
        print("T-Test results:")
        print("0.7 microgram/litre: EPA Cylindrospermosin Drinking standard, child")
        print(runTTest(csdata, csEPAchild))
        print("1.6 microgram/litre: EPA Cylindrospermosin Drinking standard, adult")
        print(runTTest(csdata,csEPAadult))
        print("4 microgram/litre: State of California Cylindrospermosin Recreation standard")
        print(runTTest(csdata,csCArec))
        print("Degrees of freedom: " + str(DOF))
        print("************************************************************************************")
        print("\n \n")
    else:
        print("No cylindrospermosin data found")
    
main()




