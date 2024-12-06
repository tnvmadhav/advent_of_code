import re

def calculate_multiplication(input: str) -> int:
    ans = 0
    matches = re.findall("mul\([0-9]+,[0-9]+\)", input)
    for match in matches:
        numbers = match[4:len(match)-1].split(",")
        ans += int(numbers[0]) * int(numbers[1])
    return ans

def calculate_conditional_multiplication(input: str) -> int:
    ans = 0
    matches = re.split("don't\(\)+.*?do\(\)+", input)
    for match in matches:
        match = match.split("don't()")[0]
        ans += calculate_multiplication(match)
    return ans

if __name__ == "__main__":

    file_path = '2024/03/03_input_test.txt'
    input = []

    ans = 0
    with open(file_path, 'r') as file:
        for line in file:
            input.append(line)

    print("Sum of muls part 1", calculate_multiplication("".join(input)))

    # Spent hours debugging why without this the output for part 2 is coming short.
    input_new = "".join("".join(input).split("\n"))
    print("Sum of muls part 2", calculate_conditional_multiplication(input_new))