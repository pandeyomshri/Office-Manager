from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime
from django.http import HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
        emps = Employee.objects.all()
        context = {
         'emps': emps
             }
        print(context)
        return render(request, 'view_all_emp.html', context)
    
def add_emp(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name'] 
       salary = int(request.POST['salary'] )
       bonus = int(request.POST['bonus']) 
       phone = int(request.POST['phone']) 
       dept = int(request.POST['dept'] )
       role = int(request.POST['role'] )
       new_emp= Employee(first_name= first_name, last_name= last_name, salary= salary, bonus= bonus, phone= phone, dept_id= dept, role_id= role, hire_date= datetime.now())
       new_emp.save()
       return HttpResponse('Employee Added Successfully')

    elif request.method == 'GET': 
        return render(request, 'add_emp.html')

    else:
        return HttpResponse('An Exception has Occured')    


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("Please Enter a valid ID")    
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    return render(request, 'filter_emp.html')
                