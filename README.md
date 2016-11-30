# Final Project (Yu Quan Poh and Cheng Yee Lim)
In your README you should be very explicit about the datasources.  This is where we take citation seriously.
You should NOT, however, include a copy of that data in your repository if it exceeds a few megabytes.  Instead, you should describe how the data was cleaned and reduced.  The cleaning scripts are a fundamental part of your projects; they should be included in the repository and itemized in your README
You SHOULD include the fully processed data as a CSV or other, so that I can see what you're working with.


Scope (20%): how many of the extensions did the group complete? How much does the application do?
Correctness (25%): is the baseline functionality fully delivered, bug-free?
Style (25%): are the front-end and code both manageable?
Performance (15%): is the site 'snappy?'
Documentation (15%): is the class presentation engaging and interesting? Does the README actually make it possible to understand how to find your data and run your site?

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

The cleaning code can be found <a href = "https://github.com/pohyuquan/Project-Harris-YQ-CY-/blob/master/Data-Set%20Cleaninig/final_cleaning_merge.ipynb">here</a>.

The final merged data set can be accessed <a href = "https://github.com/pohyuquan/Project-Harris-YQ-CY-/blob/master/Data-Set%20Cleaninig/merge_summary.csv">here</a>.
