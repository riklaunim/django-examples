(function(Blog, $, undefined) {
    Blog.Router.map(function() {
        this.route('posts');
        this.route('categoryPosts', {path: 'category/:id'});
        this.route('post', {path: 'posts/:id'});
    });
    if (window.history && window.history.pushState) {
        Blog.Router.reopen({
          location: 'history'
        });
    }
}(window.Blog, jQuery));
