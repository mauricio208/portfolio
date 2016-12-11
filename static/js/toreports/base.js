function new_pacient () {
	$np=$('#new_pacient')
	$np.toggle();
	$np.find('input[name="name"]').val('');

}	
function open_new_report(id){
	$nr=$('#new_report')
	$nr.toggle();
	$nr.find('input[name="date"]').val('');
	$nr.find('input[name="report"]').val('');
	$nr.find('input[name="pacient_id"]').val(id);
} 
function load_reports(id){
 	$.get('ajax_load_reports',"pacient_id="+id)
 		.done(function( data ) {
    		$('#reports_container').html('');
			$('#reports_container').append(data);
	});
 	$ar=$('#add_report')
	$ar.show();
	$ar.attr('onclick', "open_new_report("+id+")");
}

$('#save_pacient').submit(function (event) {
	event.preventDefault();
  	var $form = $( this );
 	$.post('ajax_save_pacient', $form.serialize() )
 		.done(function( data ) {
    		$('#pacient_container').append(data)
			$('#new_pacient').hide();
  		});
});

$('#save_report').submit(function (event) {
	event.preventDefault();
  	var $form = $( this );
 	$.post('ajax_save_report', $form.serialize() )
 		.done(function( data ) {
    		$('#reports_container').append(data)
			$('#new_pacient').hide();
  		});
});