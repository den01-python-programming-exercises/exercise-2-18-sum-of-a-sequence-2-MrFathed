def main():
    #write your code below this line
    start = int(input("First number?"))
    finish = int(input("Last number?"))
    sum = 0

    for i in range(start, finish+1):
        sum += i

    print("The sum is " + str(sum))

if __name__ == '__main__':
    main()
