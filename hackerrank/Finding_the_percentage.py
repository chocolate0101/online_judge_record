# link of the question：https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total_score = 0
    length = 0
    for name in student_marks:
        if name == query_name:
            length = len(student_marks[name])
            for i in range(len(student_marks[name])):
                total_score += student_marks[name][i]
                
    print(f"{total_score / length:.2f}")