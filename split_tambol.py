import timeit
start_time = timeit.default_timer()
#this file is split file tambol to txt
import re
def read_sql_file_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r"\((\d+), '([^']+)', (\d+), '([^']+)', (\d+), '([^']+)'\)"  

    matches = re.findall(pattern, content)
    return matches


files = [
    "tambol.sql"
]

for file_path in files:
    data = read_sql_file_and_process(file_path)
    print(f"Processed data from {file_path}:")
    for row in data[:5]:  
        print(row[0], row[1])
    print("\n")
    
with open('tambol.txt', 'w', encoding='utf-8') as write_province:
  for row in data:
    write_province.write(f"{row[0]} {row[1]}\n")

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")