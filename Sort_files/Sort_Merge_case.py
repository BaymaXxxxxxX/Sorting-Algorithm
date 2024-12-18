
import timeit

start_time = timeit.default_timer()
def Merge_sort_revers(a_list):
    n = len(a_list)
    
    if n < 2:
        return a_list

    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    Merge_sort_revers(left)
    Merge_sort_revers(right)

    i = 0  
    j = 0  
    k = 0 

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a_list[k] = right[j]
        j += 1
        k += 1

    return a_list


file = 'tambol'
list_file = []
with open(f'{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
#เริ่ม
list_reversed = Merge_sort_revers(list_file)
# แสดงผล
output_file = f'Result_Sort/{file}_Merge.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")
#วิธี Merge
#amphoe  0.0018896250039688312 วินาที
#mm  0.009294666997448076 วินาที
#province  0.00039316699985647574 วินาที
#tambol  0.011832291005703155 วินาที