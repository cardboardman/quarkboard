import os
BlogPath = 'templates/Joe/blogs/'
ProjectsPath = 'templates/Joe/project Code/'
PythonPath = 'templates/Joe/python Code/'

BlogsList = os.listdir(BlogPath)
ProjectsList = os.listdir(ProjectsPath)
PythonList = os.listdir(PythonPath)

for i in xrange(len(BlogsList)):BlogsList[i] = BlogsList[i][:-5]
for i in xrange(len(ProjectsList)):ProjectsList[i] = ProjectsList[i][:-5]
for i in xrange(len(PythonList)):PythonList[i] = PythonList[i][:-5]
