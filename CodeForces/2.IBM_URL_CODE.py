valid_auth__tokens = ["ah37]2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
requests = [
["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"], 
["GET", "https://example.com/?token=safh34ywb0p5&name=sam"], 
["POST", "https://example.com/?token=safh34ywb0p5&id=12&name=alex"], 
["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]]

def f():
    def is_valid_csrf(s):
        if len(s) < 8:
            return False
        for i in s:
            if i.isdigit():
                continue
            if i.isupper():
                return False
        return True
    res = []
    for reqType, url in requests:
        list_url = url.split('&')
        token = list_url[0][list_url[0].index('=')+1:]
        if token not in valid_auth__tokens:
            res.append('INVALID')
            continue
        list_url.pop(0)
        #print(url)
        #print(list_url)
        if reqType == 'POST':
            flag = True
            for i in range(len(list_url)):
                if 'csrf' in list_url[i]:
                    flag = False
                    csrf_token = list_url[i][list_url[i].index('=')+1:]
                    list_url.pop(i)
                    if not is_valid_csrf(csrf_token):
                        flag = True
                    break
            if flag:
                res.append('INVALID')
                continue
        #print(list_url)
        ans = 'VALID'
        for i in list_url:
            idx_eq = i.index('=')
            ans += ',' + i[:idx_eq] + ',' + i[idx_eq+1:]
        res.append(ans)
    print(res)

        


f()

