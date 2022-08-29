# Python program to combine two dictionary
# adding values for common keys
# initializing two dictionaries
dt1 = {'a': 100, 'b': 200, 'c': 300}
dt2 = {'a': 300, 'b': 200, 'c': 400}


# adding the values with common key
for i in dt2:
	if i in dt1:
		dt2[i] = dt1[i] + dt2[i]
	else:
		pass
		
print(dt2)

l1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]

d=dict(l1)
print(d)
