def mmu(mr):
    mm = 0 
    cm = 0
    for i in mr:
        cm+=i
        mm = max(mm, cm)
        
        return mm
if __name__ == "__main__":
    mr = []
    
    while True:
        r = int(input())
        if r == 0:
            break
        mr.append(r)
    f = mmu(mr)
    print(f)