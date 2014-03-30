(function($, undefined ) {
    Quotes = Ember.Application.create();
    Quotes.store = DS.Store.create({
        revision: 11,
        adapter: DS.DjangoTastypieAdapter.extend()
    });

    var attr = DS.attr;

    Quotes.Quote = DS.Model.extend({
        quote: attr('string'),
        poster: DS.belongsTo('Quotes.User'),
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
        setupController: function(controller) {
            this._super();
            controller.set('quotes', Quotes.Quote.find());
        }
    });

    Quotes.AddQuoteController = Em.Controller.extend({
        quote: '',
        saveQuote: function(text) {
            if (text) {
                var quote = Quotes.Quote.createRecord({'quote': text});
                quote.store.commit();
                this.set('quote', '');
                this.transitionToRoute('quotes-list');
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
