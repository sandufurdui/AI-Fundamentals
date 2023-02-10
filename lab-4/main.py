from utils import *
import csv

correct_detected = 0
total_images = 0

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header 
    
    for row in reader:
        result = calculate_result(row[0]) 
        expected_result = row[1] 
        if str(result) == str(expected_result):
          correct_detected = correct_detected + 1
        total_images = total_images + 1 

accuracy = correct_detected / total_images
print("{:.2f}%".format(accuracy * 100))