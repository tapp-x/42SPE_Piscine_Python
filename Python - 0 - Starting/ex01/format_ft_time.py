import datetime


x = datetime.datetime.now()
a = datetime.datetime(1970, 1, 1)
diff = (x - a)
sec = diff.total_seconds()


print("Seconds since January 1, 1970:", f"{sec:,.0f}", "or", format(sec, ".2e"), "in scientific notation")
print(x.strftime("%b"), x.strftime("%d"), x.year)
