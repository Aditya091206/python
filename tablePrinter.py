print("name:aditya.M,USN:1AY24AI004,sec:'M")

def print_table(table_data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]
    
    for row in table_data:
        for i, item in enumerate(row):
            print(str(item).rjust(col_widths[i]), end=' ')
        print()  

table = [
    ["name", "age", "city"],
    ["alice", 30, "new york"],
    ["bob", 25, "los angeles"],
    ["charlie", 35, "chicago"]
]

print_table(table)
