from types import coroutine

day_activities_dict = {
    None: None,
	'Sun': 'Wake up and Study',
	'Mon': 'Go to Office',
	'Tue': 'Work from home and study',
	'Wed': 'Go to office and finish PR'
}

@coroutine
def greet():
	name = None
	while True:
		name = yield(day_activities_dict[name])
		greeting = f'Today is {name}! Welcome to a new day.'
		print(greeting)
  
async def weekday_name(g):
	await g

w_gen = weekday_name(greet())

# None is returned at this point, so we are not printing it
# print(f'Value returned :: {w_gen.send(None)}')
w_gen.send(None)

weekdays = ['Sun', 'Mon', 'Tue', 'Wed']

print(f'**********************************\n')
for day in weekdays:
	activity = w_gen.send(day)
	print(f'Activity :: {activity}')
	print()
print(f'**********************************\n')
