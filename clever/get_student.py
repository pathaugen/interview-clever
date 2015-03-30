

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_student.py
description:  Fetching a specific student via JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


from datetime import datetime, date

from clever.get_json_dict import get_json_dict


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_student( student_id ):
    student = ''
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    json_dict = get_json_dict('/v1.1/students/'+student_id)
    # Pull student data (using student ID) as JSON from Clever API
    '''
        {
            u'links':[
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d',
                    u'rel': u'self'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/district',
                    u'rel': u'district'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/sections',
                    u'rel': u'sections'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/school',
                    u'rel': u'school'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/teachers',
                    u'rel': u'teachers'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/contacts',
                    u'rel': u'contacts'
                },
                {
                    u'uri': u'/v1.1/students/530e5960049e75a9262cff2d/events',
                    u'rel': u'events'
                }
            ],
            u'data':{
                u'district': u'4fd43cc56d11340000000005',
                u'iep_status': u'',
                u'ell_status': u'N',
                u'gender': u'F',
                u'dob': u'9/30/2003',
                u'race': u'Asian',
                u'id': u'530e5960049e75a9262cff2d',
                u'email': u'mary_r@example.net',
                u'location':{
                    u'zip': u'10038'
                },
                u'school': u'530e595026403103360ff9fe',
                u'frl_status': u'Paid',
                u'last_modified': u'2014-06-04T14:10:40.728Z',
                u'hispanic_ethnicity': u'N',
                u'credentials':{
                    u'district_username': u'maryr27',
                    u'district_password': u'ohVie2aeD'
                },
                u'sis_id': u'115088927',
                u'student_number': u'115088927',
                u'name':{
                    u'last': u'Ryan',
                    u'first': u'Mary',
                    u'middle': u'L'
                },
                u'created': u'2014-02-26T21:15:12.454Z',
                u'grade': u'4',
                u'state_id': u'155063237'
            }
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    #student += str(json_dict)
    
    
    student += '''
        <div id="popup-picture">
            <img src="/resources/images/{IMAGE}.png" />
        </div>
        <div id="popup-student">
            <h1>{LASTNAME}, {FIRSTNAME} {MIDDLENAME}</h1>
            <div class="popup-student-info">
                <h3>ID:</h3>
                {ID}
            </div>
            <div class="popup-student-info">
                <h3>Student #:</h3>
                {STUDENTNUMBER}
            </div>
            <div class="popup-student-info">
                <h3>Date of Birth:</h3>
                {BORN} (Age: {AGE})
            </div>
            <div class="popup-student-info">
                <h3>Gender:</h3>
                {GENDER}
            </div>
            <div class="popup-student-info">
                <h3>Race:</h3>
                {RACE}
            </div>
            <div class="popup-student-info">
                <h3>Grade:</h3>
                {GRADE}
            </div>
            <div class="popup-student-info">
                <h3>Email:</h3>
                <a href="mailto:{EMAIL}">{EMAIL}</a>
            </div>
            <div class="popup-student-info">
                <h3>ZIP:</h3>
                {ZIP}
            </div>
            <div class="popup-student-info">
                <h3>Username:</h3>
                {USERNAME}
            </div>
            <div class="popup-student-info">
                <h3>Password:</h3>
                {PASSWORD}
            </div>
        </div>
    '''
    
    
    # Selecting what image to use via gender
    if json_dict['data']['gender'] == 'M':      image = 'student-boy'
    elif json_dict['data']['gender'] == 'F':    image = 'student-girl'
    else:                                       image = 'user-icon'
    
    
    # Conversion of DOB to age
    student_born = datetime.strptime( json_dict['data']['dob'], '%m/%d/%Y' ) # 2/11/2007
    today = date.today()
    student_age = str( today.year - student_born.year - ((today.month, today.day) < (student_born.month, student_born.day)) )
    
    
    student = student.replace( '{IMAGE}',           image )
    student = student.replace( '{LASTNAME}',        json_dict['data']['name']['last'] )
    student = student.replace( '{FIRSTNAME}',       json_dict['data']['name']['first'] )
    student = student.replace( '{MIDDLENAME}',      json_dict['data']['name']['middle'] )
    student = student.replace( '{ID}',              json_dict['data']['id'] )
    student = student.replace( '{STUDENTNUMBER}',   json_dict['data']['student_number'] )
    student = student.replace( '{BORN}',            json_dict['data']['dob'] )
    student = student.replace( '{AGE}',             student_age )
    student = student.replace( '{GENDER}',          json_dict['data']['gender'] )
    student = student.replace( '{RACE}',            json_dict['data']['race'] )
    student = student.replace( '{GRADE}',           json_dict['data']['grade'] )
    student = student.replace( '{EMAIL}',           json_dict['data']['email'] )
    student = student.replace( '{ZIP}',             json_dict['data']['location']['zip'] )
    student = student.replace( '{USERNAME}',        json_dict['data']['credentials']['district_username'] )
    student = student.replace( '{PASSWORD}',        json_dict['data']['credentials']['district_password'] )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return student
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

