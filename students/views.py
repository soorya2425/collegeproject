from django.shortcuts import render, redirect

def student_list(request, message):
    student_names = ['Arun', 'Rahul', 'Meena']

    return render(request, 'students/list.html', {
        'students': student_names,
        'message': message
    })


def student_form(request):
    if request.method == 'POST':
        return redirect('students:list', 'Welcome Students')

    return render(request, 'students/form.html')