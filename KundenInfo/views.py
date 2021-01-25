from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from KundenInfo.models import Kundeninfo_Jira,Kundeninfo_Portal
def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match = Kundeninfo_Jira.objects.filter(Q(Fullname__contains=srch))
            match2 = Kundeninfo_Portal.objects.filter(Q(FullnameP__contains=srch))

            if match and match2 :
                return render(request,'search.html',{'sr':match, 'sr2':match2})
            elif match:
                messages.error(request, 'Keine Ergebnisse  in Portal-DB')
                return render(request, 'search.html', {'sr': match})
            elif match2:
                messages.error(request,'Keine Ergebnisse in jira-DB')
                return render(request, 'search.html', {'sr2': match2})
            else:
                messages.error(request,'Nicht gefunden in beide Datenbanken')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
