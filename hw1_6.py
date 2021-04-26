first_res = float(input('Сколько пробежал спортсмен в первый раз?'))
cur_res = first_res
end_res = float(input('Каков желаемый результат?'))
day_goal = 1
while cur_res < end_res:
    cur_res *= 1.1
    day_goal += 1
print(day_goal)