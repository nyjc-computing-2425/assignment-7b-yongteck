# Built-in imports
import math

# Your code below
GRADE = {}
grange = [i-1 for i in [0,40,45,50,55,60,70]]
letter = "USEDCBA"
for i in range(101):
    for a in range(len(grange)):
        if grange[a]<i:
            GRADE[i] = letter[a]

def read_testscores(filename):
    """
    reads a csv file and outputs a list of dictionaries containing the class, name, overall, grade and its corresponding values
    ------
    string filename
        the name of the csv file to be read
    ------
    data
        the lists of dictionaries
    """
    data = []
    with open(filename, "r") as f:
        for i in f:
            parts = f.readline()
            if parts != ['']:
                parts = parts.split(",")
                temp = {}
                temp['class'] = parts[0]
                temp['name'] = parts[1]
                formula = [0,0,0.5,0.75,35/80,2/3]
                temp['overall'] = math.ceil(sum([int(parts[i])*formula[i] for i in range(2,6)]))
                temp['grade'] = GRADE[temp['overall']]
                data.append(temp)
    return data
                
def analyze_grades(studentdata):
    """
    analyzes a list of dictionaries representing the data on students grades and outputs a list of dictionaries representing the number of a certain grade in each class
    ------
    list of dictionaries studentdata
        data on students grades,class,name and overall score
    ------
    list of dictionaries class_data
        a list of dictionaries representing the classes and the number of each grade its students have
    
    """
    class_data = {}
    for i in studentdata:
        if i['class'] not in class_data:
            class_data[i['class']] = {}
            letters = "ABCDESU"
            for a in letters:
                class_data[i['class']][a] = 0
        class_data[i['class']][i['grade']] += 1
    return class_data

#sdata = read_testscores("testscores.csv")
#analysis = analyse_grades(sdata)
