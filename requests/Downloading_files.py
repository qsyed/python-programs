from urllib import request


web_add = 'https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD'


def download_data(url):
    response = request.urlopen(web_add)
    csv = response.read()
    csv = str(csv)
    lines = csv.split("\\n")
    destination = r"random.csv"
    fx = open(destination, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close


download_data(web_add)






