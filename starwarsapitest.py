import swapi
import json
import sys
import requests
import json
import urllib.parse
import urllib.request, json

#swapi url override
swapi.settings.BASE_URL = "https://swapi.dev/api"


# function that printout all resources whos search fields match the term
def search_func():
    # in this function, working with json format that transform to python objects, reduces the API calls
    checkresourceinput = False
    checkterminput= False
    resourcelist = "https://swapi.dev/api/"
    resources = []
    with urllib.request.urlopen(resourcelist) as url: # getting all the resources
        datares = json.loads(url.read().decode())
    for key in (datares.keys()):
        resources.append(key)
    print(resources)  # the user will choose and write one of the resources from the list
    while (checkresourceinput==False): # checking the resource input from the user
        resourceInput = input('Enter resource name from the list above:')
        if (resourceInput in resources):
            checkresourceinput=True
    endpoint = "https://swapi.dev/api/{resource}/?".format(resource=resourceInput)

    with urllib.request.urlopen(endpoint) as url:
        data = json.loads(url.read().decode())
    termlist=[]
    for line in (data['results']): # getting all the keys from the resource that the user choose
        for key in line.keys():
            termlist.append(key)
        break
    print(termlist) #the user will choose which field will be in the term

    while (checkterminput == False):  # checking the field input from the user
        termInput = input('Please enter your field to the term from the list above:')
        if (termInput in termlist):
            checkterminput = True
    conditionInput = input('Please enter your condition:') # the user will write what is the condition for the term
    print('search {} {}={}'.format(resourceInput ,termInput ,conditionInput))
    results = data["results"]
    print('Results For The Search:  ')
    for entry in results: # will print all the resources that the user choose that match the term
        if entry[termInput] == conditionInput:
            print(entry)

    jsonoutput = json.dumps(results) # transform python object into json, for later use, will reduce the API Calls

# this function get full string and return all planets sorted by a given field
def getPlanets_func():
    # in this function, working with json format files that transform to python objects , reduces the API Calls
    checkorderfieldinput = False
    order_fields_options=[]

    endpoint = "https://swapi.dev/api/planets"
    with urllib.request.urlopen(endpoint) as url: # getting all the resources of planets in json format
        source = url.read()
    data=json.loads(source)
    print('List of order field: ')
    for line in (data['results']):# getting all the fields from the resource Planets
        for key in (line.keys()):
            order_fields_options.append(key)
        break
    print(order_fields_options) # the user will choose and write one of the order field from that list
    while (checkorderfieldinput==False):
        input_From = input('Enter Your Full String:(get-planets <order field> <asc/desc>)') # syntax = get-planets <order field> <asc/desc>
        inputlist = input_From.split(' ')# split the string that we recive
        order_field = inputlist[1] # get the order field from the string
        if order_field in order_fields_options:
            checkorderfieldinput=True
        else:
            print('Order field not in the list')

    sortfield = inputlist[2] # get the sort order from the string
    if (sortfield=='asc'):
        sorted_list = sorted(data['results'], key=lambda i: (i[order_field]))
    elif (sortfield=='desc'):
        sorted_list = sorted(data['results'], key=lambda i: (i[order_field]) , reverse=True)
    else:
        sorted_list = []
        print('Not Valid Sort value')
    for entry in sorted_list: # printing the planets sorted by a given field
        print(entry)
    output_json = json.dumps(sorted_list) # Transform python object back into json, for later use, and that will reduce the API calls


if __name__ == '__main__':
    #asking the user to choose which task he wants:  1) search <resource><term>
     #                                               2)get_planets <order field> <asc/desc>
    #                                                3) Exit

        taskNum = int(input('Please enter your task number:\n1)Search \n2)Get Planets\n3)Exit\n'))
        while (taskNum !=3):
            if (taskNum==1):
                search_func()
            if (taskNum==2):
                getPlanets_func()
            taskNum = int(input('Please enter your task number:\n1)Search \n2)Get Planets\n3)Exit\n'))






