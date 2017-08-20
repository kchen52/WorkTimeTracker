# Open the text file, read each line, and compile a list of times for each project
fileName = "timeTracker.txt"

# Store the project times in this dict
times = {}

# Returns the time difference between startTime and endTime in minutes
def getTimeDifference(startTime, endTime):
    # Start and end times will be formatted like so
    # 12:00
    # Assume that endTime >= startTime
    hoursDifference = 0
    minutesDifference = 0

    startSplit = startTime.split(":");
    startHour = int(startSplit[0])
    startMinute = int(startSplit[1])

    endSplit = endTime.split(":");
    endHour = int(endSplit[0])
    endMinute = int(endSplit[1])

    hoursDifference = endHour - startHour

    if endMinute < startMinute:
        hoursDifference -= 1
    minutesDifference = endMinute - startMinute
    if minutesDifference < 0:
        minutesDifference = 60 - abs(minutesDifference)
    return (60 * hoursDifference) + minutesDifference

# Takes the times dict as a parameter, and print out all the key/values
def printTimes(times):
    for key, value in times.iteritems():
        print key, value

myFile = open(fileName)
for line in myFile:
    results = line.split()

    # The first line will result in a bad split. Just ignore it
    if (len(results)) < 4:
        continue

    # The following is basically this
    #if (times.containsKey(results[1])) {
    #    // Already has it
    #} else {
    #    // Doesn't have it, add it
    #}

    if times.has_key(results[1]):
        oldTime = times.get(results[1])
        print("oldTime exists. It's:  " + str(oldTime))
        timeDiff = getTimeDifference(results[0], results[3])
        times[results[1]] = oldTime + timeDiff
    else:
        print("Adding " + results[1])
        # Get time difference
        timeDiff = getTimeDifference(results[0], results[3])
        times[results[1]] = timeDiff
printTimes(times)
