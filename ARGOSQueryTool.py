# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: John Fay (john.fay@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "Sara_noheaders.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))
    
# Close the file object
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

# Use a for loop to read each line, one at a time, until the list is exhausted
for lineString in lineStrings:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    #filter out bad data

    if obsLC in ("1","2","3"):
         # Add values to dictionary
        dateDict[recordID] = obsDate   
        locationDict[recordID] = (obsLat, obsLon) 

# Indicate script is complete
print ("Finished")


# ask for a date

    input("enter a date (M/D/YYYY:")

    #

    if not "/" in userDate:
    print("wrong format")

    # create empty key list

    keyList = []

    # loop through the date dictionary

    for k,v in dateDict.items():
        # see if the date matches th user date
        if v == userDate:
            keyList.append(k)

    for key in keyList:
        print(locationDict[key])
