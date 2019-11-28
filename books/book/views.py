from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_GET

from django.views.generic import (View, TemplateView, RedirectView, ListView, DeleteView,DetailView, FormView,
                                CreateView, UpdateView)

from .models import Book, Author
from .forms import AuthorForm, AuthorModelForm


class DetailsView(DetailView):
    template_name = 'book/detail.html'
    model= Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['form'] = AuthorForm()
        context['model_form'] = AuthorModelForm()
        return context




class IndexView(ListView):
    template_name = 'book/index.html'
    # model= Author
    context_object_name = 'latest_question_list'

    queryset = Author.objects.order_by('first_name')# mozhno ne ykaz. model


class ChoiceFormView(FormView):
    template_name = 'book/detail.html'
    form_class = AuthorModelForm
    success_url = '/book' #redirect


class ChoiceCreate(CreateView):
    model = Author
    fields = ['first_name'] #create form fields

    template_name = 'book/detail.html'
    success_url = '/book'




def vote(request, question_id):
    question = get_object_or_404(Author, pk=question_id)

    # form = AuthorForm(request.POST) #create form
    form = AuthorModelForm(request.POST) #instance=choice - for edit object


    if form.is_valid():
        form.save() #for AuthorModelForm
        data = form.cleaned_data['question_id']

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'book/detail.html', {
                'question':question,
            })
        else:
            selected_choice.votes +=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('results', args=(question.id,)))
    return render(request, 'book/detail.html', context = {'form':form, 'question':question })


# class IndexView(TemplateView):
#     template_name = 'book/index.html'

#     def get_context_data(self):
#         context = super().get_context_data()
#         latest_question_list = Author.objects.all()
#         context['latest_question_list'] = latest_question_list
#         return context



# class IndexView(View):
#     def get(self, request):
#         name = request.GET.get('name')
#         latest_question_list = Author.objects.all()
#         if name:
#             latest_question_list = latest_question_list.filter(first_name__icontains=name)

#         context = {'latest_question_list':latest_question_list}

#         return render(request, 'book/index.html', context)

#     def post(self, request):
        



# @require_GET
# def index(request):

#     name = request.GET.get('name')

#     method = request.method

#     print(request.COOKIES)
#     print(request.FILES)
#     print(request.user)
#     # print(request.user.is_authentificated) #only authentificated users

#     latest_question_list = Author.objects.all()
#     if name:
#         latest_question_list = latest_question_list.filter(first_name__icontains=name)

#     context = {'latest_question_list':latest_question_list}

#     return render(request, 'book/index.html', context)

