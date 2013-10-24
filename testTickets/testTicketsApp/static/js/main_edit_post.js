
 $(document).ready(function(){
     function showProgress() {
        $("form input, form textarea").prop('disabled', 'disabled');
        $('#progress').show();
     }

     function ajaxSuccess(){
         $("form input, form textarea").removeProp('disabled');
         $("#submit_status").text("Changes have been saved");
         $('#progress').hide();
     }

     function ajaxError(){
         $("#submit_status").text("Update error");
     }

     var options = {
         target: $('body'),
         beforeSubmit: showProgress,
         success: ajaxSuccess,
         error:ajaxError
     };

     $('#formid').submit(function() {
         $(this).ajaxSubmit(options);
         return false;
     });
});
