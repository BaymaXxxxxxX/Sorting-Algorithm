import timeit
start_time = timeit.default_timer()

import re
def read_sql_file_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r"\((\w+), '([^']+)', (\w+), '([^']+)'\)"  
    matches = re.findall(pattern, content)
    return matches


files = [
    "amphoe.sql"
]

for file_path in files:
    data = read_sql_file_and_process(file_path)
    print(f"Processed data from {file_path}:")
    for row in data[:5]:  
        print(row[0], row[3])
    print("\n")
    
with open('amphoe.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[3]}\n")

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")