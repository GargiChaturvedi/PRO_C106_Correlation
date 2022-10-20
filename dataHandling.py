import csv
import numpy as np
import plotly.express as px

studentMarks = []
daysPresent = []

def getDataSource():
    with open('Student Marks vs Days Present.csv') as f:
        global df
        df = csv.DictReader(f)
        for row in df:
            studentMarks.append(float(row['Marks In Percentage']))
            daysPresent.append(float(row['Days Present']))
    
    print("Student Marks: ", studentMarks)
    print("Days Present: ", daysPresent)

def findCorrelation():
    coefficient = np.corrcoef(studentMarks, daysPresent)
    print(coefficient[0, 1])

def plotFigure(data_path):
    with open(data_path) as f:
        global df
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Marks In Percentage", y="Days Present", color="Roll No")
        fig.show()

def setup():
    getDataSource()
    findCorrelation()
    plotFigure("Student Marks vs Days Present.csv")

setup()