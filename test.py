from collections import deque
import itertools

def solution(sales, links):
    answer = 0
    graph = [[] for _ in range(len(sales))]

    for li in links:
        graph[li[0] - 1].append(li[1] - 1)

    q = deque()
    q.append(0)

    teams = []

    while q:
        team = []
        ver = q.popleft()
        team.append(ver)

        for i in graph[ver]:
            team.append(i)
            q.append(i)

        teams.append(team)

    rteams = []

    for t in teams:
        if len(t) > 1:
            rteams.append(t)

    combs = list(itertools.product(*rteams))

    sums = []

    for comb in combs:
        tmp_comb = set(list(comb))
        sum = 0
        for idx in tmp_comb :
            sum += sales[idx]

        sums.append(sum)

    answer = min(sums)

    return answer

if __name__ == "__main__":
    a = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    b = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(a,b))



'''
from string import ascii_lowercase
import re

def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계

    dic = list(ascii_lowercase) + [str(x) for x in range(0, 10)] + ['-', '_', '.']
    temp_id = ""

    for i in range(len(new_id)):
        if new_id[i] in dic:
            temp_id += new_id[i]

    # 3단계
    while '..' in temp_id:
        temp_id = temp_id.replace('..','.')

    # 4단계
    if temp_id.startswith('.'):
        temp_id = temp_id[1: len(temp_id)]
    if temp_id.endswith('.'):
        temp_id = temp_id[0: len(temp_id)-1]

    # 5단계
    temp_id = 'a' if len(temp_id) == 0 else temp_id

    # 6단계
    if len(temp_id) >= 16:
        temp_id = temp_id[0: 15]
        temp_id = temp_id[0:len(temp_id)-1] if temp_id.endswith('.') else temp_id

    # 7
    if len(temp_id) <= 2:
        while len(temp_id) == 3:
            temp_id += temp_id[-1]

    answer = temp_id

    return answer

if __name__ == "__main__":
    result = solution("...!@BaT#*..y.abcdefghijklm")
'''

'''
from itertools import combinations as comb
from collections import Counter

def solution(orders, course):
    answer = []

    for co in course:
        temp = []
        for order in orders:
            temp += (list(comb(order, co)))

        all = []

        for te in temp:
            all.append(''.join(sorted(te)))

        count = Counter(all)

        for key, value in count.items():
            if value == max(count.values()) and value >= 2:
                answer.append(key)

    return sorted(answer)
        
    
    return answer

'''

'''
def solution(info, query):
    answer = []
    
    for need in query :
        count = 0 # 이번 니즈에 맞는사람 초기화
        tl = list(map(str, need.split(" ")))
        need_list = [tl[0],tl[2],tl[4],tl[6],tl[7]]
        
        for fo in info :
            ok = [-1] * 5
            fo_list = list(map(str, fo.split(" ")))
            
            for i in range(0,5) :
                if 0 in ok:
                    break
                
                if 0 <= i <= 3 :
                    if need_list[i] == "-":
                        ok[i] = 1
                    else:
                        ok[i] = 1 if need_list[i] == fo_list[i] else 0
                if i == 4 :
                    ok[i] = 1 if int(need_list[i]) <= int(fo_list[i]) else 0
    
            count += 1 if sum(ok) == 5 else 0
        
        answer.append(count)         
        
    return answer
'''