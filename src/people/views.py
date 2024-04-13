from django.shortcuts import render
from .models import People
# Create your views here.
def people_list(request):
    posts = People.objects.all()
    print('people : ', posts)
    return render(request, 'people/NIIPeople.html', {'people':posts})

def doctor_list(request):
    posts = People.objects.filter(doctor=True)
    return render(request, 'people/doctors.html', {'doctors':posts})

def teacher_list(request):
    posts = People.objects.filter(teacher=True)
    return render(request, 'people/teachers.html', {'teachers':posts})

def people_detail(request, pid):
    post = People.objects.get(id = pid)
    return render(request, 'people/people_detail.html', {'person':post})

# def people_new(request):
#     if request.method != 'POST':
#         form = PostForm()
#     else:
#         form = PostForm(request.POST)
#         att = request.FILES.getlist('images')
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             for image in att:
#                 PostAttachment.objects.create(
#                     file = image,
#                     post_id = post.pk
#                 )
#             return redirect('new_detail', pid=post.pk)
#     return render(request, 'posts/post_new.html', {'form':form})


