import pandas as pd 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("StudentsPerformance.csv")

reading_score = df["reading score"]

mean = statistics.mean(reading_score)
median = statistics.median(reading_score)
mode = statistics.mode(reading_score)
standard_deviation = statistics.stdev(reading_score)

first_standard_deviation_start, first_standard_deviation_end = mean - standard_deviation, mean + standard_deviation
second_standard_deviation_start, second_standard_deviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_standard_deviation_start, third_standard_deviation_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

first_standard_deviation_list = [result for result in reading_score if result > first_standard_deviation_start and result < first_standard_deviation_end]
second_standard_deviation_list = [result for result in reading_score if result > second_standard_deviation_start and result < second_standard_deviation_end]
third_standard_deviation_list = [result for result in reading_score if result > third_standard_deviation_start and result < third_standard_deviation_end]

print("Mean, Median and Mode of the data is {}, {} and {} respectively".format(mean, median, mode))
print("Standard Deviation of the data is {}".format(standard_deviation))
print("{}% of the data lies within first Standard Deviation".format((len(first_standard_deviation_list)*100)/len(reading_score)))
print("{}% of the data lies within second Standard Deviation".format((len(second_standard_deviation_list)*100)/len(reading_score)))
print("{} % of the data lies within third Standard Deviation".format((len(third_standard_deviation_list)*100)/len(reading_score)))

fig = ff.create_distplot([reading_score], ["Reading Score"], show_hist = False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.05], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_start, first_standard_deviation_start], y = [0, 0.05], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.05], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_start, second_standard_deviation_start], y = [0, 0.05], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_end, second_standard_deviation_end], y = [0, 0.05], mode = "lines", name = "Standard Deviation 2"))

fig.show()