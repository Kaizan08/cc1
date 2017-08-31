import requests

def urlchecker(userArr):
    badarray = []
    for arr in userArr:
        if ((arr.startswith("http://")) or (arr.startswith("https://"))):
            newarr = arr
        else:
            newarr = "http://" + arr

        r = requests.get(newarr)
        if r.status_code != 200:
            obj = {"badurl": newarr, "status_code": r.status_code}
            badarray.append(obj)
    return badarray
