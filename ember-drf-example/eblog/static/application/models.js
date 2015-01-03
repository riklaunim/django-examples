(function(Blog, $, undefined ) {
    Blog.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
        namespace: "api"
    });
    Blog.Category = DS.Model.extend({
        name: DS.attr('string'),
        slug: DS.attr('string')
    });
    Blog.Post = DS.Model.extend({
        title: DS.attr('string'),
        slug: DS.attr('string'),
        text: DS.attr('string'),
        category: DS.belongsTo('category', {async: true}),
        posted_date: DS.attr('date')
    });
}(window.Blog, jQuery));
