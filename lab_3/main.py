from queue_new import Queue as Q1
from queue_new2 import Queue as Q2
from weather_client import WeatherClient
# try queue_new class

q1 = Q1()
q1.insert(1)
q1.insert(2)
q1.insert(3)

print("First in the queue: "+ str(q1.pop()))
print("is Empty: "+str(q1.is_empty()))

# try queue_new2 class

q2 = Q2("q2", 10)
q2.insert(1)
q2.insert(2)
q2.insert(3)
q2.insert(4)

print("First in the queue: "+str(q2.pop()))
print("is Empty: "+str(q2.is_empty()))
print("Queue size: "+str(q2.size))
print("Queue name: "+q2.name)
q2.save()

print("Loading queue from file")
q3 = Q2.load("q2")

print("First in the queue: "+str(q3.pop()))


# try weather_client class

wc = WeatherClient()
print("Current temperature in Mansoura,Egypt: "+str(wc.get_current_temperature("Mansoura,Egypt")))
print("Temperature in Mansoura,Egypt in 3 days: "+str(wc.get_temperature_after("Mansoura,Egypt", 3)))
print("Temperature in Mansoura,Egypt in 3 days at 12: "+str(wc.get_temperature_after("Mansoura,Egypt", 3, 12)))
print("Lat and Long of Mansoura,Egypt: "+str(wc.get_lat_and_long("Mansoura,Egypt")))


