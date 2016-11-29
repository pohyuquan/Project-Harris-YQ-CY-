# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
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
from geopy import Nominatim

import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO

from django.views.generic import FormView

def index(request):

    return render(request, "base_data.html")

def data(request):

    return render(request, "data.html")

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
              'html_table' : reverse_lazy("myapp:plottable", kwargs = {'a' : state, 'b' : gradelevel, 'c' : subgroups, 'd' : topic}),
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
    colss = colss[-6:] + colss[:-6]
    df2 = df2[colss]

    table = df2.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "")
    table

    return HttpResponse(table)

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

def display_picrelation(request, c = 'r'):

    district = request.GET.get('district', 'Albuquerque Public Schools')

    params = {'title' : district,
              'form_action' : reverse_lazy('myapp:display_picrelation'),
              'form_method' : 'get',
              'form' : SchoolsForm({'district' : district}),
              'pic_source1' : reverse_lazy("myapp:plotrelation", kwargs = {'c' : district}),
              'District_Name' : district}

    return render(request, 'view_pic.html', params)

def plotrelation(request, c = "Albuquerque Public Schools"):

   filename = join(settings.STATIC_ROOT, 'myapp/merge_summary.csv')

   df = pd.read_csv(filename, index_col = "Year", parse_dates = ["Year"])

   df = df[df["Name of reporting district"].str.lower() == c.lower()]
   if not df.size: return HttpResponse("No such district!")

   ax = df[["Current expenditures per pupil", "All Students, Math, All Grades,% Performance"]]
   ax = ax.plot(x = "Current expenditures per pupil", y = "All Students, Math, All Grades,% Performance", legend=False, ylim = (0,100))
   ax.set_ylabel("Met Performance Requirements (%)")
   ax.set_xlabel("Current expenditures per pupil ($)")
   plt.title('Expenditure vs Performance ('+c+')', color='black', y = 1.03)

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

class FormClass(FormView):

    template_name = 'form.html'
    form_class = InputForm


    def get(self, request):

      state = request.GET.get('state', 'Alaska')

      return render(request, self.template_name, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})

    def post(self, request):

      state = request.POST.get('state', 'Alaska')

      return render(request, self.template_name, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})

def resp_redirect(request):

    state = request.POST.get('state', '')
    if not state: state = request.GET.get('state', '')

    if state: return HttpResponseRedirect(reverse_lazy('myapp:resp', kwargs = {'state' : state}))

    return HttpResponseRedirect(reverse_lazy('myapp:form'))


def resp(request, state):

    return HttpResponse("I hear you, {}.".format(STATES_DICT[state]))


def embedded_map(request):

  filename = join(settings.STATIC_ROOT, 'myapp/TM_WORLD_BORDERS_SIMPL-0.3.shp')

  m = folium.Map([39.828175, -98.5795], tiles='stamenwatercolor', zoom_start = 1)

  df = gpd.read_file(filename)

  mountains = ["Aconcagua", "Mount Kosciuszko", "Mont Blanc, Chamonix", "Mount Everest", "Denali", "Mount Elbrus", "Puncak Jaya", "Mount Kilimanjaro", "Mount Vinson"]
  mtn_df = gpd.tools.geocode(mountains, provider = "googlev3").to_crs(df.crs)

  folium.GeoJson(gpd.sjoin(df, mtn_df, how = "inner", op = "contains"),
                 style_function=lambda feature: {
                  'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
                 }).add_to(m)

  for xi, pt in mtn_df.iterrows():
      folium.RegularPolygonMarker(pt.geometry.coords[::][0][::-1], popup=pt.address,
                          number_of_sides = 5, radius = 8, fill_color = "black", fill_opacity = 1.0).add_to(m)

  map_string = m._repr_html_().replace("width:100%;", "width:60%;float:right;", 1)

  return render(request, 'view_map.html', {"title" : "Seven Summits",
                                           "map_string" : map_string})
