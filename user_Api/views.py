from django.shortcuts import render
import http.client
import json


def home(request):
    conn = http.client.HTTPSConnection("randomuser.me")
    payload = ''
    headers = {
        'Cookie': '__cfduid=d00f73759f0bfd85eb3582cfb4ee1f5871611607709'
    }
    conn.request("GET", "/api/?results=1000", payload, headers)
    res = conn.getresponse()

    data = res.read()


    #print(data.decode("utf-8"))
    return render(request, 'user_Api/home.html')
