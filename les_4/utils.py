from task_4_5 import currency_rates_decimal
from sys import argv

act = currency_rates_decimal(argv[1])
print(act[0] + ', ' + act[1])