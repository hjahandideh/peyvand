$(document).ready(function(){
   $('#frmpayam').submit(function(){

       var payam=$('#mpayam').val();
       $.ajax({

       url:'url_',
       type:POST,
       data:{mpayam:payam},

       statusCode:{
           404:function(){
               $('#result').text('not foound');
           }
       },
           success:function(data){
            $('#result').text(data)
           }

       });

   });
});