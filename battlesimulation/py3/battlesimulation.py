def check_seq(seq):

    return True if seq in ["RBL", "RLB", "LRB", "LBR", "BLR", "BRL"] else False

def main():
    resp_d = {"R": "S", "B":"K", "L":"H"}
    while True:
        response = ""
        line = input()
        skip_fg = 0

        for i, v in enumerate(line):
            if skip_fg:
                skip_fg -= 1
                continue
            if check_seq(line[i:i+3]):
                skip_fg = 2
                response += "C"
            else:
                response += resp_d[v]

        print(response)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
