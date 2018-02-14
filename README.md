Course Recommendation System 


This project was done as a part of Statistical Machine Learning Course in Fall 2017 at Arizona State University.

After the initial Data Cleaning part of the project and coming up with a new measure which approximates the rating given by a student in a particular course, called as Satisfiability Measure, we perfomed 3 tasks as a part of the project:

Task 1:
Broadly, ​ based on the average Satisfiability metric of the students enrolled in a particular course,
we came up with a threshold:
1. If the course has a Satisfiability metric greater than the Threshold, then we can give the following suggestions:
	– Increase the number of enrollments in the course
	– tougher course material/make it more challenging and fun learning experience for the students
	– Provide for video recording and making them accessible to public (YouTube etc.)
2. If the course has a Satisfiability metric less than the Threshold, then we can give thefollowing suggestions:
	– Change course Instructor
	– Reduce the difficulty of the course
	– Increase the number of TA’s and recitation sessions for the course, etc.,
	– Increase the Student - Instructor interaction mediums, for example, use of Piazza.

Task 2:
​ For a particular student, based on the courses he took and his ​ Satisfiability metric ​ :
- Recommend the subjects, he/she can choose to major in.
- Provide subjects he/she performed poorly for self-evaluation

The first two tasks were implemented in SML.py.

Task 3:
We recommended courses to students based on the performance of the previous students. Since, we had limitations finding the perfect dataset, with a separate test set and training set, we decided to do K-Cross validation on the existing dataset and calculate the accuracy using the F1 measure.

We decided to use Collaborative Filtering with Nearest Neighbors and the similarity metric we used to compute the nearest neighbor is Euclidean Distance.
This task was implemented in IDEA2KNN.py