import time

def seq(start):
    n = start
    yield n
    while n!=1:    
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        yield n


if __name__ == "__main__":

    t0 = time.clock()

    maxlen = 0
    max_start = 0

    lengthdic = {}
    
    for i in range(1,1000000):
        if i%10000==0:
            print i,"/ 1000000"

        len_seq = 0

        for k in seq(i):
            len_seq+=1
            #print k
            if str(k) in lengthdic:
                len_seq += lengthdic[str(k)]
                break
            
        lengthdic[str(i)]=len_seq
        
        if len_seq>maxlen:
            maxlen = len_seq
            max_start = i
    
    print(max_start)
    print time.clock()-t0
