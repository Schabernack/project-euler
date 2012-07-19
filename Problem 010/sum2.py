import time

def foo():
    
    t0 = time.clock()

    last_nbr = 2000000
    is_prime = [True] * (last_nbr+1)

    is_prime[0]=False
    is_prime[1]=False

    for i in range(2,len(is_prime)):
    	if is_prime[i]==True:
    		for k in range(i,(last_nbr/i)+1):
    			is_prime[i*k]=False

    #print(filter(lambda x: x[1]==True, enumerate(is_prime)))
    print(sum([i[0] for i in enumerate(is_prime) if i[1]==True]))
    print time.clock()-t0
	
# Run program in function to improve performance. 
# http://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function
if __name__ == "__main__":
	foo()

    
