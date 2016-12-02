# Introduction to Programming for Public Policy / Harris 30550 Final Project (Yu Quan Poh and Cheng Yee Lim)

<h1>Introduction</h1>
There has little agreement over the effectiveness of school expenditures in improving school or student performance. In some studies, student achievement seems unrelated to measures of resources directed to the schools. However, if schools were able to direct resources in productive ways, higher school expenditures would result in better schools i.e. better student performance, more extensive facilities, and more qualified teachers. Our project examines the relationship between school expenditures in improving school performance in the top 100 largest U.S. school districts from 2008-2011. We used proportion of students achieving the national math and reading proficiency levels as a proxy of school performance and current expenditures per student as a proxy of school resources. We were unable to identify a positive or negative relationship between school performance and school expenditures in our preliminary analysis, primarily due to the short timespan of our panel data. While our preliminary analysis was with mixed success, our site remains as a good exploratory tool for school expenditure and school performance indicators.

<h1>Data</h1>
Our dataset consists of information from 2008 to 2011 for 73 out of 100 largest school districts in America. We compiled the dataset by merging two datasets: Fiscal Data Tables from the <em><a href = "http://nces.ed.gov/">U.S. Department of Education: National Center for Education Statistics</a></em> and Consolidated State Performance Report from <em><a href = "http://www2.ed.gov/about/offices/list/oese/index.html">U.S. Department of Education: Office of Elementary and Secondary Education</a></em>. The fiscal data tables consolidates total students, revenues, current expenditures, current expenditures per pupil, total expenditures, and total expenditures per pupil for the 100 largest public elementary and secondary school districts in the United States from 2008 to 2011. The Consolidated State Performance Report (CSPR) consists of school performance math and reading indicators that can be stratified by grades or demographics. The collated data also serve to evaluate of the extent of attaining ESEA Goals in U.S. schools.
* Maintaining high standards of a minimum attaining proficiency or better in reading/language arts and mathematics</li>
* Safe, drug free and conducive learning environments
* 100% high school graduation rates

<h2>Cleaning</h2>
1. Appended annual Fiscal Data Tables, Consolidated State Performance Math Reports, Consolidated State Performance Reading Reports  from 2008 to 2011
2. Merged Consolidated State Performance Math and Reading Reports on the Name of school (reporting) district, State and Year
3. Reformated names of school districts in math and reading reports to match those in the Fiscal Data Tables i.e. replacing SD with school district, stripping irrelevant numbers, stripping redundant spaces
4. Merged Fiscal Data Tables and Consolidated State Performance Reports (Math and Reading) on Name of school (reporting) district, State and Year
5. Renamed relevant column headers to be more intuitive i.e. 'numvalid': 'Number of Students', 'MTH': 'Math'

The cleaning code can be found <a href = "https://github.com/pohyuquan/Project-Harris-YQ-CY-/blob/master/code/data_cleaning/data_cleaning.py">here</a>.

The final merged data set can be accessed <a href = "https://github.com/pohyuquan/Project-Harris-YQ-CY-/blob/master/code/data_cleaning/merge_summary.csv">here</a>.

<h1>Launching and Navigating our Site </h1>
To successfully launch our site:<br>
1. Launch your terminal and enter `git clone https://github.com/pohyuquan/Project-Harris-YQ-CY-.git` <br>
2. Launch Python 3.4 environment in terminal so that you can view our maps. <br>
3. Change your working directory to the django folder, `cd Project-Harris-YQ-CY-/code/django` <br>
4. Launch the dynamic website by typing `python manage.py runserver` on a mac or `python manage.py runserver --noreload` on windows OS <br>
5. Open your web browser and go to http://localhost:8000/myapp to view the dynamic webpage 

After launching our dynamic website using terminal, you can navigate our site by clicking on the following buttons on the navigation bar at the top of the website:
* *Home* is the main page of our website 
* *The Team* contains information of our group members. 
* *Data* features our data sources and the process of cleaning and merging two datasets. 
* *Code* shows where the public can obtain our code for the django website and data cleaning.
* *Overall Relationship* shows static plots of school expenditure per student and math/reading performance.
* *Tables by State* allows the user to customise data tables of all school districts in the state, by selecting the state, grade level, subgroups of the students. The table generated will contain information on current expenditure per pupil, students that have taken the math/reading placement test and the percentage of them that have met the national proficiency standards. 
* *Plots by School Districts* allows the user to select and view summary plots of our key variables for individual schooling districts. 
* *Expenditure vs Performance* allows the user to select and plot the relationship between current expenditure per pupil and school performance (average of math and reading performance) for each school district.
* *Data Exploration* provides the user an interface, where they input the specific school district, grade level, subgroup of students and subject, to plot a line graph of school performance against current expenditures per school.

<h2>Git Repository</h2>
There are three main folders in our github repository:<br>
* Fiscal Data
 * Contains the raw files of fiscal data tables
* State Assessment Data
 * Contains the raw files of math and reading Consolidated State Performance Report data
* Code 
 * Data cleaning contains the python code we used to clean and merge our two datasets, raw data files, intermediate data files, and the final dataset, *merged_summary.csv*. 
 * Django contains all the code required to launch our dynamic website.  
 * Maps contains the python code used to plot the map in our site. 
