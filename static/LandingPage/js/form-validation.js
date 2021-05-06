 jQuery(document).ready(function(){
    jQuery("#submitbtn").on('click',function(){
    
      var name = $("#name").val();
      var email = $("#email").val();
      var phone = $("#phone").val();
      var message = $("#message").val();
      
      var emailFilter = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;
      
      var dataString = 'name='+ name + '&email='+ email + '&phone='+ phone+ '&message='+ message;
      
      if ($.trim(name).length == '') {
        $("#name").css('border-bottom','2px solid #f26c4f'); //addClass()
        var na = false;
      }else{
        $("#name").css('border','1px solid #bcbcbc'); //addClass()
        var na = true;
      }
          
      if ($.trim(email).length == '' || !emailFilter.test(email)) {
        $("#email").css('border-bottom','2px solid #f26c4f'); 
        var em = false;
      }else{
        $("#email").css('border','1px solid #bcbcbc');
        var em = true;
      } 
  
      if ($.trim(phone).length == '') { 
        $("#phone").css('border-bottom','2px solid #f26c4f');
        var ph = false;
      }else{
        $("#phone").css('border','1px solid #bcbcbc');
        var ph = true;   
      }	
      if ($.trim(message).length == '') { 
        $("#message").css('border-bottom','2px solid #f26c4f');
        var message = false;
      }else{
        $("#message").css('border','1px solid #bcbcbc');
        var message = true;   
      }		
           
      if( na==true && em==true && ph == true && message == true ){
        jQuery.ajax({
          type: "POST", // For jQuery < 1.9
          url: "http://sbtechnosoft.com/ableedu/js/submitform.php",
          data: dataString, 
          cache: false,
          success: function(response){ 
            if (response == "success") {
              jQuery( "#errormsg" ).removeClass( "hidden solid #bcbcbc" );
            }
            else
            {
              jQuery( "#successmsg" ).removeClass( "hidden solid #bcbcbc" );
            }
          }
        });
      }
      return false;
    });
  });