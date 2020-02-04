(function() {
	var Sidebar = function(el, multiple) {
		this.el = el || {};
		this.multiple = multiple || false;

		var link = this('.link-menu');
		link.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
	};

	Sidebar.prototype.dropdown = function(e) {
		var el = e.data.el,
			self = this,
			next = self.next();

		next.slideToggle();
		self.parent().toggleClass('open');

		if (!e.data.multiple) {
			el.find('.submenu').not(next).slideUp().parent().removeClass('open');
		}
	}
	var sidebar = new Sidebar(document.getElementById('#sidebar'), false);
})();