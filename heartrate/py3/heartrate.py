def main():
    tc = input()
    for i in range(0, int(tc)):
        data = input()
        data_arr = data.split(' ')
        b = int(data_arr[0])
        p = float(data_arr[1])
        
        k = 60/p
        min_abpm = (b-1)*k
        abpm = b*k
        max_abpm = (b+1)*k
        
        print("%.4f %.4f %.4f" % (min_abpm, abpm, max_abpm))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
        print(e)
