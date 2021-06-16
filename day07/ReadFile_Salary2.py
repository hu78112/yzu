file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
# 進行資料結構化的整理
# [ {'name': John, 'salary':45000}, {'name': Mary, 'salary':55000}...]
employees = []
for row in rows:
    data = row.split(',')
    name = data[0] # 員工姓名
    salary = int(data[1].strip('\n'))
    employee = {'name': name, 'salary': salary} # dict 字典格式
    employees.append(employee)

print(employees)

# 求薪資總和與平均
sum = 0
for employee in employees:
    sum = sum + employee['salary']
avg = sum / len(employees)

print("薪資總和", sum)
print("薪資平均", avg)

# 請問最高薪/低薪人名是?
emp_max = max(employees, key=lambda e: e['salary'])
emp_min = min(employees, key=lambda e: e['salary'])
print(emp_max, emp_max['name'])
print(emp_min, emp_min['name'])
