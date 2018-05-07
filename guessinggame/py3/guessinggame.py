def main():
    while True:
    
        lon = [1,2,3,4,5,6,7,8,9,10]
        
        eog = False
        out_str= "Stan is dishonest"
        
        min_n = 0
        max_n = 11
        
        while not eog:
            guess = int(input())
            fb = input()
            
            if fb == "too high":
                max_n = guess
            elif fb == "too low":
                min_n = guess
            else:
#                print(guess, min_n, max_n)
                eog = True
                if guess > min_n and guess < max_n:                    
                    out_str = "Stan may be honest"
            
#            print(eog, lon, fb)
            if (min_n > max_n):

                out_str= "Stan is dishonest"
                    
                eog = True
        
        print(out_str)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
#        print(e)
        pass
