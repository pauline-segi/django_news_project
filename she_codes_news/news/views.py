from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import CommentForm, StoryForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect, get_object_or_404



class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by("-pub_date", "title")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by("-pub_date", "title").all()[:4]
        context['all_stories'] = NewsStory.objects.order_by("-pub_date", "title")
        #print(NewsStory.objects.all()[:4])
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        # Order comments by their created_date in descending order (most recent first)
        context['comments'] = story.comments.filter(approved_comment=True).order_by('-created_date')
        context['form'] = CommentForm()
        return context


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def get_success_url(self):
    '''Get the success URL for the form.'''
    news_story = self.get_object()
    return reverse_lazy('news:story', kwargs={'pk': news_story.pk})


class AddCommentView(View):
    def post(self, request, pk):
        news_story = get_object_or_404(NewsStory, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = news_story
            comment.save()
        
        # Get the updated list of comments for the story
        comments = news_story.comments.filter(approved_comment=True)

        # Pass the updated list of comments to the template
        return render(request, 'news/story.html', {'story': news_story, 'comments': comments})

    def get_object(self):
        """Get the news story that the comment is being added to."""
        news_story_pk = self.kwargs['pk']
        return NewsStory.objects.get(pk=news_story_pk)





