from collections import defaultdict


def sortByDeadline(jobs):
    for i in range(len(jobs)):
        for j in range(len(jobs)-1):
            if jobs[j][1] > jobs[j+1][1]:
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]


def main():

    jobs = [['a', 2, 100],
            ['b', 1, 19],
            ['c', 2, 27],
            ['d', 1, 25],
            ['e', 3, 15]]

    sortByDeadline(jobs)
    print(jobs)

    selectedJobIndices = defaultdict(int)

    maxTimeFrame = jobs[-1][1]

    for i in range(1, maxTimeFrame+1):
        print(i)
        for job in jobs:
            if job[1] == i and job[2] > selectedJobIndices[i]:
                selectedJobIndices[i] = job[2]

    print(selectedJobIndices)


if __name__ == "__main__":
    main()
