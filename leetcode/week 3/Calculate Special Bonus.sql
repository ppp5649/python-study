SELECT employee_id, IF('employee_id' % 2 != 0 and 'name' like 'M%', salary, 0) as bonus
FROM Employees