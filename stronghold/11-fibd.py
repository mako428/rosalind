# Given: Positive integers n≤100 and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# if rabbits live for three months they reproduce only twice before dying
# (lifespan - 1 = number of offspring pairs)

# example:
# 3 month life, 1 pair: 1, 1, 2, 2, 3, 4, 5
# 4 month life, 1 pair: 1, 1, 2, 3, 4, 6, 9, 13, 19
# 5 month life, 1 pair: 1, 1, 2, 3, 5, 7, 11

# 3 month life, 2 pair: 1, 1, 3, 4, 8, 8

# based on code from 04-fib.py

n = int(input("Enter number of months:"))
p = int(input("Enter number of pairs per generation:"))
m = int(input("Enter lifespan in months:"))

sequence = [1,1] 
while n > len(sequence):
    if len(sequence) < m :
            sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2]*p) # sequence[len(sequence)-1] + p)
    else:
        new = 0
        for x in range(len(sequence)-m, len(sequence)-1) :
            # print(x)
            new = new + sequence[x]
        sequence.append(new)
        # sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2]*p - sequence[len(sequence)-(m)])
    # print(sequence)    
if len(sequence) >= n :
    print('Final:',sequence[n-1])
    print('Final:',sequence) 

"""
# trying a different approach with age counters...
start_n = 1
# create dictionary of each month in sequence
main = dict()
while n > len(sequence):
    # each month key in main dict has a value dictionary of ages of rabbits on the given month
    main[f'month {len(sequence)}'] = dict()
    for range in m :
        main[f'month {len(sequence)}'][range(m)] = 
 """

""" # just trying to get the counter loop to work
# it seems to work, but its really inefficient past month 25, too much compute time
# need to find the pure math equation
id_ages = dict()
id_alive_status = dict()
id_ages[1] = 0
month_id = 0
unique_id_list = [1]
sequence = []
while n > len(sequence):
    month_id = month_id + 1
    print(f'----- Month {month_id} -----')
    monthly_count = 0
    # print('Starting ids:',unique_id_list)
    for id in unique_id_list :
        # print('id:',id)
        if id not in id_ages or id not in id_alive_status :
            id_ages[int(f'{id}')] = 0
            id_alive_status[int(f'{id}')] = True
        # if id_ages[f'{id}'] == 0 :
        #     continue
        # if id_ages[f'{id}'] == 1 :
        #     continue
        if id_ages[int(f'{id}')] >= 2 and id_ages[int(f'{id}')] <= m :
            monthly_count = p
        # if id_ages[int(f'{id}')] == m + 1 :
        #     # monthly_count += k
        #     id_alive_status[int(f'{id}')] = False
        if id_ages[int(f'{id}')] >= m :
            id_alive_status[int(f'{id}')] = False
        # print(p)
        # print('monthly count:',monthly_count)
        if monthly_count > 0 :
            # print(range(max(unique_id_list) + 1, max(unique_id_list) + monthly_count + 1))
            for i in range(max(unique_id_list) + 1, max(unique_id_list) + monthly_count + 1) :
                # print(i,'<--- new id')
                unique_id_list.append(i)
                # print('unique ids:',unique_id_list)
                monthly_count = 0
            
    alive_count = 0
    for k, v in id_alive_status.items() :
        if v == True :
            alive_count += 1
    # print('unique ids:',unique_id_list)
    # print('id_ages:',id_ages)
    # print('id_alive_status:',id_alive_status)
    sequence.append(alive_count)
    print('sequence:',sequence)
    print('----- END MONTH -----\n')
    for id in unique_id_list :
        id_ages[int(f'{id}')] = id_ages[int(f'{id}')] + 1

print(max(sequence))
print(sequence[len(sequence)-1]) """