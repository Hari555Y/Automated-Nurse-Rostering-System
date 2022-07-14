import sys
import pandas as pd
import json

def sched(N, D, m, a, e):
    scd = [[[],[],[]] for i in range(D)]
    times = [0 for i in range(N)]
    all_nurse = [['R' for i in range(D)] for j in range(N)]
    for i in range(D):
        if i%7==0:
            times = [0 for p in range(N)]
        for j in range(3):
            posb = set(range(N))
            if j==0:
                if i!=0:
                    prv_morn = scd[i-1][0]
                    prv_even = scd[i-1][2]
                    for z in prv_morn:
                        posb.discard(z)
                    for z in prv_even:
                        posb.discard(z)
            elif j==1:
                cur_morn = scd[i][0]
                for z in cur_morn:
                    posb.discard(z)
            else:
                cur_morn = scd[i][0]
                cur_aft = scd[i][1]
                for z in cur_morn:
                    posb.discard(z)
                for z in cur_aft:
                    posb.discard(z)
            arr = []
            num = m
            if j==1:
                num = a
            if j==2:
                num = e
            for z in posb:
                arr.append(z)
            arr.sort(key=lambda x: times[x])
            if num>len(arr) or times[arr[num-1]]>=6:
                return "NO-SOLUTION"
            for k in range(num):
                scd[i][j].append(arr[k])
                times[arr[k]] += 1
                if j==0:
                    all_nurse[arr[k]][i] = 'M'
                elif j==1:
                    all_nurse[arr[k]][i] = 'A'
                else:
                    all_nurse[arr[k]][i] = 'E'
    return all_nurse

def schedule(N, D, m, a, e, S, T):
    scd = [[[],[],[]] for i in range(D)]
    times = [0 for i in range(N)]
    all_nurse = [['R' for i in range(D)] for j in range(N)]
    for i in range(D):
        if i%7==0:
            times = [0 for p in range(N)]
        for j in range(3):
            posb = set(range(N))
            if j==0:
                if i!=0:
                    prv_morn = scd[i-1][0]
                    prv_even = scd[i-1][2]
                    for z in prv_morn:
                        posb.discard(z)
                    for z in prv_even:
                        posb.discard(z)
            elif j==1:
                cur_morn = scd[i][0]
                for z in cur_morn:
                    posb.discard(z)
            else:
                cur_morn = scd[i][0]
                cur_aft = scd[i][1]
                for z in cur_morn:
                    posb.discard(z)
                for z in cur_aft:
                    posb.discard(z)
            num = m
            if j==1:
                num = a
            if j==2:
                num = e
            a1 = []
            a2 = []
            for z in posb:
                if times[z]<6 and z<S:
                    a1.append(z)
                elif times[z]<6 and z>=S:
                    a2.append(z)
            arr = []
            if j==1:
                a1.sort(key=lambda x: times[x])
                a2.sort(key=lambda x: times[x])
                arr = a2+a1
            else:
                a1.sort(key=lambda x: times[x])
                a2.sort(key=lambda x: times[x])
                arr = a1+a2
            if num>len(arr) or times[arr[num-1]]>=6:
                return "NO-SOLUTION"
            for k in range(num):
                scd[i][j].append(arr[k])
                times[arr[k]] += 1
                if j==0:
                    all_nurse[arr[k]][i] = 'M'
                elif j==1:
                    all_nurse[arr[k]][i] = 'A'
                else:
                    all_nurse[arr[k]][i] = 'E'
    return all_nurse

def schedule_again(N, D, m, a, e, S, T):
    scd = [[[],[],[]] for i in range(D)]
    times = [0 for i in range(N)]
    all_nurse = [['R' for i in range(D)] for j in range(N)]
    for i in range(D):
        if i%7==0:
            times = [0 for p in range(N)]
        for j in range(3):
            posb = set(range(N))
            if j==0:
                if i!=0:
                    prv_morn = scd[i-1][0]
                    prv_even = scd[i-1][2]
                    for z in prv_morn:
                        posb.discard(z)
                    for z in prv_even:
                        posb.discard(z)
            elif j==1:
                cur_morn = scd[i][0]
                for z in cur_morn:
                    posb.discard(z)
            else:
                cur_morn = scd[i][0]
                cur_aft = scd[i][1]
                for z in cur_morn:
                    posb.discard(z)
                for z in cur_aft:
                    posb.discard(z)
            num = m
            if j==1:
                num = a
            if j==2:
                num = e
            a1 = []
            a2 = []
            for z in posb:
                if times[z]<6 and z<S:
                    a1.append(z)
                elif times[z]<6 and z>=S:
                    a2.append(z)
            arr = []
            if j==1:
                arr = a2+a1
                arr.sort(key=lambda x: times[x])
            else:
                a1.sort(key=lambda x: times[x])
                a2.sort(key=lambda x: times[x])
                arr = a1+a2
            if num>len(arr) or times[arr[num-1]]>=6:
                return "NO-SOLUTION"
            for k in range(num):
                scd[i][j].append(arr[k])
                times[arr[k]] += 1
                if j==0:
                    all_nurse[arr[k]][i] = 'M'
                elif j==1:
                    all_nurse[arr[k]][i] = 'A'
                else:
                    all_nurse[arr[k]][i] = 'E'
    return all_nurse

lst = sys.argv
csv_file = lst[1]
ans = []
df = pd.read_csv(csv_file)
lnt = len(df)
for i in range(lnt):
    dct = {}
    cur = df.loc[i]
    N = cur[0]
    D = cur[1]
    m = cur[2]
    a = cur[3]
    e = cur[4]
    all_nur = []
    if len(cur)==5:
        all_nur = sched(N,D,m,a,e)
    else:
        S = cur[5]
        T = cur[6]
        all_nur = schedule(N,D,m,a,e,S,T)
        if all_nur=="NO-SOLUTION":
            all_nur = schedule_again(N,D,m,a,e,S,T)

    if all_nur!="NO-SOLUTION":
        for p in range(N):
            for q in range(D):
                vl = all_nur[p][q]
                ky = f"N{p}_{q}"
                dct[ky] = vl
    ans.append(dct)

with open("solution.json" , 'w') as file:
    for d in ans:
        json.dump(d,file)
        file.write("\n")