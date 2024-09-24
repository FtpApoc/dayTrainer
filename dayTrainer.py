from trainerVerbose import trainerVerbose
import random

def Main():
    
    print("""
          Please Select Input Mode
          1. Manual
          2. Automatic
          """)

    iMode = int(input())

    if iMode == 1:
        # Take Inputs 
        uYear = int(input("Year: "))
        uMonth = int(input("Month: "))
        uDay = int(input("Day: "))

    if iMode == 2:
        uYear = random.integer(1600,3000)
        uMonth = random.integer(1,12)
        uDay = random.integer(1,31)
    
    print("""
        Please Select Verbosity
        1. High 
          """)
    
    iVerb = int(input())

    if iVerb == 1:
        trainerVerbose(uDay,uMonth,uYear)

Main()