
def solution(elements):
    answer = 0
    fin = set()
    ex  = elements + elements
    for j in range(1,len(elements)+1):
        for i in range(len(elements)):
            fin.add(sum(ex[i:i+j]))
    return len(fin)