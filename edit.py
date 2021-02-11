import discord

degree_sign_celsius = u"\N{DEGREE SIGN}" + 'C'
degree_sign_fah = u"\N{DEGREE SIGN}" + 'F'

color = 0xFFFFFF
features = {
	'temp' : 'Temperature',
	'feels_like' : 'Feels Like',
	'temp_min' : 'Minimum Temperature',
	'temp_max' : 'Maximum Temperature',
}

def parse_data(data):
	data = data['main']
	temp_data = str(data['temp'])
	if(temp_data[0] == '-' and temp_data[1] == '0'):
		temp_data = temp_data.replace('-','')
		data['temp'] = float(temp_data)
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
		# print(data[key])
		data[key] = round(data[key])
		fah_value = round((data[key] * 9/5) + 32)
		value_weather = " ".join([str(data[key]) + degree_sign_celsius, str(fah_value) + degree_sign_fah])
		message.add_field(
			name = features[key],
			# value = str(data[key]) + degree_sign_celsius + '        ' + str(fah_value) + degree_sign_fah,
			value = value_weather,
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

def help_message():
	message = discord.Embed(
		title = 'WeatherBot',
		description = 'Type ;w {location} to find weather for desired location (Location must be city of a country/province/state).',
		color = color
	)
	return message