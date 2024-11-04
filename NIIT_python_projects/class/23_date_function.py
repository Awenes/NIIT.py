import datetime as dt
ts = dt.datetime.now()


def date():

    return str(ts.year) + '-' + str(ts.month) + '-' + str(ts.day) + ' ' + \
           str(ts.hour) + ':' + str(ts.minute) + ':' + str(ts.second)


print(date())
