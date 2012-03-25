//This file creates the forms to edit an object

$(document).ready(function (){

    $("#scenario").click(function(event){
        if(sel === "selector"){
            selectEntity(event);
        }
    });
});

function selectEntity(event){
    getMouse(event);
    n = getEntity("node",nodes,mx,my);
    
    if (n){
        editLayout(n);
    }
    
}
