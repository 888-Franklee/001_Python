#创建空列表:
empty_list = list()
empty_list = []

# 从字符串创建列表
string_list = list("hello")
print(string_list)  # 输出: ['h', 'e', 'l', 'l', 'o']

# 从元组创建列表
tuple_list = list((1, 2, 3))
print(tuple_list)  # 输出: [1, 2, 3]

# 从集合创建列表
set_list = list({4, 5, 6})
print(set_list)  # 输出: [4, 5, 6] (注意: 集合是无序的，输出顺序可能不同)

#复制列表:
original_list = [1, 2, 3]
copied_list = list(original_list)
print(copied_list)  # 输出: [1, 2, 3]

#使用列表推导式创建列表:
squared_list = [x**2 for x in range(10)]
print(squared_list)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 从字典的键创建列表
dict_keys_list = list({"a": 1, "b": 2, "c": 3}.keys())
print(dict_keys_list)  # 输出: ['a', 'b', 'c']

# 从字典的值创建列表
dict_values_list = list({"a": 1, "b": 2, "c": 3}.values())
print(dict_values_list)  # 输出: [1, 2, 3]

# 从字典的键值对创建列表
dict_items_list = list({"a": 1, "b": 2, "c": 3}.items())
print(dict_items_list)  # 输出: [('a', 1), ('b', 2), ('c', 3)]