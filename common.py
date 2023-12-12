
list1=[2,4,5,6,7]
list2=[5,6,7,8,9]
if len(list1)==len(list2):
    print("a.The lists have the same lengths")
else:
    print("The lists have different lengths")
print(f"b.The sum(list1):{sum(list1)}&sum(list2):{sum(list2)}")
if sum(list1)==sum(list2):
    print("The lists sum to the same value.")
else:
    print("The lists do not sum to the same value.")
common_values=set(list1)&set(list2)
if common_values:
    print(f"c.common_values in both lists:{common_values}")
else:
    print("c.There are no common_values in both lists")
