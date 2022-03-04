from time import sleep
def printsleep(str):
    for x in str:
        print(x,end="",flush=True)
        sleep(0.05)