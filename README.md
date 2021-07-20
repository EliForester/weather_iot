# Weather IOT Project 

Small IOT project to track the temperature in my yard and in my house

* IOT device running on Wemos D1 Mini with DHT11 temperature sensor (Arduino code)
* Sends http put messages to the server with json formatted temperature, humidity, battery charge
* Server (a Raspberry Pi 3 sitting next to my cable box) running flask_restful
* Server returns temperature data in an html page

## Requirements for flask app

```
aniso8601==8.0.0
click==7.1.2
Flask==1.1.2
Flask-RESTful==0.3.8
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
peewee==3.13.3
pytz==2020.1
six==1.15.0
Werkzeug==1.0.1
```

## Authors

* **Eli Forester** - [EliForester](https://github.com/EliForester)

