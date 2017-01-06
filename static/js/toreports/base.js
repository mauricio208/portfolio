var editor;


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

function show_report(data){
	n_container = new Quill('#show_report');
	n_container.setContents(data)
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
	$("#report").val(JSON.stringify(editor.getContents()));
  	var $form = $( this );
 	$.post('ajax_save_report', $form.serialize() )
 		.done(function( data ) {
			$('#reports_container').append(data);
			$('#new_pacient').hide();
  		});
});
$( document ).ready(function() {
	var fonts = ['sofia', 'slabo', 'roboto', 'inconsolata', 'ubuntu'];
	var Font = Quill.import('formats/font');
	Font.whitelist = fonts;
	Quill.register(Font, true);
	var options = {
		 modules: {
	        // 'formula': true,
	        'toolbar': [
	          [{ 'font': fonts }, { 'size': [] }],
	          [ 'bold', 'italic', 'underline', 'strike' ],
	          [{ 'color': [] }, { 'background': [] }],

	          [{ 'header': '1' }, { 'header': '2' }, 'blockquote', 'code-block' ],
	          [{ 'list': 'ordered' }, { 'list': 'bullet'}, { 'indent': '-1' }, { 'indent': '+1' }],
	          [ 'direction', { 'align': [] }],
	          [ 'link',],
	          [ 'clean' ]
	        ],
	      },
			theme: 'snow'
		};
	editor = new Quill('#report_area', options);

});