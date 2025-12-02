def countNow(PLACES):
    for city in PLACES.values():
        if len(city)>5:
            print(city.upper())
PLACES={1:"Delhi",2:"London",3:"Paris",4:"New York",5:"Doha"}
countNow(PLACES)