from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy


from os.path import join
from django.conf import settings

import numpy as np, pandas as pd
import matplotlib.pyplot as plt

from .forms import InputForm
from .forms import InputForm1
from .models import STATES_DICT

from .forms import SchoolsForm
from .forms import SchoolsForm1
from .models import SCHOOL_DISTRICTS_DICT

from .forms import GradesForm
from .models import GRADES_DICT

from .forms import SubgroupForm
from .models import SUBGROUP_DICT

from .forms import SubjectForm
from .models import SUBJECT_DICT

import geopandas as gpd, folium
from geopy.geocoders import Nominatim

import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO

from django.views.generic import FormView

def index(request):

    return render(request, "base_data.html")


def team(request):

    return render(request, "team.html")


def data(request):

    return render(request, "data.html")


def code(request):

    return render(request, "code.html")


def display_table(request, a = "a", b = "b", c = "c", d = "d"):

    state = request.GET.get('state', 'Alaska')
    gradelevel = request.GET.get('gradelevel', 'All Grades')
    subgroups = request.GET.get('subgroups', 'All Students')
    topic = request.GET.get('topic', 'Math')

    params = {'title' : state,
              'form_action' : reverse_lazy('myapp:display_table'),
              'form_method' : 'get',
              'form' : InputForm1({'state' : state}),
              'form1' : GradesForm({'gradelevel' : gradelevel,}),
              'form2' : SubgroupForm({'subgroups' : subgroups,}),
              'form3' : SubjectForm({'topic' : topic,}),
              'html_table' : plottable(request, a = state, b = gradelevel, c = subgroups, d = topic),
              'State_Name' : state,
              'Variable2' : gradelevel,
              'Variable3' : subgroups,
              'Variable4' : topic}

    return render(request, 'view_table.html', params)


def plottable(request, a = "Alaska", b = "All Grades", c = "All Students", d = "Math"):

    filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

    df = pd.read_csv(filename)

    df = df[df["State"].str.lower() == a.lower()]
    af = df.filter(regex= b)
    af = af.filter(regex= c)
    af = af.filter(regex= d)
    cols=set(af.columns)
    cols.add('Year')
    cols.add('Name of reporting district')
    cols.add('Current expenditures per pupil')
    cols.add('Total revenues')
    cols.add('Current expenditures  ')
    cols = list(cols)
    df2 = df[cols]
    colss = df2.columns.tolist()
    colss = colss[-13:] + colss[:-13]
    df2 = df2[colss]

    return df2.to_html(float_format = "%.3f", classes = "table table-striped", index = False)


def display_pic(request, c = 'r'):

    district = request.GET.get('district', 'Albuquerque Public Schools')

    params = {'title' : district,
              'form_action' : reverse_lazy('myapp:display_pic'),
              'form_method' : 'get',
              'form' : SchoolsForm({'district' : district}),
              'pic_source' : reverse_lazy("myapp:plotmath", kwargs = {'c' : district}),
              'pic_source1' : reverse_lazy("myapp:plotreading", kwargs = {'c' : district}),
              'pic_source2' : reverse_lazy("myapp:plotexpenditure", kwargs = {'c' : district}),
              'District_Name' : district}

    return render(request, 'view_pic.html', params)


def plotmath(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   ax = df[["All Students, Math, All Grades,% Performance"]].plot(legend=False, ylim = [0,100])
   ax.set_ylabel("Met Performance Requirements (%)")
   plt.title('% of Students Hitting Performance Score (Math)', color='black')

   # write bytes instead of file.
   figfile = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")


def plotreading(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   ax = df[["All Students, Reading, All Grades,% Performance"]].plot(legend=False, ylim = [0,100])
   ax.set_ylabel("Met Performance Requirements (%)")
   plt.title('% of Students Hitting Performance Score (Reading)', color='black')

   # write bytes instead of file.
   figfile = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")


def plotexpenditure(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   dx = df[["Current expenditures per pupil"]].plot(legend=False)
   dx.set_ylabel("Expenditure per Student ($)")
   plt.title('Expenditure Per Student', color='black')

   # write bytes instead of file.
   figfile1 = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: dx.figure.savefig(figfile1, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile1.seek(0) # rewind to beginning of file
   return HttpResponse(figfile1.read(), content_type="image/png")


def display_picrelation(request, c = 'r', d = 'p'):

    district = request.GET.get('district', 'Albuquerque Public Schools')

    params = {'title' : district,
              'form_action' : reverse_lazy('myapp:display_picrelation'),
              'form_method' : 'get',
              'form' : SchoolsForm({'district' : district}),
              'pic_source' : reverse_lazy("myapp:plotrelationmath", kwargs = {'c' : district}),
              'pic_source1' : reverse_lazy("myapp:plotrelationreading", kwargs = {'c' : district}),
              'District_Name' : district}

    return render(request, 'view_pic1.html', params)


def plotrelationmath(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   ax = df[["Current expenditures per pupil", "All Students, Math, All Grades,% Performance"]]
   ax = ax.plot(x = "Current expenditures per pupil", y = "All Students, Math, All Grades,% Performance", legend=False, ylim = (0,100))
   ax.set_ylabel("Met Performance Requirements (%)")
   ax.set_xlabel("Current expenditures per pupil ($)")
   plt.title('Expenditure vs Performance Math ('+c+')', color='black', y = 1.03, fontsize=15)

   # write bytes instead of file.
   figfile1 = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile1, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile1.seek(0) # rewind to beginning of file
   return HttpResponse(figfile1.read(), content_type="image/png")

def plotrelationreading(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   ax = df[["Current expenditures per pupil", "All Students, Reading, All Grades,% Performance"]]
   ax = ax.plot(x = "Current expenditures per pupil", y = "All Students, Reading, All Grades,% Performance", legend=False, ylim = (0,100))
   ax.set_ylabel("Met Performance Requirements (%)")
   ax.set_xlabel("Current expenditures per pupil ($)")
   plt.title('Expenditure vs Performance Reading ('+c+')', color='black', y = 1.03, fontsize=15y)

   # write bytes instead of file.
   figfile1 = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile1, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile1.seek(0) # rewind to beginning of file
   return HttpResponse(figfile1.read(), content_type="image/png")


def variables(request, a = "a", b = "b", c = "c", d = "d"):

    district = request.GET.get('district', 'Albuquerque Public Schools')
    gradelevel = request.GET.get('gradelevel', 'All Grades')
    subgroups = request.GET.get('subgroups', 'All Students')
    topic = request.GET.get('topic', 'Math')

    params = {'form_action' : reverse_lazy('myapp:variables'),
              'form_method' : 'get',
              'form' : SchoolsForm1({'district' : district,}),
              'form1' : GradesForm({'gradelevel' : gradelevel,}),
              'form2' : SubgroupForm({'subgroups' : subgroups,}),
              'form3' : SubjectForm({'topic' : topic,}),
              'pic_source' : reverse_lazy("myapp:plotvariable", kwargs = {'a' : district, 'b' : gradelevel, 'c' : subgroups, 'd' : topic}),
              'Variable1' : district,
              'Variable2' : gradelevel,
              'Variable3' : subgroups,
              'Variable4' : topic}

    return render(request, 'variables.html', params)


def plotvariable(request, a = "Albuquerque Public Schools", b = "All Grades", c = "All Students", d = "Math"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == a.lower()]
   af = df.filter(regex= b)
   af = af.filter(regex= c)
   af = af.filter(regex= d)
   af = af.filter(regex= '% Performance')
   cols=set(af.columns)
   cols.add('Current expenditures per pupil')
   cols = list(cols)
   df2 = df[cols]

   df2.set_index("Current expenditures per pupil")
   ax = df2.plot(legend=False, ylim = (0,100))
   ax.set_ylabel("% Performance")
   ax.set_xlabel("Current expenditures per pupil ($)")
   plt.title('Expenditure vs Performance', color='black')

   # write bytes instead of file.
   figfile = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")


def final(request):

    params = {'Plot1' :  reverse_lazy("myapp:finalplotmath"),
              'Plot2' :  reverse_lazy("myapp:finalplotread")
              }

    return render(request, 'final.html', params)


def finalplotmath(request):

    filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

    df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

    ax = df[["Current expenditures per pupil", "All Students, Math, All Grades,% Performance"]]
    ax = ax.plot(kind = 'scatter', x = "Current expenditures per pupil", y = "All Students, Math, All Grades,% Performance", legend=False, ylim = (0,100))
    ax.set_ylabel("% Performance")
    ax.set_xlabel("Current expenditures per pupil ($)")
    plt.title('Expenditure vs Performance (Math)', color='black')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    figfile = BytesIO()

    plt.subplots_adjust(bottom = 0.16)
    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")

    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")


def finalplotread(request):

    filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

    df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

    ax = df[["Current expenditures per pupil", "All Students, Reading, All Grades,% Performance"]]
    ax = ax.plot(kind = 'scatter', x = "Current expenditures per pupil", y = "All Students, Reading, All Grades,% Performance", legend=False, ylim = (0,100))
    ax.set_ylabel("% Performance")
    ax.set_xlabel("Current expenditures per pupil ($)")
    plt.title('Expenditure vs Performance (Reading)', color='black')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    figfile = BytesIO()

    plt.subplots_adjust(bottom = 0.16)
    try: ax.figure.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such color")

    figfile.seek(0)

    return HttpResponse(figfile.read(), content_type="image/png")


def contact_us(request):

    m = folium.Map([41.789621, -87.596398],
                   tiles='cartodbpositron',
                   zoom_start=14, max_zoom=16, min_zoom=4)

    folium.Marker(location=[41.789621, -87.596398], popup='University of Chicago').add_to(m)
    folium.ClickForMarker(popup='Waypoint')

    return render(request, 'contact_us.html')
