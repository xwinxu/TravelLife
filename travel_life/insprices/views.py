from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

import datetime

from .models import *

def index(request):
    return HttpResponse(render(request, 'insprices/sitecover.html'))


def ticplan(request):
    tic_med_plans = TicplanMed.objects.order_by('age_from')
    tic_nomed_plans = TicplanNomed.objects.order_by('age_from')
    context = {
        'tic_med_plans': tic_med_plans,
        'tic_nomed_plans': tic_nomed_plans,
    }

    return HttpResponse(render(request, 'insprices/ticplan.html', context))


def berkplan(request):
    berk_med_plans = BerkplanMed.objects.order_by('age_from')
    berk_nomed_plans = BerkplanNomed.objects.order_by('age_from')
    context = {
        'berk_med_plans': berk_med_plans,
        'berk_nomed_plans': berk_nomed_plans,
    }

    return HttpResponse(render(request, 'insprices/berkplan.html', context))


def alliplan(request):
    alli_med_plans = AlliplanMed.objects.order_by('age_from')
    alli_nomed_plans = AlliplanNomed.objects.order_by('age_from')
    context = {
        'alli_med_plans': alli_med_plans,
        'alli_nomed_plans': alli_nomed_plans,
    }

    return HttpResponse(render(request, 'insprices/alliplan.html', context))


def manuplan(request):
    manu_med_plans = ManuplanMed.objects.order_by('age_from')
    manu_nomed_plans = ManuplanNomed.objects.order_by('age_from')
    context = {
        'manu_med_plans': manu_med_plans,
        'manu_nomed_plans': manu_nomed_plans,
    }

    return HttpResponse(render(request, 'insprices/manuplan.html', context))


def prices(request):
    request.session['age'] = request.GET.get('age', '')
    request.session['coverage'] = request.GET.get('coverage', '')
    request.session['start_day'] = request.GET.get('start[0]', '')
    request.session['start_month'] = request.GET.get('start[1]', '')
    request.session['start_year'] = request.GET.get('start[2]', '')
    request.session['end_day'] = request.GET.get('end[0]', '')
    request.session['end_month'] = request.GET.get('end[1]', '')
    request.session['end_year'] = request.GET.get('end[2]', '')

    # alli_nomed_plans = AlliplanNomed.objects.all()
    # alli_med_plans = AlliplanMed.objects.all()
    # berk_nomed_plans = BerkplanNomed.objects.all()
    # berk_med_plans = BerkplanMed.objects.all()
    # manu_nomed_plans = ManuplanNomed.objects.all()
    # manu_med_plans = ManuplanMed.objects.all()
    # tic_nomed_plans = TicplanNomed.objects.all()
    # tic_med_plans = TicplanMed.objects.all()

    # context = {
    #     'alli_nomed_plans': alli_nomed_plans,
    #     'alli_med_plans': alli_med_plans,
    #     'berk_nomed_plans': berk_nomed_plans,
    #     'berk_med_plans': berk_med_plans,
    #     'manu_nomed_plans': manu_nomed_plans,
    #     'manu_med_plans': manu_med_plans,
    #     'tic_nomed_plans': tic_nomed_plans,
    #     'tic_med_plans': tic_med_plans,
    # }

    return HttpResponseRedirect(reverse('insprices:results'))

def filter_plans(plans, age):
    for plan in plans:
        for entry in plan:
            if (age < int(entry.age_from) or age > int(entry.age_to)):
                entry = None

def results(request):
#    nomed_plans = TicplanNomed.objects.order_by('age_from')
#    med_plans = TicplanMed.objects.order_by('age_from')
#
#    for i in med_plans:
#        if (age >= i.age_from and age <= i.age_to):
#            output = "With stable medical coverage: $10k - {0}, \
#            $15k - {1}, $25k - {2}, $50k - {3}, $100k - {4}, $150k - {5}\n".format(
#            str(i.cov_10k), str(i.cov_15k), str(i.cov_25k), str(i.cov_50k),
#            str(i.cov_100k), str(i.cov_150k))
#            break
#
#    for j in nomed_plans:
#        if (age >= j.age_from and age <= j.age_to):
#            output = output +  "Without stable medical coverage: $10k - {0}, \
#            $15k - {1}, $25k - {2}, $50k - {3}, $100k - {4}, $150k - {5}".format(
#            str(j.cov_10k), str(j.cov_15k), str(j.cov_25k), str(j.cov_50k),
#            str(j.cov_100k), str(j.cov_150k))
#            break
#
#    return HttpResponse(output)
    start = (request.session['start_year'], request.session['start_month'], request.session['start_day'])
    end = (request.session['end_year'], request.session['end_month'], request.session['end_day'])

    age = int(request.session['age'])
    start_date = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    end_date = datetime.date(int(end[0]), int(end[1]), int(end[2]))

    # duration = (end_date - start_date).days

    alli_nomed_plans = AlliplanNomed.objects.all()
    alli_med_plans = AlliplanMed.objects.all()
    berk_nomed_plans = BerkplanNomed.objects.all()
    berk_med_plans = BerkplanMed.objects.all()
    manu_nomed_plans = ManuplanNomed.objects.all()
    manu_med_plans = ManuplanMed.objects.all()
    tic_nomed_plans = TicplanNomed.objects.all()
    tic_med_plans = TicplanMed.objects.all()

    ins_plans = [
        alli_nomed_plans, alli_med_plans, berk_nomed_plans, berk_med_plans,
        manu_nomed_plans, manu_med_plans, tic_nomed_plans, tic_med_plans
    ]

    filter_plans(ins_plans, age)

    context = {
        'alli_nomed_plans': ins_plans[0],
        'alli_med_plans': ins_plans[1],
        'berk_nomed_plans': ins_plans[2],
        'berk_med_plans': ins_plans[3],
        'manu_nomed_plans': ins_plans[4],
        'manu_med_plans': ins_plans[5],
        'tic_nomed_plans': ins_plans[6],
        'tic_med_plans': ins_plans[7],
        'age': age,
        'coverage': request.session['coverage'],
        'start': start_date,
        'end': end_date,
        'duration': (end_date - start_date).days,
    }

    return render(request, 'insprices/results.html', context)

def 