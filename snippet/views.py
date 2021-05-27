from .serializers import CountryListDetail, ErrorSerializer, Country
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
import requests
from bs4 import BeautifulSoup

# URL for scrapping data
# get URL html
page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.text, 'html.parser')
test = soup.find_all('a',class_="mt_a")
countries = [i.text for i in test]
href = [i['href'].split('/')[1] for i in test]
countries = ','.join(countries)
href = ','.join(href)
statsdict = {}
page1 = requests.get('https://www.worldometers.info/coronavirus/#countries')
stat = BeautifulSoup(page1.text, 'html.parser')


class Contentobj:
    def __init__(self,content = None,hre = None):
        self.content = content
        self.href = hre


class Error:
    def __init__(self, error= "Invalid Inputs"):
        self.error = error


class CountryNumbers:
    def __init__(self, name,tcases,acases,tdeath,perppi,rrate):
        self.name = name
        self.tcases = tcases
        self.acases = acases
        self.tdeath = tdeath
        self.perppi = perppi
        self.rrate = rrate


@api_view(['GET'])
def country_list(request, format=None):
    """
    List the countries affected.
                """
    if request.method == 'GET':
        comment = Contentobj(content=countries,hre = href)
        serializer = Country(comment)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Country(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class Country_List_Details(generics.ListCreateAPIView):
    """
        Listing the details for the requested Country
            """
    serializer_class = CountryListDetail
    search_fields = ['rrate']
    http_method_names = ['get']

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        try:
            country = self.kwargs['country']
            global stat, page1
            test = stat.find('a', class_='mt_a', href="country/" + country + "/").parent.parent.children
            stats = [i.text for i in list(test) if i != '\n']
            statsdict['name'] = stats[1]
            statsdict['tcases'] = stats[2]
            statsdict['acases'] = stats[8]
            statsdict['tdeath'] = stats[4]
            statsdict['perppi'] = round(int(stats[13].replace(',', '')) / int(stats[2].replace(',', '')), 2)
            statsdict['rrate'] = round(int(stats[13].replace(',', '')) / int(stats[2].replace(',', '')), 2)
            comment = CountryNumbers(name=statsdict['name'], tcases=statsdict['tcases'], acases=statsdict['acases'],
                                         tdeath=statsdict['tdeath'], perppi=statsdict['perppi'], rrate=statsdict['rrate'])
            a = []
            a.append(comment)
            queryset = a
            return queryset

        except(TypeError, ValueError,AttributeError):
            error = Error()
            a = []
            self.serializer_class = ErrorSerializer
            a.append(error)
            queryset = a
            return queryset










