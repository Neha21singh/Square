//$("#project_form").submit(function (event) {
//	postForm($(this), $("#action").attr('formaction'));	
//    event.preventDefault();
//});
alert('hy');
session_info={}
session_info.page={}
session_info.page.SECTORS = (session_info.page.SECTORS === undefined) ? 'any' : session_info.page.SECTORS
session_info.page.BLOCKS = (session_info.page.BLOCKS === undefined) ? 'any' : session_info.page.BLOCKS

$('#SECTORS').val((session_info.page.SECTORS === undefined) ? 'any' : session_info.page.SECTORS);
$('#BLOCKS').val((session_info.page.BLOCKS === undefined) ? 'any' : session_info.page.BLOCKS);

function filter_SECTORS(val){
//alert(val);
//$('#lang').val();
session_info.page.SECTORS= val;
x_load('todo.projects/?p_SECTORS=' + session_info.page.SECTORS + '&p_BLOCKS=' + session_info.page.BLOCKS);

}

function filter_BLOCKS(val){
//alert(val);
session_info.page.BLOCKS= val;
x_load('todo.projects/?p_SECTORS=' + session_info.page.SECTORS + '&p_BLOCKS=' + session_info.page.BLOCKS);

}
