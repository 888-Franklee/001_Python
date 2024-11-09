import random

#生成一个随机浮点数：
print(random.random())#这段代码将输出一个介于0.0和1.0之间的随机浮点数，例如：0.37444887175646646

#生成随机概率：
probability = random.random()
if probability < 0.5:
    print("成功")
else:
    print("失败")
    
#生成指定范围的随机浮点数：
random_value = 5.0 + (random.random() * 5.0)
print(random_value)#虽然 random.random() 生成的数在0.0到1.0之间，但可以通过数学运算将其转换为任意范围的随机浮点数

#生成随机颜色值：
r = random.random()
g = random.random()
b = random.random()
print(f"随机颜色: RGB({r}, {g}, {b})")

#模拟事件发生概率：
event_probability = 0.3  # 事件发生的概率为30%
if random.random() < event_probability:
    print("事件发生")
else:
    print("事件未发生")

#注意事项:
random.seed(10)
print(random.random())#random.random() 生成的数是伪随机数，由于算法的原因，虽然看起来是随机的，但实际上是由一定算法生成的，适用于大多数应用场景，但不适用于需要真正随机数的高安全性场合。如果需要生成重复的伪随机数序列，可以使用 random.seed() 设置种子。

#实践示例：
event_probability = 0.2
experiment_results = {'发生': 0, '未发生': 0}

for _ in range(1000):
    if random.random() < event_probability:
        experiment_results['发生'] += 1
    else:
        experiment_results['未发生'] += 1

print(f"实验结果: 事件发生 {experiment_results['发生']} 次, 事件未发生 {experiment_results['未发生']} 次")
#假设我们需要模拟一个实验，其中一个事件发生的概率是20%。我们可以使用 random.random() 来模拟这个实验