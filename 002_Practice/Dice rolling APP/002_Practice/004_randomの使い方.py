import random

#random.random()：生成一个0.0到1.0之间的随机浮点数（不包括1.0）
print(random.random())

#random.uniform(a, b)：生成一个a到b之间的随机浮点数（包括a和b）
print(random.uniform(1.0, 10.0))

#random.randint(a, b)：生成一个a到b之间的随机整数（包括a和b）
print(random.randint(1, 10))

#random.randrange(start, stop[, step])：从指定范围内，按指定步长，生成一个随机整数（不包括stop）
print(random.randrange(1, 10, 2))

#random.choice(seq)：从非空序列seq中随机选择一个元素
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))

#random.choices(population, weights=None, *, cum_weights=None, k=1)：从population中选择k个元素，可以指定权重
population = ['apple', 'banana', 'cherry']
print(random.choices(population, weights=[1, 2, 3], k=2))

#random.shuffle(x[, random])：将序列x随机打乱
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)

#random.sample(population, k)：从population中随机选择k个不重复的元素
population = ['apple', 'banana', 'cherry', 'date']
print(random.sample(population, 2))

#random.seed(a=None)：初始化随机数生成器。可以指定一个种子值a，如果不指定，则使用系统时间
random.seed(10)
print(random.random())

#random.getrandbits(k)：生成一个具有k位随机数的整数
print(random.getrandbits(8))