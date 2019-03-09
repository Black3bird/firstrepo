def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(1, 6)
    sumProblem(670, 80)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main() 

person = input("Enter the name of person: ")
greetings = "Hello {}".format(person)
print(greetings)
