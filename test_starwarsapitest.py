import unittest
import json
import urllib.request
import starwarsapitest
class TestResourceTerm(unittest.TestCase):
    def test_resource(self): # testing the number of resources found (suppose to be 6)
        resources = []
        resourcelist = "https://swapi.dev/api/"
        with urllib.request.urlopen(resourcelist) as url:
            datares = json.loads(url.read().decode())
        for key in (datares.keys()):
            resources.append(key)
        self.assertEqual(len(resources) , 6)
    def test_fields(self): # testing the number of fields in Planets
        fields_options = []
        endpoint = "https://swapi.dev/api/planets"
        with urllib.request.urlopen(endpoint) as url:
            source = url.read()
        data = json.loads(source)
        for line in (data['results']):  # getting all the fields from the resource Planets
            for key in (line.keys()):
                fields_options.append(key)
            break
        self.assertEqual(len(fields_options), 14)
if __name__=='__main__':
        unittest.main()
