class ClassSchedule:
   def __init__(self, course):
       self.course = course
 
   def __del__(self):
       print('You successfully deleted your schedule')

schedule = ClassSchedule('Chemistry')
# deletes the object
del schedule
