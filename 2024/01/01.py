from collections import Counter

def calculate_distance(left, right):
    ans = 0

    left.sort()
    right.sort()

    for i, j in zip(left, right):
       ans += abs(int(i) - int(j)) 
    
    return ans

def calculate_similarity(left, right):
    ans = 0

    right_counter = Counter(right)
    for c in left:
        ans += right_counter[c] * int(c)

    return ans

if __name__ == "__main__":
    
    left, right = [], []

    file_path = '01_input.txt'

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) >= 2:
                left.append(columns[0])
                right.append(columns[1])

    print("Distance", calculate_distance(left, right))
    print("Similarity Score", calculate_similarity(left, right))