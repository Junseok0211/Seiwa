from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from datetime import datetime
# Create your views here.

def index(request):
    post_list = Post.objects
    today = datetime.now()
    word = {"1": "치료나 약은 효과가 있다고 믿는 것으로 보다 효과가 높아지는 것입니다.",
            "2":"가짜 아첨보다 마음으로부터 칭찬하는 것이 마음을 움직입니다",
            "3":"누군가가 준비하고 선택하는 것이 아니라 스스로 선택하고 개척하는 것이 중요합니다.",
            "4": "저녁시간은 자신을 자책하는 것이 아니라 신선한 마음으로 맞이하는 준비시간이다.",
            "5":"모두 다른 개성을 갖고 있기 때문에 할 수 있는 일이 다릅니다.",
            "6": "심심해서 소중한 시간이에요.",
            "7":"자신의 인식하는 법, 바라보는 방법은 상대에게 좋게도 나쁘게도 영향을 주는 것입니다.",
            "8": "남자는 말이 적고 여자는 말이 많아서 오해받는다.",
            "9":"자신의 경험은 누군가에게 도움이 되고 기쁨을 주는 것입니다..",
            "10": "호기심과 모험심은 몇 살이 되어도 계속 갖고 싶다.",
            "11":"잘 되지 않는다고 느끼는 것은, 누군가에게 혹은 물건에 의존하고 있기 때문일지도 모릅니다.",
            "12": "목표나 과제는 중요한 사람에게 상담하고 결정하면 좋다.",
            "13":"즐거운 일을 기다리는 것보다 뭐든지 즐길 수 있는 자신이 되는 것이 삶이 충실해진다.",
            "14": "분노는 책임감을 갖고 싶어서 생기는 것입니다.",
            "15":"감사의 말은 마음이 맑아지고 평온해집니다.",
            "16": "배움의 좋은 점은 실천하는 것으로 환경에 나타난다.",
            "17":"생각해 보고 구체적으로 계획하는 것으로 전진해 가는 것입니다.",
            "18": "만나는 사람도 물건도 환경도 우연은 아닙니다.",
            "19":"사랑과 감사는 모든 것에 최고의 파동을 주는 말입니다.",
            "20": "사랑의 저금을 해서 행운을 부르자!",
            "21":"항상 낮은 자세를 유의하는 것이 중요합니다.",
            "22": "남자와 여자의 생각은 전혀 다릅니다.",
            "23":"인정하는 것도,좋아하는 것도 노력이 필요합니다.",
            "24": "'좋다고 생각해'의 행동은, 누군가를 위해서라고 생각해서 할까 말까하는 것과는 천지의 차이가 있다.",
            "25":"재주가 있는 사람이라도 평가하고 응원해주는 사람이 있어야 가치가 나타난다.",
            "26": "자신이 상대방의 상식에 사로잡히지 않으면 편안해진다.",
            "27":"과거도 현재도 미래도 모두 이어지고 있다. 당신의 마음을 정하고 있는 것입니다.",
            "28": "누군가를 위해서 힘낼 수 있는 상대가 있다는 것이 행복합니다",
            "29":"물건을 놓을 정위치를 여기서 결정하면 정돈된다.",
            "30": "상대의 좋은 점을 인정하고 받아들이려고 하면 나도 좋아진다.",
            "31":"사람은 마음의 정을 찾아서 모여든다."}

    today_word = word[str(today.day)]
    return render(request, 'index.html', {'post_list': post_list, 'word':today_word})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.user = request.user
    post.save()

    return redirect('/')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'post' : post_detail})

def updateForm(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if(request.user != post.user):
        return redirect('/')
    return render(request, 'updateForm.html', {'post':post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.save()
    return redirect('/')
    
# 글 삭제하기 기능
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if (request.user != post.user):
        return redirect('/')
    post.delete()
    return redirect('/')
    
