from doomsdayLogic import *

def trainerVerbose(uDay,uMonth,uYear):

    print("=======================================================")
    # 1. Year and Century Calculated First
    print("1. Year and Century Calculated First")
    total = 0

    # 1a. closest century octant selected
    (octant, remainder, leapYears) = handleCenturyOctant(uYear)
    total += octant
    print(f"    1a. Use Octant ({octant}) | Total = {total}")

    # 1b. Add remaining year offset
    total += remainder
    print(f"    1b. +/- Offset ({remainder}) | Total = {total}")

    # 1c. Add appropriate leap years
    total += leapYears
    print(f"    1c. Add Leap Years ({leapYears}) | Total = {total}")

    # 1d. Add century base
    centBase = handleCentury(uYear)
    total += centBase 
    print(f"    1d. Add Century Base ({centBase}) | Total = {total}")

    # 1e. Mod by 7
    total = total % 7
    print(f"    1e. Mod 7 | Total = {total}")

    # 1f. Is It A Leap Year?
    isLeap = handleLeap(uYear)
    print(f"    1f. is it a leap year? ({isLeap})")


    # 2. Month and Date Calculated next
    print("2. Month and Date Calculated next")

    # 2a. Closest doomsday date, set to 1e answer
    doomsdate = handleMonth(uMonth,isLeap)
    print(f"    2a.  {doomsdate}/{uMonth}/{uYear} is {total} | Total = {total}")

    # 2b. calculate offset
    offset,answer = handleDay(uDay,total,doomsdate)
    total += offset
    print(f"    2b. The Offset is {offset} | Total = {total}")

    # 2c. mod 7
    print(f"    2c. The Day Index is {(total) % 7}")

    # 2d. dayArray index
    print(f"    2d. The Answer is {answer}")
    
    print("=======================================================")