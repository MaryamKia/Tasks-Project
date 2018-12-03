import datetime
import csv
import os

tasks_list = []
max_id = 0
if os.path.isfile('tasks.csv'):
    with open('tasks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for task in reader:
            tasks_list.append(dict(task))
        max_id = int(max(task['id'] for task in tasks_list))
        print(max_id)
next_id = max_id + 1
while True:
    user_demand = input('"p": previous tasks, "n": new tasks, "e": to edit date of a task,'
                        '"x": exit: ')

    if user_demand not in 'pnex':
        print('you should enter "p" or "n" or "e"')
    elif user_demand == 'p':
        if not tasks_list:
            print('there is not any defined task.')
        else:
            for task in tasks_list:
                print(task['id'], task['user_name'], task['task_summery'], task['task_date'], task['duration'])
    elif user_demand == 'n':
            task_info = {}
            user_name = input('first_last: ')
            task_summery = input('task_summery: ')
            t = input('yyyy/mm/dd: ')
            task_date = datetime.datetime.strptime(t, '%Y/%m/%d')
            till_date = task_date - datetime.datetime.today()
            task_info['id'] = next_id
            task_info['user_name'] = user_name
            task_info['task_summery'] = task_summery
            task_info['task_date'] = task_date.date()
            task_info['duration'] = till_date.days
            tasks_list.append(task_info)
            next_id += 1
            see_arrange = input('do you want to see arrange_tasks(y/n): ')
            if see_arrange == 'y':
                arrange_tasks = sorted(tasks_list, key=lambda x: x['duration'])
                print(arrange_tasks)
            else:
                continue

    elif user_demand == 'e':
        edit_task_id = input('task id: ')
        find_tasks = [task for task in tasks_list if task['id'] == edit_task_id]
        if not find_tasks:
            print('invalid id')
            continue
        find_task = find_tasks[0]
        print(find_task)
        find_task['task_date'] = input('yyyy/mm/dd: ')
        # calculate duration again!
        task_date = datetime.datetime.strptime(find_task['task_date'], '%Y/%m/%d')
        till_date = task_date - datetime.datetime.today()
        find_task['duration'] = till_date.days
        print(find_task)
    elif user_demand == 'x':
        break

with open('tasks.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'user_name', 'task_summery', 'task_date', 'duration']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for task in tasks_list:
        writer.writerow(task)

