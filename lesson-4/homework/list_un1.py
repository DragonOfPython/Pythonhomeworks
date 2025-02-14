from collections import Counter

def collect_unc_el(list1, list2):   

    c1 = Counter(list1)
    c2 = Counter(list2)

    uncommon_elements = []

    for i in c1:
        if i not in c2: 
         uncommon_elements.extend([i] * c1[i])

    for i in c2:
     if i not in c1:
        uncommon_elements.extend([i] * c2[i])

    return uncommon_elements

list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon1 = collect_unc_el(list1, list2)
print(uncommon1)

list3 = [1, 2, 3]
list4 = [4, 5, 6]
uncommon2 = collect_unc_el(list3, list4)
print(uncommon2)

list5 = [1, 1, 2, 3, 4, 2]
list6 = [1, 3, 4, 5]
uncommon3 = collect_unc_el(list5, list6)
print(uncommon3)


