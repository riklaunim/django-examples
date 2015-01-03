(function(Blog, $, undefined ) {
    Blog.ApplicationController = Ember.ObjectController.extend({
        categories: function() {
            return this.get('store').find('category');
        }.property(),
        makeCurrentPathGlobal: function() {
            Blog.set('currentPath', this.get('currentPath'));
        }.observes('currentPath')
    });
    Blog.PostController = Ember.ObjectController.extend({
        isPython: function() {
            var title = this.get('content.title').toLowerCase();
            var category = this.get('content.category.name');
            if (category) {
                category = category.toLowerCase();
                return title.indexOf('python') != -1 || category.indexOf('python') != -1;
            }
        }.property('content.title', 'content.category.name')
    });
    Blog.CategoryController = Ember.ObjectController.extend({
        needs: ["post"],
        isActive: function() {
            var path = Blog.get('currentPath');
            console.log(path, path == 'post' && this.get('content.id') == this.get('controllers.post.content.category.id'));
            return path == 'post' && this.get('content.id') == this.get('controllers.post.content.category.id');
        }.property('content.id', 'controllers.post.content.category.id', 'Blog.currentPath')
    });
}(window.Blog, jQuery));
