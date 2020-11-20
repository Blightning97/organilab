function save_copy_laboratory(){
    console.log("Copying Lab")
    dataconfig = $("#id_dataconfig").val()
}
    
function pasting_laboratory(){
    console.log("Pasting Lab")
    old_dataconfig = $("#id_dataconfig").val()
}

$(document).ready(function() {
    console.log($("#id_dataconfig").val())
 });