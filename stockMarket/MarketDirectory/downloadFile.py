import requests


def downloadCSV(url):
    response = requests.get(url)
    data = response.content
    with open("/home/vegeta/NIFTYDATA/Sample.csv",'wb') as f:
        f.write(data)

    return "/home/vegeta/NIFTYDATA/Sample.csv"