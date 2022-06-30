from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
# from jmespath import search

from .models import *

# Create your views here.
def HomePageFun(request):
    DataToshow = ModelForAddress.objects.all()
    # print(DataToshow)
    return render(request,"index.html",{'Data':DataToshow})
    # return render(request,'registerNewUser.html')

def AddNewFun(request):

    if request.method == "POST":
        srtoaddindb = request.POST['srnotoadd']
        phonetoaddindb = request.POST['phonetoadd']
        nametoaddindb = request.POST['nametoadd']
        addresstoaddindb = request.POST['addresstoadd']
        # print(nametoaddindb)
        if srtoaddindb != '' and phonetoaddindb != '' and nametoaddindb != '' and addresstoaddindb != '':
            AddedData =  ModelForAddress.objects.create(SrNo = srtoaddindb, NametoAdd = nametoaddindb, phonetoadd = phonetoaddindb, addresstoadd = addresstoaddindb)
            return render(request,'addnew.html',{'Added':True})
        else:
            return render(request,'addnew.html',{'notAdded':True})
    return render(request,'addnew.html')


def SearchFun(request):
    searchkeyword = request.POST['search']
    if searchkeyword == "":
        return render(request,'index.html',{'nullSearchValue':True})
    else:
        searchNameData = ModelForAddress.objects.filter(NametoAdd = searchkeyword)
        searchPhoneData = ModelForAddress.objects.filter(phonetoadd = searchkeyword)
        searchMailData = ModelForAddress.objects.filter(addresstoadd = searchkeyword)
        # print(searchNameData,searchMailData,searchPhoneData)
        # print(searchPhoneData)
        if (searchNameData.exists() or searchMailData.exists() or searchPhoneData.exists()):
            # print("Loop Entered")
            # print(searchMailData)
            if((searchNameData.exists()) and (not searchMailData.exists()) and (not searchPhoneData.exists())):
                # print("Data -: ", searchNameData)
                return render(request,'index.html',{'Data':searchNameData})
            elif((not searchNameData.exists()) and (searchMailData.exists()) and (not searchPhoneData.exists())):
                return render(request,'index.html',{'Data':searchMailData})
            elif((not searchNameData.exists()) and (not searchMailData.exists()) and (searchPhoneData.exists())):
                return render(request,'index.html',{'Data':searchPhoneData})
            else:
                totalFilteredData = searchMailData | searchMailData
                return render(request,'index.html',{'Data':totalFilteredData})
        else:
            return render(request,'index.html',{'noDataFound':True})   


