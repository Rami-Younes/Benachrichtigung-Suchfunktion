from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import CsvModelForm
import email, smtplib, ssl
import csv
from .models import CSV_JiraDB
import csv
from KundenInfo.models import Kundeninfo_Jira,Kundeninfo_Portal
from django.contrib.auth.models import User
# import win32com.client as client
# import pathlib
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

from django.contrib import messages

def compare(request):
    with open('D:\ProjectCSV\django\CSVSite\csvCompare\jiraDB_csv_auszug.csv', 'r') as t1, open('D:\ProjectCSV\django\CSVSite\csvCompare\PortalDB_csv_auszug.csv', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    with open('D:\ProjectCSV\django\CSVSite\csvCompare\Desired.csv', 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                row1 = " ".join(line)
                row1 = line.replace(";", "--**--")
                outFile.write(row1)

    context = {"csv_rows": []}
    with open('D:\ProjectCSV\django\CSVSite\csvCompare\Desired.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:

            context["csv_rows"].append(" ".join(row))
    return render(request, 'index.html', context)

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = CSV_JiraDB.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader) :
                if i== 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";"," ")
                    row = row.split()
                    fullname = row[0]
                    mail = row[1]
                    benutzername = row[2]
                    Kundeninfo_Portal.objects.create(
                        FullnameP=fullname,
                        E_MailP = mail,
                        BenutzernameP= benutzername
                    )
                    print(row)
    return render(request,'upload.html',{'form':form})






