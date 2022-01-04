from geopy.geocoders import Nominatim

nom = Nominatim(user_agent="http") # because of the bug we need to clarify user_agent
n = nom.geocode("23 Lesi Ukrainky St, Yaremche 78500")
print(n.longitude, n.latitude)