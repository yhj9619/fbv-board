from django.shortcuts import render, redirect, reverse
from .models import Board
from user.models import User


# Create your views here.

def list(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list' : board_list
    }
    return render(request, 'board/list.html', context)

def index(request):
    return render(request, 'board/index.html')

def read(request, id):
    print("request.user.username")
    print(request.user.username)
    
    print()
    board = Board.objects.get(pk=id)
    print("board")
    print(board.writer)
    board.increamentReadCount()
    return render(request, 'board/read.html', {'board':board})

def regist(request, id):
    if id == 0: #신규작성
        if request.method == 'POST':
            writer = request.user 
            title = request.POST['title']
            content = request.POST['content']
            Board(title=title, writer=writer, content=content).save()
            return redirect(reverse('board:list'))
        else:
            return render(request, 'board/regist.html')
    else: #기존 게시글 작성
        board = Board.objects.get(pk=id)
        if request.method == 'POST':
            board.title = request.POST['title']
            board.content = request.POST['content']
            board.save()
            return redirect(reverse('board:read', args=(id,)))
        else:
            return render(request, 'board/edit.html', {'board':board})

    
def remove(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.delete()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/remove.html', {'board':board})