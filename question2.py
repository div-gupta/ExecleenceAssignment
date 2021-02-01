dict1 = {"1" : "name1" , "2":"name2" ,"3":"name3" }
dict2 = {"1" : 50 ,"2":60, "3":70}

itemMaxValue = max(dict2.items(), key=lambda x : x[1])
print('Key With Max value in Dict: ', itemMaxValue[0])
print('Max value in Dict: ', itemMaxValue[1])
