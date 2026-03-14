'''Problem Statement
An electricity board charges consumers based on units consumed:
First 100 units → ₹5 per unit
Next 200 units → ₹7 per unit
Above 300 units → ₹10 per unit
Calculate total bill amount.'''
 
def calculate_bill(units):
    if(units<=100):
        bill = units*5
    elif(units<=300):
        bill=(100*5)+((units-100)*7)
    else:
        bill=(100*5)+(200*7)+((units-300)*10)
    return bill

# Shopping Cart Stock Checker
    
def process_items( items):
    result = []
    for i in items:
        if i>10:
            result.append("Stock Limit Exceeded")
            break
        elif(i<=0):
            break
        else:
            result.append(f"Item Accepted: {i}")
    return result
items = [2,5,12,4]
# print(process_items(items))
        
#Multi Subject Result System
    
def evaluate_result( marks_list):
    for i in marks_list:
        if(i<35):
            result = "fail"
        avg = sum(marks_list)/5
        if(avg>=75):
            result = "Distinction"
        elif(avg>=60):
            result="First Class"
        elif(avg>=50):
            result="Second Class"
        else:
            result="pass"
    return result
    
#City-wise Revenue Calculation Using Lists and Dictionaries

def city_revenue(orders):
    revenue_dict = {}
    for i in orders:
        city = i["city"]
        amount = i["amount"]
        if city in revenue_dict:
            revenue_dict[city]+=amount
        else:
            revenue_dict[city]=amount
    highest_city = max(revenue_dict,key=revenue_dict.get)
    return { "Revenue per City" :revenue_dict, "Highest Revenue City" : highest_city }

orders = [
    {"order_id": 101, "city": "Delhi", "amount": 5000},
    {"order_id": 102, "city": "Mumbai", "amount": 7000},
    {"order_id": 103, "city": "Delhi", "amount": 1000},

]

print(city_revenue(orders))

#Subject-wise Average Marks Calculator
    
def subject_average( students):
    subject_total = {}
    subject_count = {}
    for student in students:
        marks = student["marks"]
        for subject, score in marks.items():
            if subject in subject_total:
                subject_total[subject]+=score
                subject_count[subject]+=1
            else:
                subject_total[subject]=score
                subject_count[subject]=1
    subject_average={}
    for subject in subject_total:
        subject_average[subject]=subject_total[subject]/subject_count[subject]
    highest_subject = max(subject_average,key=subject_average.get)
    return {
        "Subject Averages":subject_average,
        "Highest Average Subject": highest_subject
    }
students = [
    {"name": "Rahul", "marks": {"Math": 80, "Science": 70}},
    {"name": "Amit", "marks": {"Math": 90, "Science": 60}}
]
# print(subject_average(students))

# Department-wise Patient Count System
    
def department_patient_count(visits):
    dept_count = {}
    for record in visits:
        department = record["department"]
        if department in dept_count:
            dept_count[department]+=1
        else:
            dept_count[department]=1
    max_department = max(dept_count,key = dept_count.get)
    return {
        "Department Patient Count": dept_count,
        "Department with Maximum Patients": max_department
    }

visits = [
    {"patient_id": 1, "department": "Cardiology", "doctor": "Dr. A"},
    {"patient_id": 2, "department": "Orthopedics", "doctor": "Dr. B"},
    {"patient_id": 3, "department": "Cardiology", "doctor": "Dr. C"}
]
# print(department_patient_count(visits))


string = "Learning New Concept"
'''print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
print(string.swapcase())
print(string.find("e"))
print(string.index("o"))
print(string.startswith("N"))
print(string.endswith("w"))
print(string.count("n"))
print(string.isalpha())
print(string.isdigit())
print(string.isalnum())
print(string.isspace())
print(string.isascii())
print(string.replace("New","New and Interesting"))
print(string.strip())
print(string.rstrip())
print(string.lstrip())
print(string.split(","))
print(string.join(","))'''

l1 = ["Python","is","Interesting"]
l2 = [1,23,3]
'''l1.append(l2)
print(l1)
l2.extend(l1)
print(l2)
l1.insert(0,l2)
print(l1)
l1.remove("is")
print(l1)
l1.pop()
print(l1)
l1.clear()
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
print(l1.count("i"))
print(l1.index("is"))'''

t1 = ("Hello","Everyone",1,2)
# print(t1.count("Hello"))
# print(t1.index("Everyone"))

d1 = {1:"ABC",2:"DEF",3:"GHI"}
d2 = {4:5,5:5}
'''print(d1.update(d2))
print(d1.get(2))
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.pop(1))
print(d1.popitem())
print(d1.clear())
print(d1)
print(d1.setdefault(2))'''

s = {1,2,3,4,5,2,1,1,7}
s2 = {1,2,9,8}
'''s.add(6)
print(s)
s.remove(4)
print(s)
s.discard(3)
s.pop()
print(s)
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))
print(s.symmetric_difference(s2))'''

a = 123
'''print(a.bit_count())
print(a.bit_length())
print(a.to_bytes())
b=90.78
print(a.is_integer())'''

'''print(max([1,200,35]))
print(min([100,200,35]))
print(sum([10000,200,35]))
print(max(1,2))
print(sorted([1,2,3,45,654,34,23312]))
print(any(s))
print(all(s))'''

