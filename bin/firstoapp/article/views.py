from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForms
from django.template.context_processors import csrf
from article.function import b_replacer, keys_33, b_replacer_33,eng_capitalize, first_capitalize


# Create your views here.
def main_view(request):
    view = "main_view"
    args = {}
    if request.POST:
        set_keys = request.POST.get('set_keys','')
        what_replace_keys = request.POST.get('what_replace','')
        on_what_replace_keys = request.POST.get('on_what_replace','')
        what_replace_33_keys = request.POST.get('what_replace_33','')
        on_what_replace_33_keys = request.POST.get('on_what_replace_33','')
        what_adds_33_keys = request.POST.get('what_adds_33 what_adds_33_keys','')
        eng_capital = request.POST.get('ino_cap', False)
        spec_del = request.POST.get('spec_del', False)
        first_capital = request.POST.get('first_cap', False)

        if what_replace_keys != '':
            done_keys_keys = b_replacer(set_keys, what_replace_keys, on_what_replace_keys)
        else:
            done_keys_keys = set_keys

        if what_replace_33_keys != '':
            done_keys_keys = b_replacer_33(done_keys_keys, what_replace_33_keys, on_what_replace_33_keys)
        else:
            done_keys_keys = done_keys_keys

        if eng_capital:
            eng_capital = True
            done_keys_keys = eng_capitalize(done_keys_keys)
        else:
            eng_capital = False
        if first_capital:
            done_keys_keys = first_capitalize (done_keys_keys)
        if spec_del:
            spec_replace = '+\n'
            on_what_spec_replace = '\n'
            done_keys_keys = b_replacer(done_keys_keys, spec_replace, on_what_spec_replace)
    else:
        set_keys = ''
        what_replace_keys = ''
        on_what_replace_keys = ''
        what_replace_33_keys = ''
        on_what_replace_33_keys = ''
        what_adds_33_keys = ''
        eng_capital = True
        first_capital = True
        spec_del = True

        done_keys_keys = ''

    done_keys_keys_33 = keys_33 (done_keys_keys, 33)

    return render_to_response('articles.html',{'set_keys_keys' : set_keys,
                                               'what_replace_keys':what_replace_keys,
                                               'on_what_replace_keys':on_what_replace_keys,
                                               'what_replace_33_keys':what_replace_33_keys,
                                               'on_what_replace_33_keys':on_what_replace_33_keys,
                                               'what_adds_33_keys':what_adds_33_keys,
                                               'done_keys_keys' : done_keys_keys,
                                               'done_keys_keys_33':done_keys_keys_33,
                                               'len_set':set_keys.count('\n')+1,
                                               'len_set_33':done_keys_keys_33.count('\n'),
                                               'ino_cap_check' : eng_capital,
                                               'first_cap_check': first_capital,
                                               'spec_del_check' : spec_del})





def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def basic_two(request):
    view = "basic_two"
    t = get_template('my_view.html')
    html = t.render(Context({'name': 'alex'}))
    return HttpResponse(html)

def basic_3(request):
    view = "basic_3"
    t = get_template('my_view.html')
    return render_to_response('my_view.html',{'name': 'alex'})

def articles (request):
    return render_to_response('articles.html',{'articles': Article.objects.all()})

def addlike (request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes +=1
        article.save()
    except ObjectDoesNotExist:
            raise Http404
    return redirect('/')

def article(request):
    comment_form = CommentForms
    args = {}
    args.update(csrf(request))
    args['form'] = comment_form
    return render_to_response('articles.html', args)

