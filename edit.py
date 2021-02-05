import discord

color = 0x0000FF
features = {
	'temp' : 'Temperature',
	'feels_like' : 'Feels Like',
	'temp_min' : 'Minimum Temperature',
	'temp_max' : 'Maximum Temperature',
}

def parse_data(data):
	data = data['main']
	del data['humidity']
	del data['pressure']
	return data

def weather_message(data, location):
	location = location.title()
	message = discord.Embed(
		title = f'{location} Weather',
		description = f'Weather for {location}.',
		color = color
	)
	for key in data:
		message.add_field(
			name = features[key],
			value = str(data[key]),
			inline = False
		)
	return message

def error_message(location):
	location = location.title()
	return discord.Embed(
		title = 'Error',
		description = f'Not able to retrieve weather data for {location}.',
		color = color
	)