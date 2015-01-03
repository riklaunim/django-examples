(function(Blog, $, undefined ) {
    Blog.IndexRoute = Ember.Route.extend({
        redirect: function() {
            this.transitionTo('posts');
        }
    });
    Blog.PostsRoute = Ember.Route.extend({
        model: function() {
            return this.get('store').find('post');
        }
    });
    Blog.CategoryPostsRoute = Ember.Route.extend({
        model: function(params) {
            return this.get('store').find('post', {'category': params.id });
        }
    });
    Blog.PostRoute = Ember.Route.extend({
        model: function(params) {
            return this.get('store').find('post', params.id);
        }
    });
}(window.Blog, jQuery));
