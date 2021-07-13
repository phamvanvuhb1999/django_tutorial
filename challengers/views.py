from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenger, Result, Test
from random import randint

def index(request):
    def getSet():
        return MODEL.objects.all()
    is_relate = False
    model = request.GET.get('model', '');
    MODEL = None
    if model=='Challenger':
        MODEL = Challenger
    elif model=='Test':
        MODEL = Test
    else:
        MODEL = Result
        is_relate = True
    temp = getSet()
    result = '__________'.join([(f'{c.challenger_id}-{c.test_id}' if is_relate else f'{c.id}->{c.name}') for c in temp])
    return HttpResponse(result);

def service(request):
    get_the_best =   '''SELECT Result.challenger_id as id, Challenger.name
                        FROM (
                            (Result INNER JOIN Test ON Result.test_id=Test.id) as RT 
                                group by Result.challenger_id 
                                ORDER BY COUNT(Result.level)
                            ) as RTA INNER JOIN Challenger
                            ON Challenger.id=RTA.id'''
    

    return HttpResponse('t')


def auto_create_challenger_test_result(request):
    name1 = 'A'
    name2 = 'a'
    for index in range(20):
        level = randint(1,10)

        Challenger.objects.create(name=name1)
        Test.objects.create(name=name2, level=level)

        name2 = chr(ord(name2) + 1)
        name1 = chr(ord(name1) + 1)
    auto_creat_result()
    return HttpResponse('created')

def auto_creat_result(*args, **kwargs):
    for index in range(40):
        challenger_id = randint(21,61);
        test_id = randint(21,61)
        challenger = Challenger.objects.filter(pk=challenger_id).first()
        test = Test.objects.filter(pk=test_id).first()
        if challenger and test:
            Result.objects.create(challenger_id=challenger, test_id=test)
def auto_create_result_single(request):
    auto_creat_result()
    return HttpResponse('created result')