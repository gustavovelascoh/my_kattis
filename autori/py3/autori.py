def main():
    while True:
        line = input()
        words=line.split('-')
        autori = ""
        for w in words:
            autori += w[0]
        print(autori)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
