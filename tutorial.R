MyData <- read.csv(file="titanic.csv", header=TRUE, sep=",")

#6
print(MyData)
summary(MyData)

#7
#this is the column names in the csv file:
names(MyData) 

#values for first two columns:
MyData$PassengerId,MyData$Survived

#Table for dist of genders:
table(MyData$Sex)


#8 lost here....


