# your code goes here!
import time

def countdown(num):
    pass
    while (num > 0):
        print(f"{num} SECOND(S)!")
        num-=1
    
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    pass
    while (num > 0):
        print(f"{num} SECOND(S)!")
        time.sleep(1)
        num-=1
    
    print("HAPPY NEW YEAR!")