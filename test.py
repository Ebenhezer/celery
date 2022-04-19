from time import sleep
from tasks import reverse, gen_prime

primes = gen_prime.delay(1000)
#print(primes)
rev = reverse.delay('Ebenhezer')

while (primes.ready() != True):
    print("Still waiting")
    sleep(3)
    print(primes.ready())
    # primes = gen_prime.delay(50000)
    
print(primes.get())
print("Done")