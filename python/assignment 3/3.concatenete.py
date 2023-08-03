
# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def concatined(*dicts):
#     concat_dict={}
#     for dictionary in dicts:
#         concat_dict.update(dictionary)
#     return concat_dict
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# res=concatined(dic1,dic2,dic3)
# print(res) 

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dict4={**dic1,**dic2,**dic3}
print(dict4)