string = "Hello Earth"
print(type(string), string)

f = 33
print(type(int(f)), int(f))

a = 51.3
print(type(float(a)), float(a))

b = bytes(8)
print(type(b), b)

months = ['January','February','March','April']
print(type(months), months)

four_tuple = ("one","two","three","four")
print(type(four_tuple), four_tuple)

pets = {'dogs',"cats","mouses","birds"}
print(type(pets), pets)

fz = frozenset(months)
print(type(fz), fz)

dict = {'marvel_hero':'Spider_man','dc_hero':'Batman','dark_horse_hero':'Hellboy'}
print(type(dict), dict)

q = "qwerty_forever"
bw = "black&white"
z = q + bw
print(z)

print(bw,f)

print("Password" + q + str(f))




shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

if(customer_basket_cost >= 100):
  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost = 86.8

print("Total basket cost including shipping is " + str(customer_basket_cost))



