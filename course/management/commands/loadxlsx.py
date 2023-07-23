from django.core.management.base import BaseCommand
from openpyxl import load_workbook

#64114540443 ธีรวัฒน์ ทองเรียม

from course.models import Course,Student,Lecturer

class Command(BaseCommand):
    help = "load website data from mysite-data.xlsx."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        wb = load_workbook('mysite-data.xlsx')

        ws = wb['Course']
        for row in ws.values:
            r = [ v for v in row]
            if r[0] == 'id' or r[0] == None:
                continue
            course = {
                'id'         : int(r[0]),
                'title'      : r[1],
                'description': r[2]
            }
            c = Course(**course) 
            c.save()

        wsl = wb['Lecturer']
        for row1 in wsl.values:
            l = [ y for y in row1]
            if l[0] == 'id' or l[0] == None:
                 continue
            lecturer = {
                'id': int(l[0]),
                'first_name'         : l[1],
                'last_name'      : l[2],
                'email': l[3],
                'department': l[4],
                'faculty': l[5]
            } 
            lr = Lecturer(**lecturer) 
            lr.save()

        wss = wb['Student']
        for row2 in wss.values:
            s = [ u for u in row2]
            if s[0] == 'id' or s[0] == None:
                 continue
            student = {
                'id':int(s[0]),
                'first_name'         : s[1],
                'last_name'      : s[2],
                'email': s[3]
            }
            st = Student(**student) 
            st.save()


