from machine import Timer

count = 0


def counter(value):
    global count
    count += 1
    print(count)


timer = Timer(period=1000, mode=Timer.PERIODIC, callback=counter)

While True:
    print("Timerzustand : ",count)