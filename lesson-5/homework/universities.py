def enrollment_stats(universities):
    all_student_enrollment = []
    all_tuiton_fee = []
    for each_university in universities:
        all_student_enrollment.append(each_university[1])
        all_tuiton_fee.append(each_university[2])

    return all_student_enrollment, all_tuiton_fee

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]]
 
enrollment, tuition = enrollment_stats(universities)
all_student_number = sum(enrollment)
all_tution_fee_v = sum(tuition)

# Second part: findig mean value and median
# Finding mean
# Mean, median, and mode are different measures of center in a numerical data set. They each try to summarize a dataset with a single number to represent a "typical" data point from the dataset.
# The arithmetic mean is the sum of all of the data points divided by the number of data points.
# \text{mean}=\dfrac{\text{sum of data}}{\text{\# of data points}}

def mean(numbers):
    mean = sum(numbers)/len(numbers)
    return mean

mean_vs = round(mean(enrollment),2)
mean_vt = round(mean(tuition),2)

# Finding median
# Find the median of this data: 1, 4, 2, 4, 0
# There is an odd number of data points, so the median is the middle data point.
# 0, 1, 2, 4, 5. The median is 2.

# Find the median of this data: 10, 40, 20, 50
# Put the data in order first: 10, 20, 40, 50
# There is an even number of data points, so the median is the average of the middle two data points.
# \text{median} = \dfrac{20+40}{2}=\dfrac{60}{2}=30
# The median is 30.


def median(numbers):
    tartib = sorted(numbers)
    lenm = len(tartib)
    mid = lenm // 2

    if lenm % 2 == 0:
        mean = (tartib[mid - 1] + tartib[mid + 1])/2
        return mean
    else:
        return tartib[mid]
    
median_vs = median(enrollment)
median_vt = median(tuition)

print("******************************")
print(f"Total students: {all_student_number}.")
print(f"Total tuition: $ {all_tution_fee_v}\n")
print(f"Student mean: {mean_vs}")
print(f"Student median: {median_vs}\n")
print(f"Tuition mean: $ {mean_vt}")
print(f"Tuition median: $ {median_vt}")
print("******************************")




    
