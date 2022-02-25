def convertToXml(newxml):
    from dicttoxml import dicttoxml
    xml = dicttoxml(newxml)
    xmlfile = open("file.xml", "w")
    xmlfile.write(xml.decode())
    xmlfile.close()


def convertToJson(newjson):
    import json
    jsonfile = open('file.json', 'w')
    json.dump(newjson, jsonfile, indent=2)

def convertToYaml(newyaml):
    import yaml
    yamlfile = open('file.yaml', 'w')
    yaml.dump(newyaml, yamlfile, indent=2)


def convertToCsv(newcsv):
    #csvjson = convertToJson(newcsv)
    import csv
    liste = list()
    csvfile = open('file.csv', 'w')
    for i in newcsv.keys():
        liste.append(i)
    writer = csv.DictWriter(csvfile, fieldnames=liste)
    writer.writeheader()
    for data in newcsv:
        writer.writerow(data)
