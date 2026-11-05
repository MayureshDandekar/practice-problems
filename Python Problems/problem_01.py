s = ["  hello ", "world  "]

def strip_string(n):
    a = []
    for i in n:
        string = i.strip()
        a.append(string)
    print(a)

strip_string(s) 
# cleaned = [item.strip() for item in s] : ##shorter way to do the same task##