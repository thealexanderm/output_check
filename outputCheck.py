def outputCheck(correctOutput, myOutput):
    if(correctOutput!=myOutput):
        return False



if __name__ == '__main__':
    with open("correctOutput.txt", "r") as f:
        lines = f.readlines()
        last = lines[-1]
    with open("correctOutput.txt", "r") as f1, open("myOutput.txt", "r") as f2:
        for x, y in zip(f1, f2):
            if(outputCheck(x,y)==False):
                print("There's an error :(")
                print(f"Your output is: {y}")
                print(f"The correct output is: {x}")
                break
            elif(x==last):
                outputCheck(x,y)
                print("Yay! No errors!")
            else:
                outputCheck(x, y)
