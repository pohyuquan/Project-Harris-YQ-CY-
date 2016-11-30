from django.db import models

# Create your models here.

STATES = (
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('California', 'California'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Maryland', 'Maryland'),
    ('Michigan', 'Michigan'),
    ('New Mexico', 'New Mexico'),
    ('Nevada', 'Nevada'),
    ('North Carolina', 'North Carolina'),
    ('Ohio', 'Ohio'),
    ('Pennsylvania', 'Pennsylvania'),
    ('South Carolina', 'South Carolina'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Wisconsin', 'Wisconsin'),
   )

STATES_DICT = dict(STATES)

class Input(models.Model):

    state = models.CharField(max_length=50, choices=STATES)
    address = models.CharField(max_length=50)

SCHOOL_DISTRICTS = (
    ('Albuquerque Public Schools', 'Albuquerque Public Schools (New Mexico)'),
    ('Aldine Independent School District', 'Aldine Independent School District (Texas)'),
    ('Alpine School District', 'Alpine School District (Utah)'),
    ('Anchorage School District', 'Anchorage School District (Alaska)'),
    ('Anne Arundel County Public Schools', 'Anne Arundel County Public Schools (Maryland)'),
    ('Arlington Independent School District', 'Arlington Independent School District (Texas)'),
    ('Atlanta Public Schools', 'Atlanta public Schools (Atlanta)'),
    ('Austin Independent School District', 'Austin Independent School District (Texas)'),
    ('Baltimore City Public Schools', 'Baltimore City Public Schools (Maryland)'),
    ('Baltimore County Public Schools', 'Baltimore County Public Schools (Maryland)'),
    ('Brevard County School District', 'Brevard County School District (Florida)'),
    ('Broward County School District', 'Broward County School District (Florida)'),
    ('Brownsville Independent School District', 'Brownsville Independent School District (Texas)'),
    ('Capistrano Unified School District', 'Capistrano Unified School District (California)'),
    ('Charlotte-Mecklenburg Schools', 'Charlotte-Mecklenburg Schools (North Carolina)'),
    ('Clark County School District', 'Clark County School district (Nevada)'),
    ('Clayton County School District', 'Clayton County School District (Georgia)'),
    ('Cobb County School District', 'Cobb County School District (Georgia)'),
    ('Columbus City School District', 'Columbus City School District (Ohio)'),
    ('Conroe Independent School District', 'Conroe Independent School District (Texas)'),
    ('Cumberland County Schools', 'Cumberland County Schools (North Carolina)'),
    ('Cypress-Fairbanks Independent School District', 'Cypress-Fairbanks Independent School District (Texas)'),
    ('Dallas Independent School District', 'Dallas Independent School District (Texas)'),
    ('Dekalb County School District', 'Dekalb County School District (Georgia)'),
    ('Detroit City School District', 'Detroit City School District (Michigan)'),
    ('Duval County School District', 'Duval County School District (Florida)'),
    ('El Paso Independent School District', 'El Paso Independent School District (Texas)'),
    ('Elk Grove Unified School District', 'Elk Grove Unified School District (California)'),
    ('Fort Bend Independent School District', 'Fort Bend Independent School District (Texas)'),
    ('Fort Worth Independent School District', 'Fort Worth Independent School District (Texas)'),
    ('Fresno Unified School District', 'Fresno Unified School District (California)'),
    ('Fulton County School District', 'Fulton County School District (Georgia)'),
    ('Garden Grove Unified School District', 'Garden Grove Unified School District (California)'),
    ('Garland Independent School District', 'Garland Independent School District (Texas)'),
    ('Granite School District', 'Granite School District (Utah)'),
    ('Greenville County School District', 'Greenville County School District (South Carolina)'),
    ('Guilford County Schools', 'Guilford County Schools (North Carolina)'),
    ('Gwinnett County School District', 'Gwinnett County School District (Georgia)'),
    ('Hawaii Department of Education', 'Hawaii Department of Education (Hawaii)'),
    ('Hillsborough County School District', 'Hillsborough County School District (Florida)'),
    ('Houston Independent School District', 'Houston Independent School District (Texas)'),
    ('Howard County Public Schools', 'Howard County Public Schools (Maryland)'),
    ('Jordan School District', 'Jordan School District (Utah)'),
    ('Katy Independent School District', 'Katy Independent School District (Texas)'),
    ('Knox County School District', 'Knox County School District (Tennessee)'),
    ('Lee County School District', 'Lee County School District (Florida)'),
    ('Lewisville Independent School District', 'Lewisville Independent School District (Texas)'),
    ('Long Beach Unified School District', 'Long Beach Unified School District (California)'),
    ('Los Angeles Unified School District', 'Los Angeles Unified School District (California)'),
    ('Mesa Unified School District', 'Mesa Unified School District (Arizona)'),
    ('Milwaukee School District', 'Milwaukee School District (Wisconsin)'),
    ('Montgomery County Public Schools', 'Montgomery County Public Schools (Maryland)'),
    ('North east Independent School District', 'North east Independent School District (Texas)'),
    ('Orange County School District', 'Orange County School District (Florida)'),
    ('Osceola County School District', 'Osceola County School District (Florida)'),
    ('Palm beach County School District', 'Palm beach County School District (Florida)'),
    ('Pasadena Independent School District', 'Pasadena Independent School District (Texas)'),
    ('Philadelphia School District', 'Philadelphia School District (Pennsylvania)'),
    ('Pinellas County School District', 'Pinellas County School District (Florida)'),
    ('Plano Independent School District', 'Plano Independent School District (Texas)'),
    ('Polk County School District', 'Polk County School District (Florida)'),
    ('Prince George\'s County Public Schools', 'Prince George\'s County Public Schools (Maryland)'),
    ('Sacramento City Unified School District', 'Sacramento City Unified School District (California)'),
    ('San Antonio Independent School District', 'San Antonio Independent School District (Texas)'),
    ('San Bernardino City Unified School District', 'San Bernardino City Unified School District (California)'),
    ('San Francisco Unified School District', 'San Francisco Unified School District (California)'),
    ('San Juan Unified School District', 'San Juan Unified School District (California)'),
    ('Santa Ana Unified School District', 'Santa Ana Unified School District (California)'),
    ('Seminole County School District', 'Seminole County School District (Florida)'),
    ('Shelby County School District', 'Shelby County School District (Tennessee)'),
    ('Tucson Unified School District', 'Tucson Unified School District (Arizona)'),
    ('Volusia County School District', 'Volusia County School District (Florida)'),
    ('Wake County Schools', 'Wake County Schools (North Carolina)'),
    ('Washoe County School District', 'Washoe County School District (Nevada)'),
   )

SCHOOL_DISTRICTS_DICT = dict(SCHOOL_DISTRICTS)

class schools(models.Model):

    district = models.CharField(max_length=200, choices=SCHOOL_DISTRICTS)


GRADES = (
    ('All Grades', 'All Grades'),
    ('Grade 3', 'Grade 3'),
    ('Grade 4', 'Grade 4'),
    ('Grade 5', 'Grade 5'),
    ('Grade 6', 'Grade 6'),
    ('Grade 7', 'Grade 7'),
    ('Grade 8', 'Grade 8'),
    ('HS%', 'High School'),
   )

GRADES_DICT = dict(GRADES)

class grade(models.Model):

    gradelevel = models.CharField(max_length=50, choices=GRADES)

SUBGROUP = (
    ('All Students', 'All Students'),
    ('MAM', 'American Indian/Alaska Native'),
    ('MAS', 'Asian/Pacific Islander'),
    ('MHI', 'Hispanic'),
    ('MBL', 'Black'),
    ('MWH', 'White '),
    ('MTR', 'Two or More Races 8'),
    ('CWD', 'Children with Disabilities'),
    ('ECD', 'Economically Disadvantaged '),
    ('LEP', 'Limited English Proficiency'),
    ('F', 'Female'),
    ('M', 'Male'),
    ('HOM', 'Homeless'),
    ('MIG', 'Migrant'),
   )

SUBGROUP_DICT = dict(SUBGROUP)

class sub(models.Model):

    subgroups = models.CharField(max_length=50, choices=SUBGROUP)

SUBJECT = (
    ('Math', 'Math'),
    ('Reading', 'Reading'),
   )

SUBJECT_DICT = dict(SUBJECT)

class subjects(models.Model):

    topic = models.CharField(max_length=50, choices=SUBJECT)
