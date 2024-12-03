
def is_monotonic(report_list):
    safe_count = 0
    for report in report_list:
        safe = True
        increasing = False
        if len(report) > 0 and int(report[0]) < int(report[1]):
            increasing = True
        for level in range(1, len(report)):
            diff = int(report[level]) - int(report[level-1])
            if increasing:
                if diff < 1 or diff > 3:
                    safe = False
                    break
            else:
                if diff > -1 or diff < -3:
                    safe = False
                    break
        if safe:
            safe_count += 1
    return safe_count

def calculate_damped_safety(report_list):
    safe_count = 0
    for report in report_list:
        if is_monotonic([report]) == 1:
            safe_count += 1
            continue

        for i in range(len(report)):
            if is_monotonic([report[:i] + report[i+1:]]) == 1:
                safe_count += 1
                break
    return safe_count


if __name__ == "__main__":
    
    left, right = [], []

    file_path = '2024/02/02_input.txt'
    input = []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            input.append(columns)
            

    print("Safe Reports", calculate_damped_safety(input))
