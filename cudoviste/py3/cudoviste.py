def main():
    while True:
        rc_str = input()
        rc_arr = [int(e) for e in rc_str.split(' ')]

        map = []
        for r in range(0,rc_arr[0]):
            map.append(input())

        out = [0,0,0,0,0]

        for r in range(0,rc_arr[0]-1):
            for c in range(0,rc_arr[1]-1):
                spot = map[r][c:c+2] + map[r+1][c:c+2]
                if "#" in spot:
                    pass
                elif "X" in spot:
                    out[spot.count('X')] += 1
                else:
                    out[0] += 1

        for e in out:
            print(e)

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        pass
    except Exception as e:
        #print(e)
        pass
