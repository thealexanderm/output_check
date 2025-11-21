def output_check(correct_output, my_output):
    if(correctOutput!=myOutput):
        return False



if __name__ == '__main__':
    with open("correct_output.txt", "r") as f:
        lines = f.readlines()
        last = lines[-1]
    with open("correct_output.txt", "r") as f1, open("my_output.txt", "r") as f2:
        for x, y in zip(f1, f2):
            if(output_check(x,y)==False):
                print("There's an error :(")
                print(f"Your output is: {y}")
                print(f"The correct output is: {x}")
                break
            elif(x==last):
                output_check(x,y)
                print("Yay! No errors!")
            else:
                output_check(x, y)
