nodeCount=0;
linkCount=0;
agentCount=0;
sourceCount=0;
sel="selector";  //0:Selector,1:Node,2:Link,3:Agent,4:Traffic Source
nodes=new Array();
links = new Array();
agents = new Array();
sources = new Array();

function Node(X,Y){
    this.x = X;
    this.y = Y;
    this.label = ""+nodeCount;
    this.color = "black";
    this.id = nodeCount;   //This will be a number
    this.size = 25;
}

function Link(n1,n2){   //n1 and n2 are two nodes or traffic source/sink pair
    this.id = linkCount;
    this.end1 = n1;
    this.end2 = n2;
    this.color = "black";
    this.delay = "20.0000ms";
    this.bandwidth = "1.000Mb";
    this.label = "";
    this.orientation = "";
    this.queuePos = "0.5";
    this.queueLimit = "20";   //Assume the data type of null strings
    this._x = 0;
    this._y = 0;
}    

function Agent(n){
    this.id = agentCount;
    this.type = "TCP";
    this.node = n; // n is a node
    this.properties = {} //A dictionary of properties to be specified
    this.connectedAgent= null; // a reference to another Agent
    this._x = 0;
    this._y = 0;
}

function Source(a){
    this.id = sourceCount;
    this.type = "FTP";
    this.agent = a; // This is of type Agent
    this.startTime = "0.000";
    this.stopTime = "60.000";   
    this._x = 0;
    this._y = 0;
}

function getMouse(e){
    if (document.defaultView && document.defaultView.getComputedStyle) {
        stylePaddingLeft = parseInt(document.defaultView.getComputedStyle(c, null)['paddingLeft'], 10)      || 0;
        stylePaddingTop  = parseInt(document.defaultView.getComputedStyle(c, null)['paddingTop'], 10)       || 0;
        styleBorderLeft  = parseInt(document.defaultView.getComputedStyle(c, null)['borderLeftWidth'], 10)  || 0;
        styleBorderTop   = parseInt(document.defaultView.getComputedStyle(c, null)['borderTopWidth'], 10)   || 0;
    }
    var element = c, offsetX = 0, offsetY = 0;
    if (element.offsetParent) {
        do {
            offsetX += element.offsetLeft;
            offsetY += element.offsetTop;
        } while ((element = element.offsetParent));
    }
    
    // Add padding and border style widths to offset
    offsetX += stylePaddingLeft;
    offsetY += stylePaddingTop;
    
    offsetX += styleBorderLeft;
    offsetY += styleBorderTop;
    
    mx = e.pageX - offsetX;
    my = e.pageY - offsetY
}

$(document).ready(function(){
    
    c=document.getElementById("scenario");
    ctx=c.getContext("2d");

//    status=document.getElementById("statusbar");
    document.getElementById("statusbar").innerHTML="Ready";
    addEvent(c, 'dragover', cancel);
    addEvent(c, 'dragenter', cancel);
    addEvent(c,'drop',draw);
    $(".entity img").click(function() {
        $("statusbar").text($(this).parent().attr('id'));
        sel=$(this).parent().attr('id');
        $(".entity").css('border','1px solid #999999');
        $("#"+sel).css('border','2pt solid #0f0f0f');
/*        if (sel == "node"){
            $("#entitypanel").add("<div id=\"choide\" class=\"action\">Router<\\div>");
        }
        else{
            $("#entitypanel").remove("#choice");
        }*/
        flag = 1;
    });
    $("#scenario").click(firstClick);
    $("#simulate").click(sendJSON);
});

function sendJSON(event){
    var values = new Array();
    values[0]=nodes;
    values[1]=links;
    values[2]=agents;
    values[3]=sources;
//    $.post('../',JSON.stringify({nodes:nodes,links:links,agents:agents,sources:sources}),writeNS);
    $.post('../',JSON.stringify(values),writeNS);
}
function writeNS(data,textStatus){
    
    $("pre").text(data);
}
function clear(c) {
  c.clearRect(0, 0, WIDTH, HEIGHT);
}
/*$(".entity img").click(function (){
    document.getElementById("statusbar").innerHTML="Clicked";
    flag=1;
});*/
function firstClick(event) {
    getMouse(event);
    if (sel === "none"){
        return;
    }
    getMouse(event);
    if (sel === "node"){
        addNode(mx,my,ctx);
        nodeCount++;
        return;
    }
    else if (sel === "link"){
        n1 = "undefined";
        n1 = getEntity("node",nodes,mx,my);
        if (n1){
            $("#scenario").bind('click',secondClick);
            $("#scenario").unbind('click',firstClick);
        }
        else {
            n1 = "undefined";
            n1 = getEntity("agent",agents,mx,my);
            if (n1){
                $("#scenario").bind('click',secondClick);
                $("#scenario").unbind('click',firstClick);
            }
        }
            
    }
    else if (sel === "agent"){
        n = "undefined";
        n = getEntity("node",nodes,mx,my);
        if (n){
            addAgent(n);
            agentCount++;
        }
    }
    else if (sel === "source"){
        a = "undefined";
        a = getEntity("agent",agents,mx,my);
        if (a){
            addSource(a);
            sourceCount++;
        }
    }
    return;
}

function secondClick(event){ 
   
    $("#scenario").bind('click',firstClick);
    $("#scenario").unbind('click',secondClick);
    if (sel != "link"){
        firstClick(event);
    }
    else {
        getMouse(event);
        $("#statusbar").text(linkCount);
        n2 = getEntity("node",nodes,mx,my);
        if (n1 && n2){
            if ((n1.type == n2.type) && (n1 != n2)){
                addLink(n1,n2);
                linkCount++;
            }
            else if (n1 === n2){
                $("#scenario").bind('click',secondClick);
                $("#scenario").unbind('click',firstClick);
            }
        }
        else {
            n2 = getEntity("agent",agents,mx,my);
            if (n1 && n2){
                if( (n1.type == n2.type) && (n1 != n2)){    //TODO:Remove this redundancy of code
                    addAgentLink(n1,n2);
                }
                else if (n1 === n2){
                    $("#scenario").bind('click',secondClick);
                    $("#scenario").unbind('click',firstClick);
                }
            }                   
        }
    }
}
function draw(event){
    if(event.preventDefault){
        event.preventDefault();
    }
    
    document.getElementById("statusbar").innerHTML = event.dataTransfer.getData('text/plain');
    
    getMouse(event);
    addNode(mx,my,ctx);
    nodeCount++;
    
}
function addLink(n1,n2){
    links[linkCount]=new Link(n1,n2);
    ctx.beginPath();
    ctx.strokeStyle = links[linkCount].color;
    var m=(n2.y-n1.y)/(n2.x-n1.x);
    var x1,x2,y1,y2;
    if (n1.x > n2.x){
        x1 = n1.x - n1.size / Math.sqrt(m*m+1);
        x2 = n2.x + n2.size / Math.sqrt(m*m+1);
    }
    else if (n1.x < n2.x){
        x1 = n1.x + n1.size / Math.sqrt(m*m+1);
        x2 = n2.x - n2.size / Math.sqrt(m*m+1);
    }
    else {
        x1=x2=n1.x;
    }
    if (n1.y > n2.y){
        y1 = n1.y - n1.size / Math.sqrt(1/(m*m)+1);
        y2 = n2.y + n2.size / Math.sqrt(1/(m*m)+1);
    }
    else if (n1.y < n2.y){
        y1 = n1.y + n1.size / Math.sqrt(1/(m*m)+1);
        y2 = n2.y - n2.size / Math.sqrt(1/(m*m)+1);
    }
    else {
        y1=y2=n1.y;
    }
    ctx.moveTo(x1,y1);
    ctx.lineTo(x2,y2);
    ctx.stroke();
    ctx.closePath();
}
function addAgent(n){
    agents[agentCount] = new Agent(n);
    agents[agentCount]._x = n.x;
    agents[agentCount]._y = n.y-n.size-10;
    ctx.strokeRect(agents[agentCount]._x-10,agents[agentCount]._y-5,20,10);
    ctx.fillStyle ="white";
    ctx.fillRect(agents[agentCount]._x-10,agents[agentCount]._y-5,20,10);
}
function addAgentLink(n1,n2){
    n1.connectedAgent=n2;
    n2.type = "TCPSink";
    //TODO: Draw a visualization
    ctx.beginPath();
    ctx.stroke();
    ctx.moveTo(n1._x,n1._y);
    ctx.lineTo(n2._x,n2._y);
    ctx.closePath();
    ctx.strokeStyle = 'green';
    ctx.stroke();
    
}
function addSource(a){  // `a` is the agent onto which the source is added
    sources[sourceCount] = new Source(a);
    sources[sourceCount]._x = a._x;
    sources[sourceCount]._y = a._y - 10;
    ctx.strokeStyle="green";
    ctx.strokeRect(a._x-10,sources[sourceCount]._y-5,20,10);
    ctx.fillStyle = "#aaffaa";
    ctx.fillRect(a._x-10,sources[sourceCount]._y-5,20,10);
}
function addNode(x,y,context){
    nodes[nodeCount]=new Node(x,y);
    context.strokeStyle=nodes[nodeCount].color;
    context.fillStyle = 'white';
    context.beginPath();
    node_img = new Image();
    node_img.src = "img/node.png"
    size = nodes[nodeCount].size
/*    context.arc(x,y,nodes[nodeCount].size,0,Math.PI*2,true);
    context.closePath();
    context.fill();
    context.stroke();*/
    context.fillStyle = "white";
    context.drawImage(node_img,x-size,y-size,2*size,2*size);
//    context.moveTo(x-size,y-size);
    context.textAllign = "centre";
    context.fillText(""+nodeCount,x-size/2,y-size/3);
}
function getEntity(typ,list,mx,my){
    clear(gcxt);
    for(var i = list.length-1; i >= 0; i--){
        drawBlackEntity(typ,list[i]);
        var imageData = gcxt.getImageData(mx,my,1,1);
        if (imageData.data[3] > 0){
            return list[i];
            clear(gcxt);
        }
    }
    clear(gcxt);
    return null;
        
}

function drawBlackEntity(typ,entity){
    if(typ === "node"){
        gcxt.strokeStyle = 'black';
        gcxt.fillStyle = 'black';
        gcxt.beginPath();
        gcxt.arc(entity.x,entity.y,entity.size,0,Math.PI*2,true);
        gcxt.closePath();
        gcxt.stroke();
        gcxt.fill();
    }
    if (typ === "agent"){
        gcxt.strokeStyle = 'black';
        gcxt.fillStyle = 'black';
        gcxt.strokeRect(entity.node.x-10,entity.node.y-entity.node.size-15,20,10);
        gcxt.fillRect(entity.node.x-10,entity.node.y-entity.node.size-15,20,10);
    }
}
function cancel(event){
    if(event.preventDefault){
        event.preventDefault();
    }
//    event.dataTransfer.

    return false;
}


