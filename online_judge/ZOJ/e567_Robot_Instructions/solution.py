# link of the question: https://zerojudge.tw/ShowProblem?problemid=e567

num_test_case = int(input())

for i in range(num_test_case):
    num_instruction_per_case = int(input())
    position = 0
    history_instruction = []
    for j in range(num_instruction_per_case):
        current_instruction = input().split()
        if current_instruction[0] == "LEFT":
            position -= 1
        elif current_instruction[0] == "RIGHT":
            position += 1
        else:
            tmp_instruction = history_instruction[int(current_instruction[2])-1]
            if tmp_instruction == ["LEFT"]:
                position -= 1
                current_instruction = ["LEFT"]
            else:
                position += 1
                current_instruction = ["RIGHT"]
        history_instruction.append(current_instruction)
    print(position)