from die import Die
import pygal

die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequncies = []

for value in range(1,die.num_sides+1):
    frequncy = results.count(value)
    frequncies.append(frequncy)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6',frequncies)
hist.render_to_file("die_visual.svg")

# print(frequncies)