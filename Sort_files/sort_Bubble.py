import timeit

start_time = timeit.default_timer()
def Bubble_sort_revers(a_list):
    n = len(a_list)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            #swap
            if a_list[j] < a_list[j+1] :
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                flag = 1
        if flag == 0:
            break
    return a_list



file = 'tambol'
list_file = []
with open(f'{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
#เริ่ม
list_reversed = Bubble_sort_revers(list_file)
# แสดงผล
output_file = f'result_sort/{file}_Bubble.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")
#วิธี Bubble
#amphoe  0.032537082995986566 วินาที
#mm  1.1037465420013177 วินาที
#province  0.0010177500007557683 วินาที
#tambol  1.9172543329987093 วินาที
