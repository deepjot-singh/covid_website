from django.shortcuts import render, redirect
from .models import CovidDailyCount, CovidStateCount, VaccinationCenters


# Create your views here.
def covidCasesInformation(request):
    if not 'email' in request.session.keys():
        return redirect('login')
    count, date = getDataDaily()
    total_cases = getTotalCases()
    state_data = getStateData(total_cases)
    context = {}
    context['DailyDataDate'] = date
    context['DailyDataCount'] = count
    context['StateData'] = state_data
    return render(request, 'covidInformation.html', context)


def covidVaccinationInformation(request):
    if not 'email' in request.session.keys():
        return redirect('login')

    context = {}
    vaccination_centers = VaccinationCenters.objects.all()
    context['VaccinationCenters'] = vaccination_centers
    return render(request, 'covidVaccinationInformation.html', context)

def getTotalCases():
    query = CovidStateCount.objects.all()
    total_count = 0
    for data in query:
        total_count += int(data.count)
    return total_count

def getStateData(totalCase:int):
    query = CovidStateCount.objects.all()
    state_data = []
    for data in query:
        state_percentage = int(int(data.count) * 100 / totalCase)
        state_data.append({"state": data.stateName.stateName, "percentage": state_percentage})

    return state_data

def getDataDaily():
    query = CovidDailyCount.objects.order_by('currentDate')
    count = []
    date = []
    for data in query:

        count.append(data.count)
        date.append(data.currentDate.strftime("%Y-%m-%d"))
    return count, date
