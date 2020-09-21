$("document").ready(function(){
  var message = $("#demo").val();        ajax({
        	// url: 'http://example.com/refresh.php',
  url:"http://localhost:5000/api/",
  type: "POST",
  data: {myNumber: Math.random(),
  },
  success: function(data) {
      $('#container').html(data).delay(2000);
  }
})});
