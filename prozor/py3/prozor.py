def main():
    #while True:
    line = input()
    line_list = line.split(' ')
    R = int(line_list[0])
    K = int(line_list[1])
    S = int(line_list[2])

    x = 0
    y = 0
    m = 0

    w = []
    wp = []

    for i in range(R):
        a = input()
        wp.append([1 if i=='*' else 0 for i in a])
        w.append(a)

#    print(w)

    lr = R-S+2
    lc = K-S+2

#    print(lr, lc)

    for i in range(1,lr):
        for j in range(1,lc):
            f = ""
            tm = 0
#            print("i,j",i,j)
            for k in range(0,S-2):
                for l in range(0,S-2):
#                    print("k,l",k,l)
                    c = w[i+k][j+l]
                    if c == '*':
                        tm += 1
                    f += c
            if tm > m:
                m = tm
                x = i
                y = j
#            print(f,tm)
#        print("//    ")
#    print("max ",m,x,y)

    print(m)
    for i in range(R):

        if i == x-1 or i == x+S-2:
#            print(w[i][0:y-1]+"wwww"+w[i+S-1:])
            print(w[i][0:y-1]+"+"+("-"*(S-2))+"+"+w[i][y+S-1:])
        elif i > x-1 and i < x+S-2:
            print(w[i][0:y-1]+"|"+w[i][y:y+S-2]+"|"+w[i][y+S-1:])
        else:
            print(w[i])


if __name__ == "__main__":
    #try:
    main()
    #except:
    #    pass
