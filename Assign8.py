#1 
a={1:"A",2:"B",3:"C",4:"D"}
print(a)

b=dict(sorted(a.items(),key=lambda item:item[1]))
print(b)

c=dict(sorted(a.items(),key=lambda item:item[1] ,reverse=True))
print(c)

#2
a={1:"A",2:"B",3:"C",4:"D"}
print( 1 in a)

#3
d={5:"E",6:"F",7:"G"}
a.update(d)
print(a)

#4
z=(1,2,3,4,5)
x=list(z)
print(type(x))
x.insert(5,6)
print(x)
z=tuple(x)
print(z)

#5
q=(1,4.4,"abc",True)
print(q)

#6
w=[1,2,3,4,5]
e=sum(w)
print(e)

#7
w=[1,2,3,4,5]
print(max(w))

#8
w=[1,2,3,4,5]
w.extend(["z","y"])
print(w)

#9
w=[1,2,3,4,5]
w.reverse()
print(w)

#10
w=[1,2,3,4,5]
print(w)
print(w[0])
print(w[1])
print(w[3])
