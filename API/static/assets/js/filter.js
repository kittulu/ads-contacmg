$(document).ready(function() {
	$('#filterOptions li a').click(function() {
		// fetch the class of the clicked item
		var ourClass = $(this).attr('class');
		
		// reset the active class on all the buttons
		$('#filterOptions li').removeClass('active');
		// update the active state on our clicked button
		$(this).parent().addClass('active');
		
		if(ourClass == 'all') {
			// show all our items
			$('#ourHolder').children('div.item').removeClass('d-none');	
		}
		else {
			// hide all elements that don't share ourClass
			$('#ourHolder').children('div:not(.' + ourClass + ')').removeClass('d-none');
			// show all elements that do share ourClass
            $('#ourHolder').children('div.' + ourClass).addClass('d-none')
		}
		return false;
	});
});