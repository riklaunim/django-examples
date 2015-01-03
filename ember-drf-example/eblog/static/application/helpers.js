(function(Blog, $, undefined ) {
    Ember.Handlebars.registerBoundHelper('date', function(date) {
        //moment.lang('pl');
        return moment(date).fromNow();
    });
}(window.Blog, jQuery));
