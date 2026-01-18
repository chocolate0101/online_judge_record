# solution 1
from itertools import combinations

alphabet = "abcdefghijklmnopqrstuvwxyz"
word_map = {}
index = 1
for length in range(1, 6):
	for combo in combinations(alphabet, length):
		word = "".join(combo)
		word_map[word] = index
		index += 1
		
while True:
	try:
		input_str = input()
	except:
		break
		
	if input_str in word_map:
		print(word_map[input_str])
	else:
		print("0")

# solution 2
from collections import deque

word_map = {}
alphabet_queue = deque()
for ch in range(ord('a'), ord('z') + 1):
	alphabet_queue.append(chr(ch))
	
index = 1
while alphabet_queue:
	current_str = alphabet_queue.popleft()
	word_map[current_str] = index
	index += 1
	
	if len(current_str) == 5:
		continue
	
	current_str_last_chr = current_str[-1]
	for next_chr in range(ord(current_str_last_chr)+1, ord('z') + 1):
		next_str = current_str + chr(next_chr)
		alphabet_queue.append(next_str)
		
while True:
	try:
		input_str = input()
	except:
		break
		
	if input_str in word_map:
		print(word_map[input_str])
	else:
		print("0")