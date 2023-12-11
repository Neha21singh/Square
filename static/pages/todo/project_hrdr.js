//$("#project_form").submit(function (event) {
//	postForm($(this), $("#action").attr('formaction'));	
//    event.preventDefault();
//});
alert('hy');
session_info={}
session_info.page={}
session_info.curr={}
session_info.page.SECTORS = (session_info.page.SECTORS === undefined) ? 'any' : session_info.page.SECTORS
session_info.page.BLOCKS = (session_info.page.BLOCKS === undefined) ? 'any' : session_info.page.BLOCKS

$('#SECTORS').val((session_info.page.SECTORS === undefined) ? 'any' : session_info.page.SECTORS);
$('#BLOCKS').val((session_info.page.BLOCKS === undefined) ? 'any' : session_info.page.BLOCKS);

x_getJSON("/api/project/", function( data ) {
	$('#BLOCKS').empty();
    $('#BLOCKS').append('<option value="">All BLOCKS</option>');
	$.each(data.projects, function () {
		var option = $('<option />');
		option.attr('value', this['_id']).text(this['BLOCKS']);
		$('#BLOCKS').append(option);	
	});
	if(session_info.curr.sel_BLOCKS!==undefined && session_info.curr.sel_BLOCKS!==''){
		$('#BLOCKS').val(session_info.curr.sel_BLOCKS);
		refproject();
	}			
});


function addproject(){	
	alert('Updated Function');
	session_info.curr.sel_BLOCKS=$('#BLOCKS').val();
	session_info.curr.sel_BLOCKS=$('#BLOCKS option:selected').text();
	s="todo.project"
	console.log(s)
	x_load(s);
}

function refproject(){
	s="todo.project_list/?BLOCKS="+session_info.curr.sel_BLOCKS
	console.log(s)
	x_load(s);
}