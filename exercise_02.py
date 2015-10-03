#age  = raw_input("what's your age? ")

prompt = ('> ')

print "What's your age? Type in [years],[months] "
years,months = map(int, raw_input(prompt).split(','))

print "So you're %d years and %d months old." %(years, months)

ageInDays = years * 30 * 12 + months * 30

print "Which is", ageInDays ,"days old." 

