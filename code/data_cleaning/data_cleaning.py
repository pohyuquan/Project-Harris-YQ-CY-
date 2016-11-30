import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

#append and clean state performance math and reading data
#import state performance math data and create year variable
df1 = pd.read_csv("Math 08-09.csv")
df1['Year'] = np.array(2008)
df1.rename(columns = {"leanm08":"Name of reporting district"}, inplace=True)
df2 = pd.read_csv("Math 09-10.csv")
df2['Year'] = np.array(2009)
df2.rename(columns = {"leanm09":"Name of reporting district"}, inplace=True)
df3 = pd.read_csv("Math 10-11.csv")
df3['Year'] = np.array(2010)
df3.rename(columns = {"leanm10":"Name of reporting district"}, inplace=True)
df4 = pd.read_csv("Math 11-12.csv")
df4['Year'] = np.array(2011)
df4.rename(columns = {"leanm11":"Name of reporting district"}, inplace=True)
#append state performance math reports from 2008 t0 2011
math = df1.append([df2, df3, df4])

#import state performance reading data and create year variable
read1 = pd.read_csv("Reading 08-09.csv")
read1['Year'] = np.array(2008)
read1.rename(columns = {"leanm08":"Name of reporting district"}, inplace=True)
read2 = pd.read_csv("Reading 09-10.csv")
read2['Year'] = np.array(2009)
read2.rename(columns = {"leanm09":"Name of reporting district"}, inplace=True)
read3 = pd.read_csv("Reading 10-11.csv")
read3['Year'] = np.array(2010)
read3.rename(columns = {"leanm10":"Name of reporting district"}, inplace=True)
read4 = pd.read_csv("Reading 11-12.csv")
read4['Year'] = np.array(2011)
read4.rename(columns = {"leanm11":"Name of reporting district"}, inplace=True)

#append state performance math reports from 2008 t0 2011
read = read1.append([read2, read3, read4])

#merge math and reading performance data on Name of reporting district, State and Year
list = ['LEAID', 'STNAM', 'Year']
mathread = pd.merge(math, read, left_on = list , right_on = list)

#rename column headers
mathread.rename(columns = {"STNAM": "State", "LEAID": "DISTRICT_ID", "Name of reporting district_x": 'Name of reporting district'}, inplace=True)
# setting columns to be matched to be of lower case
mathread['State'] = mathread['State'].str.lower()
mathread['Name of reporting district'] = mathread['Name of reporting district'].str.lower()

#removing extra spaces on the start and end of strings
mathread["State"] = pd.core.strings.str_strip(mathread["State"])

#removing duplicate columns
drop_col = ['FIPST_x', 'FIPST_y', 'Name of reporting district_y']
mathread.drop(drop_col, axis=1, inplace=True)

#removing values that were not valid (e.g. GE50). These values were because of the small sample size in certain groups in order to maintain anonimity.
mathread = mathread.replace('^[A-Z]{2}', np.nan, regex=True)
#rounding down ranges (ranges were used for small sample sizes to maintain anonimity)
mathread = mathread.replace('-[0-9]{2}$', "", regex=True)
#some values appeared as dates, no idea why. Removed them.
mathread = mathread.replace('[0-9]-[A-Za-z]{3}', np.nan, regex=True)

#replace n/a to nan to be identifiable by pandas
mathread = mathread.replace('n/a', np.nan)

#making Name of reporting district identical as fiscal dataset
mathread['Name of reporting district'] = np.where(mathread['State'] == 'california',
                                                  mathread['Name of reporting district'].astype(str)+ str(' school district'),
                                                  mathread['Name of reporting district'])

mathread['Name of reporting district'] = np.where(mathread['State'] == 'alabama',
                                                  mathread['Name of reporting district'].astype(str)+ str(' school district'),
                                                  mathread['Name of reporting district'])

mathread['Name of reporting district'] = np.where(mathread['State'] == 'florida', mathread['Name of reporting district'].astype(str)+ str(' county school district'), mathread['Name of reporting district'])
mathread.ix[mathread["State"] == "illinois", "Name of reporting district"] = mathread.ix[mathread["State"] == "illinois", "Name of reporting district"].str.replace("sd", "school district")
mathread.ix[mathread["State"] == "pennsylvania", "Name of reporting district"] = mathread.ix[mathread["State"] == "pennsylvania", "Name of reporting district"].str.replace("city sd", "school district")

#remove double statistic
mathread.ix[mathread["State"] == "texas", "Name of reporting district"] = mathread.ix[mathread["State"] == "texas", "Name of reporting district"].str.replace("northside", "ns")
mathread.ix[mathread["State"] == "south carolina", "Name of reporting district"] = mathread.ix[mathread["State"] == "south carolina", "Name of reporting district"].str.replace("greenville 01", "greenville county school district")
mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"] = mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"].str.replace("memphis city schools district$", "memphis city schools")
mathread.ix[mathread["State"] == "arizona", "Name of reporting district"] = mathread.ix[mathread["State"] == "arizona", "Name of reporting district"].str.replace("district", "school district")
mathread.ix[mathread["State"] == "utah", "Name of reporting district"] = mathread.ix[mathread["State"] == "utah", "Name of reporting district"].str.replace("district", "school district")
mathread.ix[mathread["State"] == "georgia", "Name of reporting district"] = mathread.ix[mathread["State"] == "georgia", "Name of reporting district"].str.replace("county", "county school district")
mathread.ix[mathread["State"] == "alabama", "Name of reporting district"] = mathread.ix[mathread["State"] == "alabama", "Name of reporting district"].str.replace("county", "county school district")
mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"] = mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"].str.replace("knox county$", "knox county school district")
mathread.ix[mathread["State"] == "ohio", "Name of reporting district"] = mathread.ix[mathread["State"] == "ohio", "Name of reporting district"].str.replace("columbus city$", "columbus city school district")
mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"] = mathread.ix[mathread["State"] == "tennessee", "Name of reporting district"].str.replace("shelby county$", "shelby county school district")

#export cleaned file as csv
mathread.to_csv("processed_mathread08-11.csv")


#import state performance math data
df08 = pd.read_excel('100LSD_Fiscal_Tables_FY08.xlsx', header=2)
df09 = pd.read_excel('100LSD_Fiscal_Tables_FY09.xlsx', header=2)
df10 = pd.read_excel('100LSD_Fiscal_Tables_FY10.xlsx', header=2)
df11 = pd.read_excel('100LSD_Fiscal_Tables_FY11.xlsx', header=2)

#dropping missing values
df08.dropna(inplace = True)
df09.dropna(inplace = True)
df10.dropna(inplace = True)
df11.dropna(inplace = True)

#removing extra spaces on the start and end of strings
df10['Name of reporting district'] = pd.core.strings.str_strip(df10['Name of reporting district'])
df11['Name of reporting district'] = pd.core.strings.str_strip(df11['Name of reporting district'])

#create year variable
df08['Year'] = np.array(2008)
df09['Year'] = np.array(2009)
df10['Year'] = np.array(2010)
df11['Year'] = np.array(2011)

#rearranging the columns
cols = df10.columns.tolist()
col2 = cols[-1:] + cols[:-1]
df10 = df10[col2]
df11 = df11[col2]

#append fiscal data from 2008 to 2011
fiscal = df08.append([df09, df10, df11])

#setting matching columns to lowercase
fiscal['Name of reporting district'] = fiscal['Name of reporting district'].str.lower()
fiscal['State'] = fiscal['State'].str.lower()

#setting matching column year as integer
fiscal["Year"] = fiscal["Year"].astype(int)

#removing whitespaces at the start and end of string
fiscal["State"] = pd.core.strings.str_strip(fiscal["State"])

#stripping numbers at the end of arizona and texas school districts
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 1')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 901')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 902')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 903')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 904')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 905')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 906')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 907')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 908')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 909')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 910')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 911')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 912')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 913')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 914')
fiscal["Name of reporting district"] = fiscal["Name of reporting district"].str.strip(to_strip=' 915')

#rename name of reporting districts to be matching with mathread name of reporting district column
fiscal.ix[fiscal["State"] == "new mexico", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "new mexico", "Name of reporting district"].str.replace("school district", "public schools")
fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"].str.replace("county schools", "county public schools")
fiscal.ix[fiscal["State"] == "texas", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "texas", "Name of reporting district"].str.replace("arlington independent school$", "arlington independent school district")
fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"].str.replace("baltimore city schools$", "baltimore city public schools")
fiscal.ix[fiscal["State"] == "ohio", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "ohio", "Name of reporting district"].str.replace("columbus city$", "columbus city school district")
fiscal.ix[fiscal["State"] == "north carolina", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "north carolina", "Name of reporting district"].str.replace("cumberland county school$", "cumberland county schools")
fiscal.ix[fiscal["State"] == "michigan", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "michigan", "Name of reporting district"].str.replace("detroit public school district$", "detroit city school district")
fiscal.ix[fiscal["State"] == "georgia", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "georgia", "Name of reporting district"].str.replace("fulton county$", "fulton county school district")
fiscal.ix[fiscal["State"] == "georgia", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "georgia", "Name of reporting district"].str.replace("fulton county³$", "fulton county school district")
fiscal.ix[fiscal["State"] == "california", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "california", "Name of reporting district"].str.replace("garden grove unified school dist$", "garden grove unified school district")
fiscal.ix[fiscal["State"] == "north carolina", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "north carolina", "Name of reporting district"].str.replace("guilford county school$", "guilford county schools")
fiscal.ix[fiscal["State"] == "hawaii", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "hawaii", "Name of reporting district"].str.replace("hawaii public schools$", "hawaii department of education")
fiscal.ix[fiscal["State"] == "wisconsin", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "wisconsin", "Name of reporting district"].str.replace("milwaukee city school district$", "milwaukee school district")
fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"].str.replace("montgomery county school$", "montgomery county public schools")
fiscal.ix[fiscal["State"] == "florida", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "florida", "Name of reporting district"].str.replace("orange county school board$", "orange county school district")
fiscal.ix[fiscal["State"] == "florida", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "florida", "Name of reporting district"].str.replace("orange county public schools$", "orange county school district")
fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"] = fiscal.ix[fiscal["State"] == "maryland", "Name of reporting district"].str.replace("prince georges county public schools$", "prince george's county public schools")

fiscal.to_csv("processed_fiscal08-11.csv")


#merge fiscal and mathread from 2008 to 2011
#creating list of matching columns
list = ['State', 'Name of reporting district', 'Year']

#merge fiscal and mathread datasets
summary_stats = pd.merge(mathread, fiscal, left_on = list, right_on = list)

#remove unwanted columns
drop_col = ['Instructional-related current expenditures', 'Total expenditures', 'Federal revenues', 'State revenues', 'Local revenues']
summary_stats.drop(drop_col, axis=1, inplace=True)

#re-capitalizing data for presentation
summary_stats["Name of reporting district"] = summary_stats["Name of reporting district"].str.capitalize()
summary_stats["State"] = summary_stats["State"].str.capitalize()

#renaming index column for presentation
summary_stats.index.name = 'No.'

#renaming column headers
summary_stats.columns = summary_stats.columns.str.replace('numvalid', 'Number of Students')
summary_stats.columns = summary_stats.columns.str.replace('pctprof', '% Performance')
summary_stats.columns = summary_stats.columns.str.replace('_MTH', ' Math, ')
summary_stats.columns = summary_stats.columns.str.replace('_RLA', ' Reading, ')
summary_stats.columns = summary_stats.columns.str.replace('ALL', 'All Students,')
summary_stats.columns = summary_stats.columns.str.replace('00', 'All Grades,')
summary_stats.columns = summary_stats.columns.str.replace('01', 'Grade 1, ')
summary_stats.columns = summary_stats.columns.str.replace('02', 'Grade 2, ')
summary_stats.columns = summary_stats.columns.str.replace('03', 'Grade 3, ')
summary_stats.columns = summary_stats.columns.str.replace('04', 'Grade 4, ')
summary_stats.columns = summary_stats.columns.str.replace('05', 'Grade 5, ')
summary_stats.columns = summary_stats.columns.str.replace('06', 'Grade 6, ')
summary_stats.columns = summary_stats.columns.str.replace('07', 'Grade 7, ')
summary_stats.columns = summary_stats.columns.str.replace('08', 'Grade 8, ')

#export merged dataframe as csv
summary_stats.to_csv("merge_summary.csv")
