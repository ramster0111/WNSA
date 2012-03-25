//This file resizes content to fit the window

$(document).ready(function(){
    var c = document.getElementById("scenario");
    var ctx = c.getContext("2d");
    var wa = document.getElementById("workarea");
//    $("#workarea").height($("#workarea").height()-82);
    ctx.canvas.width  = window.innerWidth*0.98;
    ctx.canvas.height = $("#workarea").innerHeight();
    /*
    var oldCanvas = c.toDataURL("image/png");
    var img = new Image();
    img.src = oldCanvas;
    img.onload = function (){
        c.height = ($("#workarea").height());
        c.width = ($("#workarea").width());
        ctx.drawImage(img, 0, 0);
    } */
    ghostcanvas = document.createElement('canvas');
    HEIGHT = c.height;
    WIDTH = c.width;
    ghostcanvas.height = HEIGHT;
    ghostcanvas.width = WIDTH;
    gcxt = ghostcanvas.getContext('2d');
});

function editLayout(entity){
    
    
    
}
