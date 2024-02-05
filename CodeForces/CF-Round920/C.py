import sys

sys.stdin = open('CodeForces/input.txt',  'r')

def get_input():
    t = int(input())
    res =  []
    for _ in range(t):
        n, f, a, b = list(map(int, input().split()))
        messages_ts = list(map(int, input().split()))
        res.append([n, f, a, b, messages_ts])

    return res

def f():
    tc = get_input()
    for i in tc:
        num_msgs, phone_charge, chrg_used_per_time, chrg_used_on_off, messages_ts = i
        final_ts_phone_on = messages_ts[-1]*chrg_used_per_time
        if final_ts_phone_on < phone_charge:
            print('YES')
            continue
        final_ts_phone_on = 0
        t = messages_ts[0]*chrg_used_per_time
        if  t > chrg_used_on_off:
            final_ts_phone_on += chrg_used_on_off
        else:
            final_ts_phone_on += t
        for i in range(num_msgs-1):
            t = (messages_ts[i+1] - messages_ts[i])*chrg_used_per_time
            if  t > chrg_used_on_off:
                final_ts_phone_on += chrg_used_on_off
            else:
                final_ts_phone_on += t
        #print(phone_charge, chrg_used_per_time, chrg_used_on_off, messages_ts, final_ts_phone_on)
        if final_ts_phone_on < phone_charge:
            print('YES')
            continue
        print('NO')
        
        

f()
    