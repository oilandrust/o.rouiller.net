from django.views import generic
from blog.models import Post

class PostList(generic.ListView):
    queryset = Post.objects.published()
    template_name = 'blog/blog.html'
    paginate_by = 10
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/blog_post.html'
