def generate_cases():
    expr_arr = []
    expr_dict = {}

    for i in range(0,64):
        masks = []
        masks.append(i & 0x0003)
        masks.append((i & 0x000c) >> 2)
        masks.append((i & 0x0030) >> 4)

        strx = "4 "     

        for m in masks:
            if m == 0:
                strx += "-"
            elif m == 1:
                strx += "+"
            elif m == 2:
                strx += "*"
            else:
                strx += "/"
            strx += " 4 "

        expr_arr.append(strx)
        res = int(eval('//'.join(strx.split('/'))))
        expr_dict[res] = strx + "= " + str(res)
    
    return expr_dict
            
def main():

    dict_4 = {0: "4 / 4 / 4 / 4 = 0",
                1: "4 * 4 / 4 / 4 = 1",
                2: "4 / 4 + 4 / 4 = 2",
                4: "4 - 4 / 4 / 4 = 4",
                68: "4 + 4 * 4 * 4 = 68",
                7: "4 + 4 - 4 / 4 = 7",
                8: "4 + 4 * 4 / 4 = 8",
                9: "4 + 4 + 4 / 4 = 9",
                256: "4 * 4 * 4 * 4 = 256",
                15: "4 * 4 - 4 / 4 = 15",
                16: "4 * 4 * 4 / 4 = 16",
                17: "4 * 4 + 4 / 4 = 17",
                24: "4 + 4 + 4 * 4 = 24",
                -60: "4 - 4 * 4 * 4 = -60",
                32: "4 * 4 + 4 * 4 = 32",
                -16: "4 - 4 - 4 * 4 = -16",
                -15: "4 / 4 - 4 * 4 = -15",
                -1: "4 - 4 - 4 / 4 = -1",
                -8: "4 + 4 - 4 * 4 = -8",
                -7: "4 / 4 - 4 - 4 = -7",
                60: "4 * 4 * 4 - 4 = 60",
                -4: "4 / 4 / 4 - 4 = -4",
                4: "4 + 4 / 4 / 4 = 4",
    }
    tcn = int(input())

    for i in range(0,tcn):
        idx = int(input())
        out_str = ""
        if idx in dict_4.keys():
            out_str = dict_4[idx]
        else:
            out_str = "no solution"

        print(out_str)
if __name__ == "__main__":
    try:
        main()
    except:
        pass
