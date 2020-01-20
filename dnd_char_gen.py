import pygal
from die import Die
import matplotlib.pyplot as plt

#Create 4 d6
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()

#Make some rolls, store results in a list
results = []

def roll_attribute():
    rolls = []
    rolls.append(die_1.roll())
    rolls.append(die_2.roll())
    rolls.append(die_3.roll())
    rolls.append(die_4.roll())
    rolls.remove(min(rolls))

    result = sum(rolls)

    return result

for roll_num in range(10000):
   
    result = roll_attribute()
    results.append(result)

#Analyze the results
frequencies = []
max_result = 18

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling 4d6 and subtracting the lowest value 10000 times"
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('stat roll', frequencies)
hist.render_to_file('D&Drolls.svg')

#Compare rolling to the default stats given in the book
default_stats = 72
#[0 - neutral, 1 - very strong, 2 - strong, 3 - weak, 4 - very weak]
over_default = [0, 0, 0, 0, 0]
exactly_default = [0, 0, 0, 0, 0]
under_default = [0, 0, 0, 0, 0]

for roll_set in range(10000):
    strong_vs_weak = 0
    attributes = []
    vs_char = False
    s_char = False
    w_char = False
    vw_char = False

    for roll in range(6):
        attribute = roll_attribute()
        if attribute > 15:
            strong_vs_weak +=1
        elif attribute < 8:
            strong_vs_weak -=1

        attributes.append(attribute)
    total = sum(attributes)

    if strong_vs_weak > 1:
        vs_char = True
    elif strong_vs_weak == 1:
        s_char = True
    elif strong_vs_weak < -1:
        vw_char = True
    elif strong_vs_weak == -1:
        w_char = True

    if total > default_stats:
        if vs_char:
            over_default[1] += 1
        elif s_char:
            over_default[2] += 1
        elif w_char:
            over_default[3] += 1
        elif vw_char:
            over_default[4] += 1
        else:
            over_default[0] += 1
    elif total < default_stats:
        if vs_char:
            under_default[1] += 1
        elif s_char:
            under_default[2] += 1
        elif w_char:
            under_default[3] += 1
        elif vw_char:
            under_default[4] += 1
        else:
            under_default[0] += 1
    elif total == default_stats:
        if vs_char:
            exactly_default[1] += 1
        elif s_char:
            exactly_default[2] += 1
        elif w_char:
            exactly_default[3] += 1
        elif vw_char:
            exactly_default[4] += 1
        else:
            exactly_default[0] += 1

sum_over = sum(over_default)
sum_exact = sum(exactly_default)
sum_under = sum(under_default)
sum_all = (sum_over + sum_exact + sum_under)
pie_chart = pygal.Pie()
pie_chart.title = 'Quality of characters rolled using PHB Standard Method'
pie_chart.add('Over Default', [{'value': ((over_default[0])/sum_all)*100, 'label': 'Regular Characters'},
                               {'value': ((over_default[1])/sum_all)*100, 'label': 'Very Strong Characters'},
                               {'value': ((over_default[2])/sum_all)*100, 'label': 'Strong Characters'},
                               {'value': ((over_default[3])/sum_all)*100, 'label': 'Weak Characters'},
                               {'value': ((over_default[4])/sum_all)*100, 'label': 'Very Weak Characters'}])

pie_chart.add('Exactly Default', [{'value': ((exactly_default[0])/sum_all)*100, 'label': 'Regular Characters'},
                               {'value': ((exactly_default[1])/sum_all)*100, 'label': 'Very Strong Characters'},
                               {'value': ((exactly_default[2])/sum_all)*100, 'label': 'Strong Characters'},
                               {'value': ((exactly_default[3])/sum_all)*100, 'label': 'Weak Characters'},
                               {'value': ((exactly_default[4])/sum_all)*100, 'label': 'Very Weak Characters'}])

pie_chart.add('Under Default', [{'value': ((under_default[0])/sum_all)*100, 'label': 'Regular Characters'},
                               {'value': ((under_default[1])/sum_all)*100, 'label': 'Very Strong Characters'},
                               {'value': ((under_default[2])/sum_all)*100, 'label': 'Strong Characters'},
                               {'value': ((under_default[3])/sum_all)*100, 'label': 'Weak Characters'},
                               {'value': ((under_default[4])/sum_all)*100, 'label': 'Very Weak Characters'}])
pie_chart.render_to_file('D&DCharacters.svg')








