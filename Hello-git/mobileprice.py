print ("Please enter the cost price of your mobile")
cp = input()
print("Now please enter the selling price of your mobile")
sp = input()
if (sp>cp):
    gain=float(sp)-float(cp)
    print("Nice! you've got profit of",float(sp)-float(cp), "bucks")
    print("Great! you'have got" ,float(gain)/float(cp)*100, "% profit of cost price")
elif (sp<cp):
    loss=float(cp)-float(sp)
    print("Opps! you've got loss of", float(cp)-float(sp),  "bucks")
    print("Oh! no, you've got", float(loss)/float(cp)*100, "% loss of cost price")
else:
    print("You have'nt loss or earn any buck")
    
