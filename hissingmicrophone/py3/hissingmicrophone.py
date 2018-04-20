def main():
    while True:
        line = input()
        output = "no hiss"
        for i, v in enumerate(line):
            if line[i:i+2] == "ss":
                output = "hiss"
                break
        print(output)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
