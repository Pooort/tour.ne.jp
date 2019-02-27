import datetime
from pytz import timezone

japan = timezone('Japan')
japan_now = datetime.datetime.now(japan)
#'20190227'
print('{}{:02d}{}'.format(japan_now.year, japan_now.month, japan_now.day))

print('!')