# I have created this file - Vinay

from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    #return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default') # here default is default value if we did't get any text
    oldtext = djtext # A reference of old text
    if djtext == "":
        return redirect("/")

    # Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # its a list of operations
    djpurpose = []

    # its blank analyzed text string
    analyzed=""

    # REMOVE PUNCTUATIONS
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char

        djtext = analyzed
        djpurpose.append("Removed Punctuations !")

    # UPPERCASE
    if uppercase == "on":
        analyzed = djtext.upper()
        djtext = analyzed
        djpurpose.append("Converted to Uppercase !")

    # NEW LINE REMOVER
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r': # '\r' because in network '\n' and '\r' sent to transport new line character
                analyzed+=char

        djtext = analyzed
        djpurpose.append("Removed New Line !")

    # EXTRA SPACE REMOVER
    # Removes more than 1 spaces in text
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            try:
                if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                    analyzed+=char
            except:
                pass
        
        djpurpose.append("Removed Extra Space !")

    # CHARACTER COUNTER
    counter = -1
    newcounter = -1
    if charactercounter == "on":
        print("---->", len(analyzed))
        counter = 0
        for char in oldtext:
            if char != ' ':
                counter+=1

        newcounter = 0
        if analyzed != "" and counter != -1:
            for char in analyzed:
                 if char != ' ':
                    print(char)
                    newcounter+=1

        djpurpose.append("Character Counted !")

    if (newlineremover != 'on' and removepunc != 'on' and uppercase != 'on' and extraspaceremover != 'on' and charactercounter != 'on'):
        return HttpResponse("Error Occured ! Please select one operation !")

    # CREATING PARAM = Parameters to be sent in template
    params = {
            'purposes': djpurpose,
            'analyzed_text': analyzed,
            'oldcharactercount': counter,
            'newcharactercount': newcounter,
            #'oldcharactercount': len(oldtext),
            #'newcharactercount': len(analyzed),
        }
    return render(request, 'analyze.html', params)


## THIS IS TESTING STRING
    '''This        is
my;;
website'''