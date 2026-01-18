# link of the question：https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count += 1
    return count

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        k = i
        for j in range(len(sub_string)):
            if k > len(string) - 1:
                break
            elif sub_string[j] == string[k]:
                k += 1
                if j == len(sub_string)-1:
                    count += 1
            else:
                break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)