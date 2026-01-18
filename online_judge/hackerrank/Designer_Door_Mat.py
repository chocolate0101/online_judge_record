# link of the question：

n, m = map(int, input().split())

# 上半部
for i in range(n // 2):
    # 計算圖案的寬度：(2*i + 1) 個 .|.，每個 .|. 有 3 個字元
    pattern_width = (2 * i + 1) * 3
    pattern = '.|.' * (2 * i + 1)
    padding_count = (m - pattern_width) // 2
    
    print('-' * padding_count + pattern + '-' * padding_count)

# WELCOME 部分
welcome_padding = (m - 7) // 2
print('-' * welcome_padding + 'WELCOME' + '-' * welcome_padding)

# 下半部
for i in range(n // 2 - 1, -1, -1):
    pattern_width = (2 * i + 1) * 3
    pattern = '.|.' * (2 * i + 1)
    padding_count = (m - pattern_width) // 2
    
    print('-' * padding_count + pattern + '-' * padding_count)