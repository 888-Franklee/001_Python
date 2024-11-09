#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

passion = "what?"
word_dict = {
    "life": "生活",
    "need": "需要",
    "passion": "激情！！"
}

def what_the_life_need(life_dict):
    global passion
    passion = "激情！！"
    life_dict["passion"] = passion

# 関数の呼び出し
what_the_life_need(word_dict)

# 辞書参照部分を ' ' で囲む
print(
    f"passion: {passion}, "
    f"life need {word_dict['passion']}"
)

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

x = 10

def create_local():
    x = 20
    print(x)

create_local()  # 输出: 20
print(x)  # 输出: 10

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#

counter = 0

def increment():
    global counter
    counter += 1

def decrement():
    global counter
    counter -= 1

def print_counter():
    print(counter)

increment()
print_counter()  # 输出: 1
decrement()
print_counter()  # 输出: 0