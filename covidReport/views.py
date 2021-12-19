from django.shortcuts import render, redirect
from .models import CovidReport
from authentications.models import User


# Create your views here.
def uploadReport(request):
    if not 'email' in request.session.keys():
        return redirect('login')
    if request.method == "POST":
        file = request.FILES['file']
        print(file)
        user_obj = User.objects.get(email=request.session['email'])
        report_obj, created = CovidReport.objects.update_or_create(user=user_obj, defaults={'report': file,
                                                                                            'isReportPositive': False})

    return render(request, 'uploadReport.html', {})


def statusReport(request):
    if not 'email' in request.session.keys():
        return redirect('login')

    context = {}
    report_query = CovidReport.objects.get(user=User.objects.get(email=request.session['email']))
    context['report_link'] = report_query.report.url
    if report_query.isReportPositive:
        context['isReportPositive'] = True

    return render(request, 'statusReport.html', context)
