#making a simple method
def printTwoSentences():
    print("A much longer sentence than your method call.")
    print("Another sentence.")


printTwoSentences()#look how much shorter that was!

#taking parameters
def print_addition(num1, num2):
    print(str(num1)+" + "+str(num2)+" = "+str(num1+num2))

print_addition(1,4) #fancy!

#returning something!
def add_a_space(n1, n2):
    return str(n1) + " " + str(n2)

print("If you have a method return "+add_a_space("its","result")+" instead of printing it,")
print("It is much easier to use its output in an "+add_a_space("almost","unlimited")+" number of ways!")
print ("As a bonus, you "+add_a_space("can", add_a_space("even", "nest"))+" methods when calling them!")



