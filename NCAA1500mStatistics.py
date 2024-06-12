import csv
import math
from decimal import Decimal

filepath = 'C:/RunningCoding/Running-Statistics-NCAA/Top500NCAA1500mStatsMen.csv'
#Change the filepath To Change Data
#Small Men: 'C:/RunningCoding/Running-Statistics-NCAA/Top100NCAA1500mStatsMen.csv'
#Large Men: 'C:/RunningCoding/Running-Statistics-NCAA/Top500NCAA1500mStatsMen.csv'
#Small Women: 'C:/RunningCoding/Running-Statistics-NCAA/Top100NCAA1500mStatsWomen.csv'
#Large Women: 'C:/RunningCoding/Running-Statistics-NCAA/Top500NCAA1500mStatsWomen.csv'

def AverageTimesMen():
    CombinedTimes = 0
    RunnersUnder4Minutes = []
    count = 0
    under4Count = 0
    with open(filepath, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            (m, s) = row[5].split(":")
            result = Decimal(m) * 60 + Decimal(s)
            CombinedTimes += result 
            count+=1
            if (result<Decimal(222.21)):
                RunnersUnder4Minutes.append(row)
                under4Count+=1
    finalAverage = CombinedTimes/count
    Seconds = finalAverage%60
    Minutes = math.floor(finalAverage/60)
    AverageTime = f"Average Time: {Minutes}:{round(Seconds,2)}\n"
    PercentageOfRunnersUnder4 = f"\nPercentage Under 4 Minute Mile Equivalent: {round(((under4Count/count)*100),2)}%\n"
    NumberOfRunnersUnder4 = f"\n# of Runners Under 4 Minute Mile Equivalent: {under4Count} out of {count}"
    return AverageTime + PercentageOfRunnersUnder4 + NumberOfRunnersUnder4

def AverageTimesWomen():
    CombinedTimes = 0
    RunnersUnderBarrier = []
    count = 0
    underBarrierCount = 0
    with open(filepath, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            (m, s) = row[5].split(":")
            result = Decimal(m) * 60 + Decimal(s)
            CombinedTimes += result 
            count+=1
            if (result<Decimal(259.25)):
                RunnersUnderBarrier.append(row)
                underBarrierCount+=1
    finalAverage = CombinedTimes/count
    Seconds = finalAverage%60
    Minutes = math.floor(finalAverage/60)
    AverageTime = f"Average Time: {Minutes}:{round(Seconds,2)}\n"
    PercentageOfRunnersUnder430 = f"\nPercentage Under 4:40 Mile Equivalent: {round(((underBarrierCount/count)*100),2)}%\n"
    NumberOfRunnersUnder430 = f"\n# of Runners Under 4:40 Mile Equivalent: {underBarrierCount} out of {count}"
    return AverageTime + PercentageOfRunnersUnder430 + NumberOfRunnersUnder430

def AgeOfTopFinishers():
    CountFreshman = 0
    totalRankFR = 0
    CountSophomore = 0
    totalRankSO = 0
    CountJunior = 0
    totalRankJR = 0
    CountSenior = 0
    totalRankSR = 0
    totalRunners = 0
    teams = {}
    with open(filepath, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            totalRunners+=1
            if (row[3]=='FR-1'):
                CountFreshman+=1
                totalRankFR+=int(row[0])
            if (row[3]=='SO-2'):
                CountSophomore+=1
                totalRankSO+=int(row[0])
            if (row[3]=='JR-3'):
                CountJunior+=1
                totalRankJR+=int(row[0])
            if (row[3]=='SR-4'):
                CountSenior+=1
                totalRankSR+=int(row[0])
    NumberOfRunner= f"\n# of Runners: {totalRunners}\n"
    NumberOfAgesForRunners= f"\n# of Freshman: {CountFreshman}\n# of Sophomore: {CountSophomore}\n# of Junior: {CountJunior}\n# of Senior: {CountSenior}\n"
    AverageRankOfEachClass= f"\nAvg Rank Of Freshman: {round(totalRankFR/CountFreshman,2)}\nAvg Rank Of Sophomore: {round(totalRankSO/CountSophomore,2)}\nAvg Rank Of Junior: {round(totalRankJR/CountJunior,2)}\nAvg Rank of Senior: {round(totalRankSR/CountSenior,2)}\n"
    finalValues=NumberOfRunner + NumberOfAgesForRunners + AverageRankOfEachClass
    return finalValues
        
finalMen=AverageTimesMen()
finalWomen=AverageTimesWomen()
Ages=AgeOfTopFinishers()
if (filepath=='C:/RunningCoding/Running-Statistics-NCAA/Top100NCAA1500mStatsMen.csv'):
    print("Top 100 NCAA Men 1500m Runners")
    print(Ages)
    print(finalMen)
if (filepath=='C:/RunningCoding/Running-Statistics-NCAA/Top500NCAA1500mStatsMen.csv'):
    print("Top 500 NCAA Men 1500m Runners")
    print(Ages)
    print(finalMen)
if (filepath=='C:/RunningCoding/Running-Statistics-NCAA/Top100NCAA1500mStatsWomen.csv'):
    print("Top 100 NCAA Women 1500m Runners")
    print(Ages)
    print(finalWomen)
if (filepath=='C:/RunningCoding/Running-Statistics-NCAA/Top500NCAA1500mStatsWomen.csv'):
    print("Top 500 NCAA Women 1500m Runners")
    print(Ages)
    print(finalWomen)