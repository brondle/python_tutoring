$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();        $.ajax({
            url: "http://localhost:5000/api/",
            type: "GET",
            contentType: "application/json",
            data: JSON.stringify({"message": message})        }).done(function(data) {
            $("#message").text(data);        });    });});
