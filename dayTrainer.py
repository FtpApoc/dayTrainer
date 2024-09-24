import json
import math

def handleLeap(uYear):
    if uYear % 4 == 0:
        if uYear % 100 == 0:
            isLeap = False
        else:
            isLeap = True
    else:
        isLeap = False
    return isLeap

def handleCentury(uYear):
    centuryArray = [2,0,5,3]
    answer = (math.floor(uYear/100) - 20) % 4 
    centuryDoomsDay = centuryArray[answer]

    return(centuryDoomsDay)

def handleYear(uYear):
    centuryDoomsDay = handleCentury(uYear)

    yearsPast = uYear % 100
    leapYearsPast = math.floor(yearsPast / 4)
    
    answer = centuryDoomsDay + yearsPast + leapYearsPast

    isLeap = handleLeap(uYear)

    return answer,isLeap
    

def handleMonth(uMonth,leap_year):
    uMonth -= 1

    with open("doomsdays.json","r") as json_file:
        monthDayList = json.load(json_file)["months"][uMonth]


        if (leap_year and "leap_alternate" in monthDayList):
           monthDayType = "leap_alternate" 
        else: 
            monthDayType = "doomsday"

        monthsDoomsDate = monthDayList[monthDayType]
    
    return monthsDoomsDate

def handleDay(uDay):
    
    dayArray = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    offset = uDay - monthsDoomsDate
    answer = dayArray[(doomsday + offset) % 7]
    
    print(f"The Doomsday This Month is: {monthsDoomsDate}")
    print(f"This is {offset} days away from Chosen Date")
    print(f"Doomsday is a {dayArray[doomsday % 7]}")
    print(f"==============================")
    print(f"{uDay} is a {answer}")
    print(f"==============================")

if __name__ == "__main__":
    uYear = int(input("Year: "))
    uMonth = int(input("Month: "))
    uDay = int(input("Day: "))

    (doomsday, isLeap) = handleYear(uYear)
    monthsDoomsDate = handleMonth(uMonth,isLeap)
    handleDay(uDay)