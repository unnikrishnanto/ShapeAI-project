import requests
from datetime import datetime

def getData(city) -> str:
    try:
        api_key = "eb5ef05a1f20ab85b9ff23ff53bd617f"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        r = requests.get(URL)
        return r.json()
    except:
        r = r.json()
        if r['mesage']=="city not found":
            print("Error")
        return None
    
def out(res, city) -> str:
    temp_city = ((res['main']['temp']) - 273.15)
    weather_desc = res['weather'][0]['description']
    hmdt = res['main']['humidity']
    wind_spd = res['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    
    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print (" speed    :",wind_spd ,'kmph')

    with open('file.txt', 'w')as f:
        
      f.write(f"""-------------------------------------------------------------
               Weather Stats for - {city.upper()}  || {date_time}
              -------------------------------------------------------------

               Current temperature is: {temp_city} deg C
               Current weather desc  :{weather_desc}
               Current Humidity      :{hmdt}% 
               speed    :{wind_spd} kmph
              """)
      f.close()     
    return True
    
if __name__=='__main__':
    city = input("Enter the city name: ")
    res = getData(city)
    breakpoint()
    if res == 'None':
        print("City not found! check your keywork")
    else:
        out(res, city)
    
