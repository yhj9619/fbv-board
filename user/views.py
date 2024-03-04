from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from board.models import Board
from .models import User
from .forms import UserForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request,user)
            board_list = Board.objects.all().order_by('-id')
            context = {
                'board_list' : board_list
            }
            return render(request, "board/list.html", context)
        else:
            print("인증실패")
            return render(request, "user/login.html")
    else:
        return render(request, "user/login.html")
    

def logout_view(request):
    logout(request)
    return redirect("board:list")

# def signup_view(request):
#     if request.method == "POST":
#         print("request.method")
#         print(request.method)
#         print("request.POST")
#         print(request.POST)
#         form = UserForm(request.POST)
#         print("form")
#         print(form)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)  # 사용자 인증
#             login(request, user)  # 로그인

#             if user is not None:
#                 print("인증 성공")
#                 login(request,user)
#                 board_list = Board.objects.all().order_by('-id')
#                 context = {
#                     'board_list' : board_list
#                 }
#                 return render(request, "board/list.html", context)
#             else:
#                 print("인증실패")
#                 return render(request, "user/login.html")
#     else:
#         form = UserForm()
#         return render(request, 'user/signup.html', {'form': form})
    

def signup_view(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            login(request, user)
            board_list = Board.objects.all().order_by('-id')
            context = {
                    'board_list' : board_list
            }
            return render(request, "board/list.html", context)
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')