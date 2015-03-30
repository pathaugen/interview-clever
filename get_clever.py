

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_clever.py
description:  Accessing Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import time     # used for delaying code a few seconds for development reasons

from random import randint

#from clever.get_json_dict  import get_json_dict
from clever.get_districts   import get_districts


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_clever():
    clever = ''
    
    
    clever += '<h1>Patrick Haugen Framework Accessing Clever API</h1>'
    
    
    # Adding time before content load to show the loading process
    random_sleep = randint(0,3)
    time.sleep(random_sleep)
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # STEP 1: DISPLAY ALL DISTRICTS (top level)
    # Pull default district data as JSON from Clever API
    # https://clever.com/developers/docs
    clever += '<h1>Districts</h1>'
    clever += get_districts()
    #clever += str( get_json('/v1.1/districts') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # STEP 2: Clicking a district pulls the links you can click
    # clever/get_district(district_id)
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # STEP 3a: Show the schools under a district
    # clever/get_district_link -> clever/get_district_schools
    
    # STEP 3b: Show the teachers under a district
    # clever/get_district_link -> clever/get_district_teachers
    
    # STEP 3c: Show the students under a district
    # clever/get_district_link -> clever/get_district_students
    
    # STEP 3d: Show the sections under a district
    # clever/get_district_link -> clever/get_district_sections
    
    # STEP 3e: Show the events under a district
    # clever/get_district_link -> clever/get_district_events
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # STEP 3a: PART 2: Show the selected school
    # clever/get_school
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Pull default school data as JSON from Clever via API
    #data = get_json('/v1.1/schools')
    '''
        {
            "data":[
                {
                    "data":{
                        "created":          "2014-02-26T21:14:56.662Z",
                        "district":         "4fd43cc56d11340000000005",
                        "low_grade":        "9",                                            -> {LOW_GRADE}
                        "principal":{
                            "name":         "Theodora Khan",                                -> {PRINCIPAL_NAME}
                            "email":        "tdkhan@mailinator.com"                         -> {PRINCIPAL_EMAIL}
                        },
                        "school_number":    "02M800",
                        "sis_id":           "02M800",
                        "phone":            "(212) 555-1212",                               -> {PHONE}
                        "state_id":         "712345",
                        "high_grade":       "12",                                           -> {HIGH_GRADE}
                        "location":{
                            "address":      "350 5th Avenue",                               -> {ADDRESS}
                            "city":         "New York",                                     -> {CITY}
                            "state":        "NY",                                           -> {STATE}
                            "zip":          "10001"                                         -> {ZIP}
                        },
                        "last_modified":    "2014-02-26T21:14:56.665Z",
                        "name":             "Clever High School",                           -> {NAME}
                        "nces_id":          "360008000000",
                        "id":               "530e595026403103360ff9fd"                      -> This is the ID used for URI and the links
                    },
                    "uri":                  "/v1.1/schools/530e595026403103360ff9fd"        -> URI to pull more information
                },
                {
                    "data":{
                        "high_grade":       "5",
                        "last_modified":    "2014-02-26T21:14:56.670Z",
                        "low_grade":        "Kindergarten",
                        "name":             "Clever Elementary School",
                        "principal":{
                            "name":         "Cecilia Roderick",
                            "email":        "ceciliar@mailinator.com"
                        },
                        "district":         "4fd43cc56d11340000000005",
                        "phone":            "(718) 555-4567",
                        "sis_id":           "13K123",
                        "state_id":         "30890",
                        "created":          "2014-02-26T21:14:56.668Z",
                        "location":{
                            "address":      "110 Pineapple Street",
                            "city":         "Brooklyn",
                            "state":        "NY",
                            "zip":          "11201"
                        },
                        "nces_id":          "360007000000",
                        "school_number":    "13K123",
                        "id":               "530e595026403103360ff9fe"
                    },
                    "uri":                  "/v1.1/schools/530e595026403103360ff9fe"
                },
                {
                    "data":{
                        "district":         "4fd43cc56d11340000000005",
                        "low_grade":        "6",
                        "name":             "Clever Middle School",
                        "phone":            "(718) 555-8989",
                        "created":          "2014-02-26T21:14:56.671Z",
                        "high_grade":       "8",
                        "last_modified":    "2014-02-26T21:14:56.673Z",
                        "state_id":         "412",
                        "location":{
                            "address":      "322 Old Beach 88th Street",
                            "city":         "Rockaway Beach",
                            "state":        "NY",
                            "zip":          "11693"
                        },
                        "nces_id":          "360001000000",
                        "principal":{
                            "name":         "Leonard Springsteen",
                            "email":        "lspringsteen@mailinator.com"
                        },
                        "school_number":    "27Q321",
                        "sis_id":           "27Q321",
                        "id":               "530e595026403103360ff9ff"
                    },
                    "uri":                  "/v1.1/schools/530e595026403103360ff9ff"
                }
            ],
            "paging":{
                "current":    1,
                "total":      1,
                "count":      3
            },
            "links":[{
                "rel":    "self",
                "uri":    "/v1.1/schools"
            }]
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Working with JSON from Clever
    '''
    for school in data['data']:
        clever += ''
            <div class="school" style="background-color:lightblue;padding:2%;">
                <h3>{NAME}</h3>
                <div>
                    Grades: {LOW_GRADE} - {HIGH_GRADE}
                </div>
                <div>
                    Phone: {PHONE}
                </div>
            </div>
        ''
        clever = clever.replace( '{NAME}',          school['data']['name'] )
        clever = clever.replace( '{LOW_GRADE}',     school['data']['low_grade'] )
        clever = clever.replace( '{HIGH_GRADE}',    school['data']['high_grade'] )
        clever = clever.replace( '{PHONE}',         school['data']['phone'] )
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Pull district data (using school ID) as JSON from Clever API
    #clever += str( get_json('/v1.1/schools/530e595026403103360ff9fd/district') )
    '''
        {
            u'links':[
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005',
                    u'rel':    u'self'
                }
            ],
            u'data':{
                u'id':         u'4fd43cc56d11340000000005',
                u'name':       u'Demo District'
            }
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return clever
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

