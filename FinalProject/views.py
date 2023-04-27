from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import csv

def log_in(request): 
    try:
        if request.method == 'POST':
            Id = request.POST.get('id')
            Pass = request.POST.get('pass')
            print(Id)
            print(Pass)
            with connection.cursor() as cursor:
                    cursor.execute('SELECT Password,User_type FROM dataapp_all_user WHERE ID = %s',[Id])
                    rows = cursor.fetchall()
                    if len(rows) != 0:
                        print(rows[0][0])
                        if rows[0][0]==Pass:
                            if rows[0][1] == "FACULTY":
                                return redirect("fact")
                            else:
                                data={
                                    'ID':Id
                                    }
                                return render(request, "student.html", {'data': data})
                        else:
                          return HttpResponse("password is incorrect!!")
                    else:
                        return HttpResponse("This userid doesnot exist")
                 
    except:
        pass
    return render(request,"login.html")

    



def faculty_page(request):
    if request.method == 'POST':
        if 'btn_1' in request.POST:
            id = int(request.POST.get('S_ID'))
            Year = int(request.POST.get('E_Year'))
            course = request.POST.get('E_Course')
            section = int(request.POST.get('E_Section'))
            grade = request.POST.get('Grade')
            selected_semester = request.POST.get('Spring') or request.POST.get('Summer') or request.POST.get('Autumn')
            print(selected_semester)
            
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT sectionID FROM dataapp_section WHERE year=%s AND courseID=%s AND sectionNum=%s AND semester=%s', (Year, course, section, selected_semester))
                rows = cursor.fetchall()
                cursor.execute('INSERT INTO dataapp_co_t (sectionID_id, studentID_id, grade) VALUES ( %s, %s, %s)', (rows[0][0],id,grade))
                connection.commit()
            return HttpResponse("Data successfully uploaded")
        elif 'btn_2' in request.POST:
            csv_f = request.FILES['csv_file']
            decoded_file = csv_f.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            with connection.cursor() as cursor:
                for row in reader:
                    cursor.execute('SELECT sectionID FROM dataapp_section WHERE year=%s  AND semester=%s AND courseID=%s AND sectionNum=%s', (row['EducationalYear'], row['EducationalSemester'], row['EnrolledCourse'], row['EnrolledSection']))
                    r = cursor.fetchall()
                    
                    
                    cursor.execute('INSERT INTO dataapp_co_t (sectionID_id, studentID_id,grade) VALUES (%s, %s, %s)', (r[0][0], row['StudentID'], row['ObtainedGrade']))
                    connection.commit()
            return HttpResponse("File successfully uploaded")

    return render(request,"faculty.html")

def student_page(request):
    return render(request,"student.html")

def display_student_page(request):
    if request.method == 'POST':
        if 'Btn1' in request.POST:
            ID = request.POST.get('S_id')
            print(ID)
            with connection.cursor() as cursor:
                cursor.execute('SELECT studentID_id,year,semester,courseID,sectionNum,grade FROM dataapp_co_t AS C INNER JOIN dataapp_section AS S ON C.sectionID_id = S.sectionID WHERE studentID_id=%s',(ID,) )
                rows = cursor.fetchall()
              
                data={
                    'rows':rows
                }
                return render(request,"Display_S.html",data)
        elif 'Btn2' in request.POST:
            Year = int(request.POST.get('E_Year'))
            course = request.POST.get('E_Course')
            section = int(request.POST.get('E_Section'))
            selected_semester = request.POST.get('Spring') or request.POST.get('Summer') or request.POST.get('Autumn')
            with connection.cursor() as cursor:
                cursor.execute('SELECT sectionID FROM dataapp_section WHERE year=%s AND courseID=%s AND sectionNum=%s AND semester=%s', (Year, course, section, selected_semester))
                rows = cursor.fetchall()
                print(rows)
                cursor.execute('SELECT studentID_id,year,semester,courseID,sectionNum,grade FROM dataapp_co_t AS C INNER JOIN dataapp_section AS S ON C.sectionID_id = S.sectionID WHERE sectionID_id=%s',(rows[0][0],) )
                r = cursor.fetchall()
                data = {
                    'rows':r
                }
                return render(request,"Display_S.html",data)


    return render(request,"Display_S.html")
    
def faculty1st(request):
    return render(request,"faculty_1st.html")