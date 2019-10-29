#look at a temperature and figure out what state water is in - solid, liquid or gas
#
##set the temperature first - and turn our text into a number => that's int() does
temp = int(input("enter temperature"))

if temp < 4:
	print("water is frozen - a solid")