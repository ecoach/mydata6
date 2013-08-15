from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

_AP_BIO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_AP_CHE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_FS_LEASTVALUABLE_CHOICES = (
    ('NewValue1', 'Advice From students'),
    ('NewValue2', 'Advice From professors'),
    ('NewValue3', 'General study tips'),
    ('NewValue4', 'Problem roulette'),
    ('NewValue5', 'Video content'),
    ('NewValue6', 'Grade prediction tool'),
    ('NewValue7', 'Grade calculator tool'),
    ('NewValue8', 'Class calendar'),
)

_DECLARED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_SEMESTERS_COMPLETED_CHOICES = (
    ('9', 'More than 8 semesters'),
)

_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

_FS_USAGE_CHOICES = (
    ('daily', 'Daily'),
    ('coupledays', 'Every couple of days'),
    ('onceweek', 'Once a week'),
    ('everyfewweeks', 'Once every few weeks'),
    ('postexams', 'Mostly after exams'),
)

_CONCENTRATE_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Physics', 'Physics/Astrophysics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Biology_MCDB', 'Biology MCDB'),
    ('Biology_EEB', 'Biology EEB'),
    ('Health', 'Health-related Field (Physical Therapy, Pharmacology, Nursing, etc.)'),
    ('Humanities', 'Humanities'),
    ('Math', 'Mathematics'),
    ('Neurosci', 'Neuroscience'),
    ('Social_Science_not_Psych', 'Social Science (excluding Psychology)'),
    ('Psych_BBCS', 'Psychology or BBCS'),
    ('Education', 'Education'),
    ('IDK', 'I do not know'),
    ('Other', 'Other'),
)

_ATTENDANCE_ANTICIPATED_CHOICES = (
    ('Never', 'Never'),
    ('1to5', 'Between 1 and 5 times'),
    ('5to10', 'Between 5 and 10 times'),
    ('morethan10', 'Greater than 10 times'),
)

_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certification program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

_SUBJECT_INTEREST_CHOICES = (
    ('0', '0<br>Not at all interested'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10<br>Extremely interested'),
)

_CUM_GPA_SURVEY_CHOICES = (
    ('2_0', '2.0 or lower'),
    ('2_1', '2.1'),
    ('2_2', '2.2'),
    ('2_3', '2.3'),
    ('2_4', '2.4'),
    ('2_5', '2.5'),
    ('2_6', '2.6'),
    ('2_7', '2.7'),
    ('2_8', '2.8'),
    ('2_9', '2.9'),
    ('3_0', '3.0'),
    ('3_1', '3.1'),
    ('3_2', '3.2'),
    ('3_3', '3.3'),
    ('3_4', '3.4'),
    ('3_5', '3.5'),
    ('3_6', '3.6'),
    ('3_7', '3.7'),
    ('3_8', '3.8'),
    ('3_9', '3.9'),
    ('4_0', '4.0'),
)

_EMPLOYMENT_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)

_CONFIDENCE_CHOICES = (
    ('0', '0<br>Not confident at all'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10<br>Extremely confident'),
)

_REASON_CHOICES = (
    ('Possible_Concentrate_req', 'I am considering this subject as my concentration'),
    ('Concentration_req', 'This is a course required by my concentration'),
    ('Grad_req', 'I need this class to prepare for my graduate/professional program'),
    ('Credit', 'For a specific credit (NS, QR, etc.)'),
    ('Interest', "I'm taking this class because of my interest in the subject"),
)

_FS_MOSTVALUABLE_CHOICES = (
    ('1', 'Advice from students'),
    ('2', 'Advice from professors'),
    ('3', 'General study tips'),
    ('4', 'Problem Roulette'),
    ('5', 'Video content'),
    ('6', 'Grade prediction tool'),
    ('7', 'Grade calculator tool'),
    ('8', 'Class calendar'),
)

_GOAL_GRADE_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C-'),
)

_PRED_MOSTPROB_INITIAL_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C-'),
)

GRADE_DIST_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C-'),
)

_INVOLVED_IN_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

_HIGH_SCHOOL_CUMGPA__CHOICES = (
    ('2_0', 'Less than 2.0'),
    ('2_1', '2.1'),
    ('2_2', '2.2'),
    ('2_3', '2.3'),
    ('2_4', '2.4'),
    ('2_5', '2.5'),
    ('2_6', '2.6'),
    ('2_7', '2.7'),
    ('2_8', '2.8'),
    ('2_9', '2.9'),
    ('3_0', '3.0'),
    ('3_1', '3.1'),
    ('3_2', '3.2'),
    ('3_3', '3.3'),
    ('3_4', '3.4'),
    ('3_5', '3.5'),
    ('3_6', '3.6'),
    ('3_7', '3.7'),
    ('3_8', '3.8'),
    ('3_9', '3.9'),
    ('4_0', '4.0'),
)

_SLC_ENROLLED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_CLASS_STANDING_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
)

_BIRTHMO_CHOICES = (
    ('-1', 'Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)


class EmptySource(SubjectData):
    pass

class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_source1'
    SLC_Enrolled = models.CharField(max_length=3, choices=_SLC_ENROLLED_CHOICES, null=True, blank=True)
    AP_Bio = models.CharField(max_length=3, choices=_AP_BIO_CHOICES, null=True, blank=True)
    AP_Chem = models.CharField(max_length=3, choices=_AP_CHE_CHOICES, null=True, blank=True)
    Confidence = models.CharField(max_length=2, choices=_CONFIDENCE_CHOICES, null=True, blank=True)
    Goal_Grade = models.CharField(max_length=1, choices=_GOAL_GRADE_CHOICES, null=True, blank=True)
    Subject_Interest = models.CharField(max_length=2, choices=_SUBJECT_INTEREST_CHOICES, null=True, blank=True)
    Attendance_Anticipated = models.CharField(max_length=10, choices=_ATTENDANCE_ANTICIPATED_CHOICES, null=True, blank=True)
    FS_MostValuable__1 = models.NullBooleanField()
    FS_MostValuable__2 = models.NullBooleanField()
    FS_MostValuable__3 = models.NullBooleanField()
    FS_MostValuable__4 = models.NullBooleanField()
    FS_MostValuable__5 = models.NullBooleanField()
    FS_MostValuable__6 = models.NullBooleanField()
    FS_MostValuable__7 = models.NullBooleanField()
    FS_MostValuable__8 = models.NullBooleanField()
    FS_LeastValuable__NewValue1 = models.NullBooleanField()
    FS_LeastValuable__NewValue2 = models.NullBooleanField()
    FS_LeastValuable__NewValue3 = models.NullBooleanField()
    FS_LeastValuable__NewValue4 = models.NullBooleanField()
    FS_LeastValuable__NewValue5 = models.NullBooleanField()
    FS_LeastValuable__NewValue6 = models.NullBooleanField()
    FS_LeastValuable__NewValue7 = models.NullBooleanField()
    FS_LeastValuable__NewValue8 = models.NullBooleanField()
    FS_Changes = models.TextField(null=True, blank=True)
    FS_Usage = models.CharField(max_length=13, choices=_FS_USAGE_CHOICES, null=True, blank=True)
    FS_Challenges = models.TextField(null=True, blank=True)
    Exam1_FR = models.FloatField(null=True, blank=True)
    Exam1_MC = models.FloatField(null=True, blank=True)
    Exam1_Score = models.FloatField(null=True, blank=True)
    Exam1_ClassAvg = models.FloatField(null=True, blank=True)
    Exam2_FR = models.FloatField(null=True, blank=True)
    Exam2_MC = models.FloatField(null=True, blank=True)
    Exam2_Score = models.FloatField(null=True, blank=True)
    Exam2_ClassAvg = models.FloatField(null=True, blank=True)
    Exam3_FR = models.FloatField(null=True, blank=True)
    Exam3_MC = models.FloatField(null=True, blank=True)
    Exam3_Score = models.FloatField(null=True, blank=True)
    Exam3_ClassAvg = models.FloatField(null=True, blank=True)
    Exam4_FR = models.FloatField(null=True, blank=True)
    Exam4_MC = models.FloatField(null=True, blank=True)
    Exam4_Score = models.FloatField(null=True, blank=True)
    Exam4_ClassAvg = models.FloatField(null=True, blank=True)
    Project1_Grade = models.FloatField(null=True, blank=True)
    Project2_Grade = models.FloatField(null=True, blank=True)
    Project3_Grade = models.FloatField(null=True, blank=True)
    iClicker_Grade = models.FloatField(null=True, blank=True)
    CellMap_Grade = models.FloatField(null=True, blank=True)
    Num_PR_Questions = models.IntegerField(null=True, blank=True)
    Grade_PR_Questions = models.FloatField(null=True, blank=True)
    MCDB310FinalGradeLetter = models.FloatField(null=True, blank=True)
    MCDB310FinalGradeNumber = models.FloatField(null=True, blank=True)
    dist_id = models.CharField(max_length=50, null=True, blank=True)
    Pred_MostProb_Initial = models.IntegerField(null=True, blank=True)
    Pred_MostProb_PostExam1 = models.IntegerField(null=True, blank=True)
    Pred_MostProb_PostExam2 = models.IntegerField(null=True, blank=True)
    Pred_MostProb_PostExam3 = models.IntegerField(null=True, blank=True)
    Pred_Dist_Intial = models.CharField(max_length=100, null=True, blank=True)
    Pred_Dist_PostExam1 = models.CharField(max_length=100, null=True, blank=True)
    Pred_Dist_PostExam2 = models.CharField(max_length=100, null=True, blank=True)
    Pred_Dist_PostExam3 = models.CharField(max_length=100, null=True, blank=True)
    Reason__Possible_Concentrate_req = models.NullBooleanField()
    Reason__Concentration_req = models.NullBooleanField()
    Reason__Grad_req = models.NullBooleanField()
    Reason__Credit = models.NullBooleanField()
    Reason__Interest = models.NullBooleanField()

class commonsurvey(SubjectData):
    pass

class Common1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_common1'
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    uniqname = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=_GENDER_CHOICES, null=True, blank=True)
    BirthDay = models.IntegerField(null=True, blank=True)
    BirthMo = models.IntegerField(null=True, blank=True)
    BirthYr = models.IntegerField(null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    College = models.CharField(max_length=11, choices=_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=30, null=True, blank=True)
    Concentrate__Engineering = models.NullBooleanField()
    Concentrate__Physics = models.NullBooleanField()
    Concentrate__Chemistry = models.NullBooleanField()
    Concentrate__Biology = models.NullBooleanField()
    Concentrate__Biology_MCDB = models.NullBooleanField()
    Concentrate__Biology_EEB = models.NullBooleanField()
    Concentrate__Health = models.NullBooleanField()
    Concentrate__Humanities = models.NullBooleanField()
    Concentrate__Math = models.NullBooleanField()
    Concentrate__Neurosci = models.NullBooleanField()
    Concentrate__Social_Science_not_Psych = models.NullBooleanField()
    Concentrate__Psych_BBCS = models.NullBooleanField()
    Concentrate__Education = models.NullBooleanField()
    Concentrate__IDK = models.NullBooleanField()
    Concentrate__Other = models.NullBooleanField()
    Concentrate_Other = models.TextField(null=True, blank=True)
    Declared = models.CharField(max_length=3, choices=_DECLARED_CHOICES, null=True, blank=True)
    Class_Standing = models.CharField(max_length=9, choices=_CLASS_STANDING_CHOICES, null=True, blank=True)
    Cum_GPA_Survey = models.CharField(max_length=3, choices=_CUM_GPA_SURVEY_CHOICES, null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=_EMPLOYMENT_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.TextField(null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=_POST_COLLEGE_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=_PARENT_ED_CHOICES, null=True, blank=True)
    High_School_CumGPA = models.CharField(max_length=3, choices=_HIGH_SCHOOL_CUMGPA__CHOICES, null=True, blank=True)


