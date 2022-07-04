import math

def main():

    math.log(5,2)

    while True:
        line = input()
        days = math.ceil(math.log(int(line),2))+1
        print(days)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
