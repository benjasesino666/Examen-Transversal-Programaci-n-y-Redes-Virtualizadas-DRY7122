import urllib.parse
import requests
#aca se llama a la key y la paguina web de mapquest
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "yB8o1tLoQYd60zQUFlygdr4ncyvr3VAj"
#codigo para que funciones 
while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()
    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones desde " + orig + " hasta " + dest)

        duration_seconds = json_data["route"]["time"]
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        seconds = duration_seconds % 60
        print("Duración del viaje:   {} horas, {} minutos, {} segundos".format(hours, minutes, seconds))

        kilometers = json_data["route"]["distance"] * 1.61
        print("Kilómetros:      {:.1f} km".format(kilometers))

        fuel_used_liters = json_data["route"]["fuelUsed"] * 3.78
        print("Combustible utilizado (Ltr): {:.1f} lts".format(fuel_used_liters))

        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + "{:.1f}".format(each["distance"] * 1.61) + " km)")
        print("=============================================\n")
    elif json_status == 402:
        print("****************")
        print("Código de Estado: " + str(json_status) + "; Entradas de usuario inválidas para una o ambas ubicaciones.")
        print("****************\n")
    elif json_status == 611:
        print("****************")
        print("Código de Estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("****************\n")
    else:
        print("************************")
        print("Para el código de estado: " + str(json_status) + "; Consulta:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************\n")
