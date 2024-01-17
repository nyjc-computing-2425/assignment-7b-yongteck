# Assignment 7b: Score and grade calculation

The file `testscores.csv` contains test scores for a cohort of students. The first row contains header names.

## Part 1: Score to grade mapping

**Generate** a `dict`, `GRADE`, that has score 0-100 (`int`) as keys, and the appropriate grade as values.  
You may use a `for` or `while` loop.

The letter grade for each score range is as follows:

    A:      score >= 70
    B: 70 > score >= 60
    C: 60 > score >= 55
    D: 55 > score >= 50
    E: 50 > score >= 45
    S: 45 > score >= 40
    U: 40 > score
    
### Expected output

    >>> GRADE[30]
    'U'
    >>> GRADE[55]
    'C'
    >>> GRADE[69]
    'B'

## Part 2: File reading and score calculation

Write a function `read_testscores(filename)` that:
1. Takes a string `filename`
2. Reads in data from the file `filename` in CSV format
3. Represents each row's data as a dict with the following keys:
   - `'class'`
   - `'name'`
   - `'overall'`
   - `'grade'`
4. Calculates the overall score of each student (see calculation formula below) and stores it under the `'overall'` key
5. Determines the grade of each student and stores it under the `'grade'` key.
6. Returns a `list` of `dict`s, each `dict` representing row data for a single student

You are recommended to store the scores for P1 to P4 as a quadruple (a 4-element `tuple`) instead of under separate `'p1'` to `'p4'` keys, for easier retrieval.  

### Overall score calculation formula

The overall score is calculated using the following formula:

    overall = (p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20)
    
Where `p1`, `p2`, `p3`, and `p4` are the scores for P1, P2, P3, and P4 respectively.  
The overall score is to be **rounded up** to the nearest integer. You may use the `ceil()` function from the `math` module to do this.

### Expected output

    >>> studentdata = read_testscores('testscores.csv')
    >>> studentdata[0]['class']
    'Class1'
    >>> studentdata[0]['name']
    'Student1'
    >>> studentdata[0]['overall']
    51
    >>> studentdata[0]['grade']
    'D'

## Part 3: Grade analysis

Write a function, `analyze_grades(studentdata)` which takes the student data and returns a dict representing the count of each grade for each class, i.e. how many A, B, C, D, E, S and U each class has.

### Expected output

    >>> analysis = analyze_grades(studentdata)
    >>> analysis['Class1']['A']
    4
    >>> analysis['Class18']['U']
    0

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.

