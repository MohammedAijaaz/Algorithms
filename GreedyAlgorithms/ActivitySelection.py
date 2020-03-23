import random


def sortByEndTime(startTimes, endTimes):
    for i in range(len(endTimes)):
        for j in range(len(endTimes)-1):
            if endTimes[j] > endTimes[j+1]:
                endTimes[j], endTimes[j+1] = endTimes[j+1],  endTimes[j]
                startTimes[j], startTimes[j +
                                          1] = startTimes[j+1],  startTimes[j]


def shuffleActivities(startTimes, endTimes):
    print("Before Shuffiling: ", startTimes, endTimes)
    for i in range(10):
        randomIndex1 = random.randint(0, len(startTimes)-1)
        randomIndex2 = random.randint(0, len(startTimes)-1)

        startTimes[randomIndex1], startTimes[randomIndex2] = startTimes[randomIndex2], startTimes[randomIndex1]
        endTimes[randomIndex1], endTimes[randomIndex2] = endTimes[randomIndex2], endTimes[randomIndex1]
    print("After Shuffling: ", startTimes, endTimes)


def main():

    startTimes = [1, 3, 0, 5, 8, 5]
    endTimes = [2, 4, 6, 7, 9, 9]

    shuffleActivities(startTimes, endTimes)
    sortByEndTime(startTimes, endTimes)
    print(startTimes, endTimes)

    selectedAcitivities = []
    selectedAcitivities.append(0)

    for i in range(1, len(startTimes)):
        currentActivity = {
            'startTime': startTimes[i],
            'endTime': endTimes[i]
        }
        previousActivityIndex = selectedAcitivities[len(selectedAcitivities)-1]
        previousActivity = {
            'startTime': startTimes[previousActivityIndex],
            'endTime': endTimes[previousActivityIndex]
        }

        if previousActivity["endTime"] <= currentActivity["startTime"]:
            selectedAcitivities.append(i)

    print(selectedAcitivities)


if __name__ == "__main__":
    main()
