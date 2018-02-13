# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:48:22 2017

@author: Saiteja Sirikonda
@Course: Statistical Machine Learning, Fall 2017
Arizona State University

There are two functions implemented in this script:

1. First one - Recommends if the University needs to increase the resources
allocated to the Course or act accordingly based on the Average Satisfiability
Metric of students who took the course.

2. Second One - Recommends major a student after the courses he's taken in his
Freshman year based on his Satisfiability Metric Values for each course.


"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import math
#with open('filteredData.csv','rb') as csvFile:
    #reader = csv.reader(csvFile)
    #for _ in xrange(2):
        #print reader.next()


def Resources_for_Course():
    subjects,finalAvgMetric = {},{}
    with open('filteredData.csv','rb') as csvFile:
        reader = csv.reader(csvFile)       
        
        for row in reader:       
            if row[0] == "course_id": continue
            if row[0] not in subjects:
                subjects[row[0]] = [float(row[21]),1]
            else:
                subjects[row[0]][0] += float(row[21])
                subjects[row[0]][1] += 1
        #for i in subjects.values():
        #   print i
        for i in subjects.keys():
            #print subjects[i][0], subjects[i][1]
            finalAvgMetric[i] = (subjects[i][0]/subjects[i][1])*100.0
        #temp = sorted(final.values())
        #for i in temp: print i*100
        n_groups = range(len(finalAvgMetric.values()));
        threshold = np.percentile(finalAvgMetric.values(),60)
        print threshold
        above_threshold = np.maximum(np.asarray(finalAvgMetric.values()) - threshold, 0)
        below_threshold = np.minimum(np.asarray(finalAvgMetric.values()), threshold)
        print np.asarray(finalAvgMetric.values())
        fig, ax = plt.subplots()
        ax.bar(n_groups, below_threshold, 0.5, color="b")
        ax.bar(n_groups, above_threshold, 0.5, color="orange",bottom=below_threshold)
        
        # horizontal line indicating the threshold
        ax.plot([0.,16], [threshold, threshold], "k--",label="Course Avg Satisfiability Metric")
        plt.legend('upper-right')
        plt.xlabel("Course Satisfaction")
        fig.savefig("look-ma_a-threshold-plot.png", dpi=400)
        
        # and plot it
        
        
                           
def Stream_recommendation():
    users = {}
    with open('filteredData.csv','rb') as csvFile:
        reader = csv.reader(csvFile)       
        uniquevalues = []
        for row in reader:
            if row[0] == "course_id": continue
            if row[0] not in uniquevalues:
                uniquevalues.append(row[0])
            
        print len(uniquevalues)
        course_thresholds = {}
        
        for i in uniquevalues:
            csvFile.seek(0)
            course_satis = []
            #print "theihe"
            for row in reader:
                #print row
                if row[0] == "course_id": continue
                elif row[0] == i:
                    #print "the case is getting in", row[21]
                    course_satis.append(float(row[21]))
                    
                else: continue
            #print len(course_satis), np.percentile(np.asarray(course_satis),25)
            lower,upper = np.percentile(course_satis,40),np.percentile(course_satis,95)            
            course_thresholds[i] = [round(lower,3),round(upper,3)]    
        print course_thresholds
        csvFile.seek(0)
        for row in reader:
            if row[0] == "course_id": continue
            if row[1] not in users:
                if round(float(row[21]),3) <= course_thresholds[row[0]][0]:
                    users[row[1]] = [[(row[0],round(float(row[21]),3))], []]
                if round(float(row[21]),3) >= course_thresholds[row[0]][1]:
                    users[row[1]] = [[], [(row[0],round(float(row[21]),3))]]
            else:
                if round(float(row[21]),3)<=course_thresholds[row[0]][0]:
                    users[row[1]][0].append((row[0],round(float(row[21]),3)))
                if round(float(row[21]),3) >= course_thresholds[row[0]][1]:
                    users[row[1]][1].append((row[0],round(float(row[21]),3)))
        print "thresholds", course_thresholds        
        count = 0
        for key in users:
            if count < 10:
                print "the dictionary", key, users[key]
            count +=1
        print len(users)
        
        
            

Stream_recommendation()
                
        
        
    
    
             
             
        
            
        
        
    