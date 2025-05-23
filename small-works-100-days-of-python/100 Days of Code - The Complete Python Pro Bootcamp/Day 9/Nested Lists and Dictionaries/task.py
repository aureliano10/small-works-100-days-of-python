'''travel_log = {
    "French" : ["Paris", "Lille", "Dijon"],
    "Alemania" : ["Stuttgart", "Berlin"],
}
#print(travel_log["French"][1])
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])'''
travel_log = {
  "Francia": {
    "ciudades_visitadas": ["París", "Lille", "Dijon"],
    "total_visitas": 12
   },
  "Alemania": {
    "ciudades_visitadas": ["Berlín", "Hamburgo", "Stuttgart"],
    "total_visitas": 5
   },
}
print(travel_log["Alemania"]["ciudades_visitadas"][2])