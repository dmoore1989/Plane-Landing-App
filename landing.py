import sys
import re
import requests

def check_landing(string):
    if string == None: 
        request = requests.get("https://datis.clowd.io/api/klga")
        request_atis = request.json()[0]['datis']
    else:
        request_atis = string
    departing_rwy = re.split(r"\s|\.",  request_atis[request_atis.find("DEPART"):])[2]
    landing_sentence = request_atis.find("LND") if request_atis.find("LND") > -1 else request_atis.find("LAND") 
    landing_rwy = re.split(r"\s|\.",  request_atis[landing_sentence:]) 
    landing_rwy = landing_rwy[2]
    print("Departing Runway: " + departing_rwy) 
    print("Landing Runway: " +  landing_rwy)
    if landing_rwy == "4":
        print("Planes will be landing over the landing lights park")
    if departing_rwy == "22":
        print("Planes will be taking off over the landing lights park")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        string = sys.argv[1] 
    else:
        string = None
    check_landing(string)
