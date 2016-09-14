function Client(data) {
    this.id = ko.observable(data.id);
    this.company_name = ko.observable(data.company_name);
    this.email = ko.observable(data.email);
    this.description = ko.observable(data.description);
}

function ClientListViewModel() {
    var self = this;
    self.clients = ko.observableArray([]);
    self.newClientCN = ko.observable();
    self.newClientEmail = ko.observable();
    self.newClientDesc = ko.observable();

    self.addClient = function() {
	self.save();
	self.newClientCN("");
	self.newClientEmail("");
        self.newClientDesc("");
    };

    $.getJSON('/admin/clients_list', function(clientModels) {
	var t = $.map(clientModels.clients, function(item) {
	    return new Client(item);
	});
	
	self.clients(t);
    });

    self.save = function() {
//alert( self.newClientCN()+ "    "+self.newClientEmail()+"    "+self.newClientDesc());
	return $.ajax({
	    url: '/admin/new_client',
	    contentType: 'application/json',
	    type: 'POST',
	    data: JSON.stringify({
		'company_name': self.newClientCN(),
		'email': self.newClientEmail(),
		'description': self.newClientDesc()
	    }),
	    success: function(data) {
		console.log("Pushing to clients array");
		self.clients.push(new Client({ company_name: data.company_name, email: data.email, description: data.description, id: data.id}));
		$('#new_client').modal('hide')
		return;
	    },
	    error: function(e) {
		return console.log("Failed"+e);
	    }
	});
    };
}

ko.applyBindings(new ClientListViewModel());
