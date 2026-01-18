# link of the question: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

# better approach
size_of_group = int(input())
all_room_id = list(map(int, input().split()))
unique_set = set()
repeat_set = set()

for i in all_room_id:
    if i in unique_set:
        repeat_set.add(i)
    else:
        unique_set.add(i)

captain_room_id = unique_set - repeat_set
print(captain_room_id.pop())

# brute force
size_of_group = int(input())
all_room_id = list(map(int, input().split()))
unique_room_id = set(all_room_id)

for i in unique_room_id:
    count = 0
    for j in range(len(all_room_id)):
        if i == all_room_id[j]:
            count += 1
            
        if count > 1:
            break
            
    if count == 1:
        print(i)