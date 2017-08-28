# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import QueryForm
from .search import find_records, get_all_experiments, get_all_hybrids
from .result import QueryInfo, DataSchema, ReservedFields
#from highcharts.views import HighChartsBarView

# Create your views here.
def make_query(request):
    result = None
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            options = QueryInfo(form.cleaned_data['experiment'], form.cleaned_data['hybrid'])
            for item in DataSchema:
                cname = "control_" + str(item[1] - ReservedFields)
                dcontrol = form.cleaned_data[cname]
                if dcontrol:
                    options.mark(item[0])
            result = find_records(form.cleaned_data['experiment'], form.cleaned_data['hybrid'], options.data)
            result.set_query(options)
            return render(request, 'webquery/make_reply.html', {'result': result})
    form = QueryForm
    form.declared_fields['experiment'].choices = get_all_experiments()
    hybrids = get_all_hybrids()
    hybrids.insert(0, (None, 'Все'))
    form.declared_fields['hybrid'].choices = hybrids
    return render(request, 'webquery/make_query.html', {'form': form})

