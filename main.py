import matplotlib.pyplot as plt
import numpy as np

full_notes = []
mt1 = []
mt2 = []
final = []
lab = []
hw =[]
att = []

with open("data9_me.csv","r") as f:
    data = f.read().split("\n")
    data.pop(0)
    data.pop(-1)

    for i in data:
        a = i.split(";")
        full_notes.append(a)

    for i in range(len(full_notes)):

        for j in range(len(full_notes[0])):

            full_notes[i][j] = int(full_notes[i][j])

    for i in range(len(full_notes)):
        mt1.append(full_notes[i][0])
        mt2.append(full_notes[i][1])
        final.append(full_notes[i][2])
        lab.append(full_notes[i][3])
        hw.append(full_notes[i][4])
        att.append((full_notes[i][5]))

def mean(a):
    return sum(a)/len(a)

def median(a):
    a = sorted(a)
    if len(a)%2 == 0:
        return (a[int((len(a)/2))]+a[int((len(a)/2) -1)])/2
    else:
        return a[int((len(a)/2))]

def std(a):
    dvs = []
    mn = mean(a)
    for x in a:
        dvs.append((x-mn)**2)
    variance = sum(dvs)/len(a)
    return (variance)**(1/2)

def skew(a):
    mode = list(set(filter(lambda x: a.count(x) == max(list(map(a.count, a))), a)))[0]
    if mean(a) > mode:
        return "Skew Positive"
    elif mean(a) < mode:
        return "Skew negative"
    else:
        return "Skew Symmetric"

def main():
    all_notes = [mt1,mt2,final,lab,hw,att]
    all_notes_names = ["Midterm 1","Midterm 2","Final","Lab","Homeworks","Attendance"]

    for i in range(len(all_notes)):
        print("Statistical Values For", all_notes_names[i])
        print("")
        print("Mean of  the " , all_notes_names[i], " = ", mean(all_notes[i]))
        print("Median of  the " , all_notes_names[i], " = ", median(all_notes[i]))
        print("Standart Deviation of  the " , all_notes_names[i], " = ", std(all_notes[i]))
        print("Skew of  the " , all_notes_names[i], " = ", skew(all_notes[i]))
        print("")
        print("---------")
        print("")

main()