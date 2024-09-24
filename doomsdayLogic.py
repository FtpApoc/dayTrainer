
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
    centArray = [2,0,5,3]
    answer = (math.floor(uYear/100) - 20) % 4 
    centuryDoomsDay = centArray[answer]

    return(centuryDoomsDay)

def handleCenturyOctant(uYear):
    centNum = uYear % 100

    centOctant,centRemainder = divmod(centNum,12)

    centLeaps = math.floor(centRemainder / 4)
    
    return (centOctant, centRemainder, centLeaps)

def handleYear(uYear):
    centuryDoomsDay = handleCentury(uYear)

    yearsPast = uYear % 100
    leapYearsPast = math.floor(yearsPast / 4)
    
    answer = centuryDoomsDay + yearsPast + leapYearsPast

    isLeap = handleLeap(uYear)

    return {answer,leapYearsPast,isLeap}
    

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

def handleDay(uDay,doomsday,doomsdate):
    
    dayArray = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    offset = uDay - doomsdate
    answer = dayArray[(doomsday + offset) % 7]

    return offset,answer

if __name__ == "__main__":
    print("Hello World")