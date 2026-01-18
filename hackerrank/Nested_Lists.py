# link of question：https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    class_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_list.append([name, score])
        
    score = set(item[1] for item in class_list)
    score_list = list(score)
    score_list.sort()
    second_lowest = score_list[1]
    ans_list = []
    for i in range(len(class_list)):
        if second_lowest == class_list[i][1]:
            ans_list.append(class_list[i][0])
            
    ans_list.sort()
    for i in range(len(ans_list)):
        print(ans_list[i])