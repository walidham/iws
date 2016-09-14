function Client(data) {
    
    this.id = data.id;
    this.company_name = data.company_name;
    this.email = ko.observable(data.email);
    this.description = ko.observable(data.description);
}

function Feature(data,self) {
    this.id = ko.observable(data.id);
    this.title = ko.observable(data.title);
    this.target_date = ko.observable(data.target_date);
    this.description = ko.observable(data.description);
    this.ticket_url = ko.observable(data.ticket_url);
    this.client_priority = ko.observable(data.client_priority);
    this.client_id = ko.observable(GetClient(data.client_id,self).id);
    this.client_name = ko.observable(GetClient(data.client_id,self).company_name);
    alert(this.client_name);
}

function GetClient(id,self){
    var client;

    ko.utils.arrayForEach(self.clients(), function(c) {
        if(c.id == id){
	    
            client= c;
	}
    });
    alert(client);

    return client;
}

function FeatureListViewModel() {


    var self = this;
    self.clients = ko.observableArray([]);

    $.getJSON('/admin/clients_list', function(clientModels) {
	var t = $.map(clientModels.clients, function(item) {
	    return new Client(item);
	});
	
	self.clients(t);
    });



    self.features = ko.observableArray([]);

    self.newTitle = ko.observable();
    self.newDesc = ko.observable();
    self.newTargetDate = ko.observable();
    self.newTicketUrl = ko.observable();
    self.newClientPriority = ko.observable();
    self.newClient = ko.observable();
    

    self.addFeature = function() {
	self.save();
	self.newTitle("");
	self.newDesc("");
        self.newTargetDate("");
	self.newTicketUrl("");
	self.newClientPriority("");
	self.newClient("");
    };

    $.getJSON('/features_list', function(featureModels) {
	var t = $.map(featureModels.features, function(item) {
	    return new Feature(item,self);
	});
	self.features(t);
    });

    self.save = function() {

	return $.ajax({
	    url: '/new_feature',
	    contentType: 'application/json',
	    type: 'POST',
	    data: JSON.stringify({
		'title': self.newTitle(),
		'target_date': self.newTargetDate(),
		'ticket_url': self.newTicketUrl(),
		'client_id': self.newClient().id,
		'client_priority': self.newClientPriority(),
		'description': self.newDesc()
	    }),
	    success: function(data) {
		console.log("Pushing to feature array");
		self.clients.push(new Client({ title: data.title, target_date: data.target_date, 
			description: data.description,ticket_url: data.ticket_url,client_priority: data.client_priority,client_id: data.client_id, id: data.id}));
		$('#new_feature').modal('hide')
		return;
	    },
	    error: function(e) {
		return console.log("Failed"+e);
	    }
	});
    };
}

ko.applyBindings(new FeatureListViewModel());
