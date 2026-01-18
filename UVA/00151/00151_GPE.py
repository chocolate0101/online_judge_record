"""
Power Crisis

UVA 151: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=87
ZeroJudge q891: https://zerojudge.tw/ShowProblem?problemid=q891
GPE 考古: 21944
"""

while True:
    num_region = int(input())
    if num_region == 0:
        break

    region_id = [ _ for _ in range(1, num_region+1)]

    for i in range(1, num_region+1):
        del region_id[0]
        delete_region = 0
        while len(region_id) > 1:
            delete_region = (delete_region+i-1) % len(region_id)
            if region_id[delete_region] == 13:
                break
            del region_id[delete_region]
        
        if len(region_id) == 1:
            print(f"{i}")
            break
        region_id = [ _ for _ in range(1, num_region+1)]