console.log('script:admin');

jQuery(document).ready(function($){

	var category_icon_select = $('#id_icon');
	var category_color = $('#id_color')

	category_icon_select.select2({

		escapeMarkup: function(markup) {
		    return markup;
		},
		
	});

	category_color.spectrum({
	    showInput: true
	});
});