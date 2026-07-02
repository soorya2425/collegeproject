from django.shortcuts import render, redirect

def teacher_list(request, message):
    teacher_names = ['John', 'David', 'Priya']

    return render(request, 'teachers/list.html', {
        'teachers': teacher_names,
        'message': message
    })


def teacher_form(request):
    if request.method == 'POST':
        return redirect('teachers:list', 'Welcome Teachers')

    return render(request, 'teachers/form.html')