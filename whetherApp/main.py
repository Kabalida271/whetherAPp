import requests, json  
app = requests(__name__)
@app.route('/')
api_key = "Entering of the API"  
base_urlin = "http://api.openweathermap.org/data/2.5/weather?"  
city_namein = input("Entering up the city name : ")  
complete_urlin = base_urlin + "appidin=" + api_keyin + "&q=" + city_namein  
response = requests.get(complete_urlin)  
x = response.json()  
if x["cod"] != "404":  
	y = x["main"]  
	current_temperaturein = y["temp"]  
	current_humidityin = y["humidity"]  
	z = x["weather"]  
	weather_descriptionin = z[0]["description"]  
	print(" Temperature (in kelvin unit) = " + str(current_temperaturein) + "\n atmospheric pressure display(in hPa unit) = " + str(current_pressurein) + "\n humidity display(in percentage) = " + str(current_humidityin) + "\n description = " + str(weather_descriptionin))  
else:  
	print(" City Unknown ")  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
