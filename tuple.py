tp=(1,2,3,4,5,6,7)
ls=[8,9,10]

print("1. type of tp is ",type(tp))

tp = list(tp)
print("2. type(tp) ",type(tp))
tp.extend(ls)
print(tp)

tp=tuple(tp)
print("3. type(tp) ",type(tp))
print("Element in tp : ",tp)