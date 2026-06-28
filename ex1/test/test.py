import pandas
import numpy

data = {
    "Name": ["Spangebob", "Patric", "Squidward"],
    "Age": [30, 35, 50]
    }

df = pandas.DataFrame(data)
print(df)


my_list = [1, 2, 3, 4]
my_list = my_list * 2
print(my_list)


array = numpy.array([1, 2, 3, 4])

print(array)
print(type(array))

array = array * 2
print(array)
