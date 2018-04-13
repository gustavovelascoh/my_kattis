def main():

    translator= {"a":"@",
    "n":"[]\\[]",
    "b":"8",
    "o":"0",
    "c":"(",
    "p":"|D",
    "d":"|)",
    "q":"(,)",
    "e":"3",
    "r":"|Z",
    "f":"#",
    "s":"$",
    "g":"6",
    "t":"']['",
    "h":"[-]",
    "u":"|_|",
    "i":"|",
    "v":"\\/",
    "j":"_|",
    "w":"\\/\\/",
    "k":"|<",
    "x":"}{",
    "l":"1",
    "y":"`/",
    "m":"[]\\/[]",
    "z":"2"}

    while True:
        line = input()
        
        out_str = ""
        for c in line.lower():
            if c in translator.keys():
                out_str += translator[c]
            else:
                out_str += c
        print(out_str   )
if __name__ == "__main__":
    try:
        main()
    except:
        pass
