import os

def get_input(file):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, file)
    with open(filename, 'r') as input_file:
        return list(map(int, input_file.readlines()))

def get_answer_part1():
    for x in range(0, len(numbers) - 1): 
        for y in range(x + 1, len(numbers)):
            if numbers[x] + numbers[y] == 2020:
                return numbers[x] * numbers[y]
                
def get_answer_part2():
    for x in range(0, len(numbers) - 2): 
        for y in range(x + 1, len(numbers) - 1):
            for z in range(x + 2, len(numbers)):
                if numbers[x] + numbers[y] + numbers[z] == 2020:
                    return numbers[x] * numbers[y]  * numbers[z]

numbers = get_input('dec01.txt')
answer1 = get_answer_part1()
answer2 = get_answer_part2()

print(answer1)
print(answer2)
