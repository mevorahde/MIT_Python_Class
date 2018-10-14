# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:37:48 2018

@author: Owner
"""

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  total = total / (len(numbers))
  return total

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return(.1 * homework + .3 * quizzes + .6 * tests)

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score < 90 and score >= 80:
    return "B"
  elif score < 80 and score >= 70:
    return "C"
  elif score < 70 and score >= 60:
    return "D"
  else:
    return "F"

    
def get_class_average(students):
  results = []
  for student in students:
    results.append(get_average(student))
  return average(results)

print('Lloyd\'s letter grade is: ' + get_letter_grade(get_average(lloyd)))
print('Alice\'s letter grade is: ' + get_letter_grade(get_average(alice)))
print('Tyler\'s letter grade is: ' + get_letter_grade(get_average(tyler)))
print('\n')
class_list = [lloyd, alice, tyler]
print('The class average is: ' + str(get_class_average(class_list)) +'.')
print('The class average letter grade is a: ' + str(get_letter_grade(get_class_average(class_list))) +'.')



    

  
  