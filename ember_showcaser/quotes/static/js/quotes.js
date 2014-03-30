(function($, undefined ) {
    Quotes = Ember.Application.create();
    Quotes.ApplicationAdapter = DS.DjangoTastypieAdapter.extend({});
    Quotes.ApplicationSerializer = DS.DjangoTastypieSerializer.extend({});

    var attr = DS.attr;

    Quotes.Quote = DS.Model.extend({
        quote: attr('string'),
        poster: DS.belongsTo('user'),
        posted_date: attr('date')
    });
    Quotes.User = DS.Model.extend({
        username: attr('string')
    });

    Quotes.Router.map(function() {
        this.route('quotes-list');
        this.route('about');
        this.route('contact');
        this.route('add-quote');
    });

    Quotes.IndexRoute = Ember.Route.extend({
        redirect: function() {
            this.transitionTo('quotes-list');
        }
    });
    Quotes.QuotesListRoute = Ember.Route.extend({
        model: function() {
            return this.store.find('quote');
        }
    });

    Quotes.AddQuoteController = Em.Controller.extend({
        quote: '',
        actions: {
            saveQuote: function(text) {
                if (text) {
                    this.store.createRecord('quote', {'quote': text}).save();
                    this.set('quote', '');
                    this.transitionToRoute('quotes-list');
                }
            }
        }
    });

    Quotes.AddQuoteView = Ember.View.extend({
        submit: function() {
            var text = this.get('controller.quote');
            this.get('controller').send('saveQuote', text);
        }
    });
}(jQuery));
