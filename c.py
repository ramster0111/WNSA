#!/usr/bin/env python

import os
import re 
import string
import json
import math
import sys
#tclfile = open('tclfile.tcl','w')
datafromserver = []
def readModel(dfs):
    global datafromserver
    if dfs:
        datafromserver = dfs
    else:
        string = '[[{"x":133,"y":196,"label":"0","color":"black","id":0,"size":25},{"x":303,"y":117,"label":"1","color":"black","id":1,"size":25},{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},{"x":704,"y":310,"label":"4","color":"black","id":4,"size":25},{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},{"x":469,"y":382,"label":"6","color":"black","id":6,"size":25}],[{"id":0,"end1":{"x":133,"y":196,"label":"0","color":"black","id":0,"size":25},"end2":{"x":303,"y":117,"label":"1","color":"black","id":1,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":1,"end1":{"x":303,"y":117,"label":"1","color":"black","id":1,"size":25},"end2":{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":2,"end1":{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},"end2":{"x":469,"y":382,"label":"6","color":"black","id":6,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":3,"end1":{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},"end2":{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":4,"end1":{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},"end2":{"x":704,"y":310,"label":"4","color":"black","id":4,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":5,"end1":{"x":704,"y":310,"label":"4","color":"black","id":4,"size":25},"end2":{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":6,"end1":{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},"end2":{"x":469,"y":382,"label":"6","color":"black","id":6,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""},{"id":7,"end1":{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},"end2":{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},"color":"black","delay":"","bandwidth":"","label":"","orientation":"","queuePos":"","queueLimit":""}],[{"id":0,"type":"","node":{"x":133,"y":196,"label":"0","color":"black","id":0,"size":25},"properties":{},"connectedAgent":null},{"id":1,"type":"","node":{"x":303,"y":117,"label":"1","color":"black","id":1,"size":25},"properties":{},"connectedAgent":null},{"id":2,"type":"","node":{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},"properties":{},"connectedAgent":null},{"id":3,"type":"","node":{"x":469,"y":382,"label":"6","color":"black","id":6,"size":25},"properties":{},"connectedAgent":null},{"id":4,"type":"","node":{"x":704,"y":310,"label":"4","color":"black","id":4,"size":25},"properties":{},"connectedAgent":null},{"id":5,"type":"","node":{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},"properties":{},"connectedAgent":null},{"id":6,"type":"","node":{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},"properties":{},"connectedAgent":null}],[{"id":0,"type":"","agent":{"id":0,"type":"","node":{"x":133,"y":196,"label":"0","color":"black","id":0,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":1,"type":"","agent":{"id":1,"type":"","node":{"x":303,"y":117,"label":"1","color":"black","id":1,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":2,"type":"","agent":{"id":2,"type":"","node":{"x":363,"y":280,"label":"2","color":"black","id":2,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":3,"type":"","agent":{"id":6,"type":"","node":{"x":554,"y":99,"label":"3","color":"black","id":3,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":4,"type":"","agent":{"id":5,"type":"","node":{"x":747,"y":98,"label":"5","color":"black","id":5,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":5,"type":"","agent":{"id":4,"type":"","node":{"x":704,"y":310,"label":"4","color":"black","id":4,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""},{"id":6,"type":"","agent":{"id":3,"type":"","node":{"x":469,"y":382,"label":"6","color":"black","id":6,"size":25},"properties":{},"connectedAgent":null},"startTime":"","stopTime":""}]]  '
        datafromserver = json.loads(string)


code = ""

#code += '\n'+ a

nodes = []
#code += '\n'+ nodes

links = []
#code += '\n'+ links

agents = []
#code += '\n'+ agents

sources = []
#code += '\n'+ sources
#for array in datafromserver:
#    code += '\n'+ i
#    for j in i:
#        code += '\n'+ j
#        code += '\n'+ "inner element ended"
#    code += '\n'+ "element ended"

def init():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code

#    set ns [new Simulator]
# Create a nam trace datafile.
#set namfile [open exp.nam w]
#$ns namtrace-all $namfile
    code += '\n' + "set ns [new Simulator]\n"
    code += '\n' + "set namfile [open a.nam w]\n"
    code += '\n' + "$ns namtrace-all $namfile\n"
#    code += '\n'+"#Node Creation Section Ends\n\n"
#    code += '\n'+"#Link Creation Section Begins\n\n"
#    code += '\n'+"#Link Creation Section Ends\n\n"
#    code += '\n'+"#Assign Queue size Section Begins\n\n"
#    code += '\n'+"#Assign Queue size Section Ends\n\n"
#    code += '\n'+"#Node Creation Section Begins\n\n"
#    code += '\n'+"#Node Creation Section Ends\n\n"


def final():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code
#proc finish {} {
#    global ns namfile
#    $ns flush-trace
#    close $namfile
#    exec nam -r 2000.000000us exp.nam &    
#    exit 0
#    }
#$ns at 60.000000 "finish"
#$ns run
    code += '\n'+ "proc finish {} {\n"
    code += '\n'+ "    global ns namfile\n\n\n"
    code += '\n'+ "    $ns flush-trace\n"
    code += '\n'+ "    close $namfile\n"
    code += '\n'+ "    exec nam -r 2000.000000us a.nam &\n"
    code += '\n'+ "    exit 0\n"
    code += '\n'+ "    }\n"
    code += '\n'+ "$ns at 60.000000 \"finish\"\n"
    code += '\n'+ "$ns run\n"


# Create wired nodes.
#set node(2) [$ns node]
## node(2) at 536.546875,588.968750
#$node(2) set X_ 536.546875
#$node(2) set Y_ 588.968750
#$node(2) set Z_ 0.0
#$node(2) color "black"
#$ns at 0.0 "$node(2) label n1"

def createnodes():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code
    #code += '\n'+ nodes
    for node in nodes:
        #code += '\n'+ "\n\n"        
        #code += '\n'+ node
        #code += '\n'+ node['id']
        toWriteline=""
        toWriteline+="\nset" + "  "
        toWriteline+="nsnode" + str(node['id'])
        toWriteline+="  " + "[$ns node]"
        code += '\n'+ toWriteline
        toWriteline=""
        toWriteline+="$nsnode" + str(node['id']) + " set X_ " + str(node['x'])
        code += '\n'+ toWriteline
        
        toWriteline=""
        toWriteline+="$nsnode" + str(node['id']) + " set Y_ " + str(node['y'])
        code += '\n'+ toWriteline

        toWriteline=""
        toWriteline+="$nsnode" + str(node['id']) + " color " + "\"" + str(node['color']) + "\""
        code += '\n'+ toWriteline
        
        toWriteline=""
        toWriteline+="$ns at 0.0 " + "\"" + "$nsnode"+str(node['id']) + " label n" + str(node['label']) +"\"" 
        code += '\n'+ toWriteline
        
#{u'end1': {u'color': u'black', u'label': u'0', u'y': 196, u'x': 133, u'id': 0, u'size': 25}, u'queuePos': '', u'end2': {u'color': u'black', u'label': u'1', #u'y': 117, u'x': 303, u'id': 1, u'size': 25}, u'queueLimit': '', u'orientation': '', u'color': u'black', u'label': '', u'delay': '', u'bandwidth': '', #u'id': 0}


        

# Create links between nodes.
#$ns duplex-link $node(2) $node(1) 1.000000Mb 20.000000ms DropTail
#$ns duplex-link-op $node(2) $node(1) queuePos 0.5
#$ns duplex-link-op $node(2) $node(1) color black
#$ns duplex-link-op $node(2) $node(1) orient 174.7deg
#$ns duplex-link-op $node(2) $node(1) label l1
# Set Queue Properties for link 2->1
#[[$ns link $node(2) $node(1)] queue] set limit_ 20

def createlinks():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code
    #code += '\n'+ links
    for link in links:
#        code += '\n'+ link
        code += '\n'+ "\n"
        toWriteline=""
        linktype="duplex-link"  #FIXME: Figure out link type
        if link['bandwidth']=='':        
            link['bandwidth'] = "1.00000Mb"
        if link['orientation']=='':
            if (link['end1']['x'] - link['end2']['x']) != 0:
                angle =  math.degrees( math.atan( ( link['end1']['y'] - link['end2']['y'] ) / (link['end1']['x'] - link['end2']['x']) ) )
            elif ( link['end1']['y'] - link['end2']['y'] ) < 0:
                angle = 270
            else:
                angle =90
            if angle < 0:
                angle = 360 - angle
            link['orientation']= angle
        if link['delay']=='':        
            link['delay'] = "20.00000ms"
        if link['queuePos']=='':        
            link['queuePos'] = ".5"
        if link['queueLimit']=='':        
            link['queueLimit'] = "20"
    
        toWriteline+="$ns "+ str(linktype) +  " $nsnode" + str(link['end1']['id']) + " $nsnode" + str(link['end2']['id']) + " " + str(link['bandwidth']) + " " + str(link['delay']) + " DropTail"
        code += '\n'+ toWriteline
        
        toWriteline=""
        toWriteline+="$ns "+ str(linktype) +"-op" +  " $nsnode" + str(link['end1']['id']) + " $nsnode" + str(link['end2']['id']) + " queuePos " + str(link['queuePos'])
        code += '\n'+ toWriteline

        toWriteline=""
        toWriteline+="$ns "+ str(linktype) +"-op" +  " $nsnode" + str(link['end1']['id']) + " $nsnode" + str(link['end2']['id']) + " orient " + str(link['orientation'])
        code += '\n'+ toWriteline

        toWriteline=""
        toWriteline+="$ns "+ str(linktype) +"-op" +  " $nsnode" + str(link['end1']['id']) + " $nsnode" + str(link['end2']['id']) + " color " + str(link['color'])
        code += '\n'+ toWriteline
        
        toWriteline=""
        toWriteline+="[[$ns "+ "link" +  " $nsnode" + str(link['end1']['id']) + " $nsnode" + str(link['end2']['id']) + "] queue]  set limit_ " + str(link['queueLimit'])
        code += '\n'+ toWriteline
        
#{u'node': {u'color': u'black', u'label': u'0', u'y': 196, u'x': 133, u'id': 0, u'size': 25}, u'connectedAgent': None, u'type': '', u'id': 0, u'properties': #{}}

# Create agents.
#set agent(2) [new Agent/TCP]
#$ns attach-agent $node(2) $agent(2)


def createagents():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code
    #code += '\n'+ agents

    for agent in agents:
        #code += '\n'+ agent
        if agent['type']=='':
            agent['type'] = "TCP"
        
        toWriteline=""
        toWriteline+="\nset" + "  agent" + str(agent['id']) + " [new Agent/" + str(agent['type']) +"]"
        code += '\n'+ toWriteline
         
        toWriteline=""
        toWriteline+="$ns attach-agent" + " $nsnode" + str(agent['node']['id']) + " $agent" + str(agent['id'])
        code += '\n'+ toWriteline
        
    for agent in agents:
        if agent['connectedAgent']:
            toWriteline="$ns connect $agent"+str(agent['id'])+" $agent"+str(agent['connectedAgent']['id'])
            code +='\n' +toWriteline
        
       


#{u'startTime': '', u'stopTime': '', u'type': '', u'id': 0, u'agent': {u'node': {u'color': u'black', u'label': u'0', u'y': 196, u'x': 133, u'id': 0, u'size': #25}, u'connectedAgent': None, u'type': '', u'id': 0, u'properties': {}}}

#set traffic_source(2) [new Application/FTP]
#$traffic_source(2) attach-agent $agent(2)
#$traffic_source(2) set maxpkts_ 256


def createsources():
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    global code
    for source in sources:
        #code += '\n'+ source
        if source['type']=='':
            source['type'] = "FTP"
        
        toWriteline=""
        toWriteline+="\nset" + "  traffic_source" + str(source['id']) + " [new Application/" + str(source['type']) +"]"
        code += '\n'+ toWriteline
         
        toWriteline=""        
        toWriteline+= "$traffic_source" + str(source['id']) + " attach-agent $agent" + str(source['agent']['id'])
        code += '\n'+ toWriteline
        
        toWriteline="$ns at "+str(source['startTime'])+" \"$traffic_source"+str(source['id'])+" start\""
        code += '\n' + toWriteline
        toWriteline="$ns at "+str(source['stopTime'])+" \"$traffic_source"+str(source['id'])+" stop\""
        code += '\n' + toWriteline
        


def main():
    global code
    global nodes
    global links
    global agents
    global sources
    global datafromserver
    nodes = datafromserver[0]
    #code += '\n'+ nodes

    links = datafromserver[1]
    #code += '\n'+ links

    agents = datafromserver[2]
    #code += '\n'+ agents

    sources = datafromserver[3]
    code = "";
    init()
    createnodes()
    createlinks()
    createagents()
    createsources()
    code += '\n'+ "\n\n\n"
    final()
    return code
#    xml_file = os.path.abspath(__file__)
#    xml_file = os.path.dirname(xml_file)
    #xml_file += "/a.xml"
#    xml_file = os.path.join(xml_file, "a.xml")
    #element = ET.XML(xml_file)
#    tree = ET.parse(xml_file).getroot()
#    code += '\n'+ tree
#    tclfile1 = open('tclfile.tcl','r')
#    tclfile2 = open('gentclfile.tcl','w')
    #Node Creation Section Ends
#    NumNodes=0
#    NodeList=[]
    
#    NumLinks=0
#    LinkList= dict()
#    LinkList.setdefault(NumLinks, [])
#    #LinkList.append
#    LinkList[0]=NodeList

#    NumAgents=0
#    AgentNameList=[]
#    AgentList= dict()
#    AgentList.setdefault(NumLinks, [])
    #LinkList.append
#    AgentList[0]=NodeList

    
    
#parsing the tree and counting the number of nodes and links present in the system with there names
#    for element in tree:
#        if element.tag == "node":
#            NumNodes+=1
#            NodeList.append(element.text)
#        if element.tag == "link":
#            NumLinks+=1
#        if element.tag =="agent":#
#            NumAgents+=1
#            AgentNameList.append(element.text)
            #LinkList.append(element.text)
#    code += '\n'+ NodeList
#    code += '\n'+ NumNodes
#    code += '\n'+ LinkList
#    code += '\n'+ NumLinks
#    code += '\n'+ NumAgents
#    code += '\n'+ AgentList
#    code += '\n'+ AgentNameList
#
##generating the code for the creation of these nodes
#    toWriteline=""
#    for j in range(NumNodes):
#        toWriteline+="\nset" + "  "
#        toWriteline+=str(NodeList[j])
#        toWriteline+="  " + "[$ns node]"
#    code += '\n'+ toWriteline

#$ns duplex-link $n0 $n1 2Mb 10ms DropTail


#    linkwrite=""

#generating link code
#    for k in range(NumLinks):
#        linkwrite+="$ns duplex-link"
#        linkwrite+=" "+ "$" + str(LinkList[k][0]) + " " + "$" + str(LinkList[k][1]) + " "
#        linkwrite+="2Mb 10ms DropTail"
        



#    linkwrite+="\n$ns queue-limit $n0 $n1 10" + "\n$ns duplex-link-op $n0 $n1 queuePos 0.5" + ""
#    code += '\n'+ linkwrite

#set udp [new Agent/UDP]
#$ns attach-agent $n0 $udp
#set null [new Agent/Null]
#$ns attach-agent $n1 $null
#$ns connect $udp $null
#$udp set fid_ 2

#    agentWrite=""
    #code += '\n'+ toupper(AgentNameList[0])
#    for l in range(NumAgents):
#        agentWrite+="set" + AgentNameList[0] + "[new Agent/UDP]" + "\n"
#        agentWrite+="$ns attach-agent" + " "+ "$" + str(LinkList[k][0]) + " "+ "$" +str( AgentNameList[0] ) + "\n"
#        agentWrite+="set null [new Agent/Null]" + "\n"
#        agentWrite+="$ns attach-agent" + " "+ "$" + str(LinkList[k][1]) + " "+ "$null" + "\n"
#        agentWrite+="$ns connect " + "$" + str(AgentNameList[0])  +  " $null"    + "\n" + "#$udp set fid_ 2" + "\n" 
#    
#    code += '\n'+ agentWrite
#
#        if element.tag == "node":
#            for line in tclfile1:
                #if element.text=="Two":
                #    code += '\n'+ line
#                if re.search("Node Creation Section Ends",line):                        
#                    toWriteline="\nset" + "  "
#                    toWriteline+=str(element.text)
#                    toWriteline+="  " + "[$ns node]" + "\n\n#Node Creation Section Ends \n"
#                    tclfile2.write(str(toWriteline
#                    break

#                code += '\n'+ toWriteline        
#                line.replace("#Node Creation Section Ends","Hello")
#                code += '\n'+ line

#                tclfile2.write(str(line
            
#            code += '\n'+ element.text
#    code += '\n'+ "set cbr [new Application/Traffic/CBR] \n $cbr attach-agent $udp \n $cbr set type_ CBR \n $cbr set packet_size_ 1000 \n $cbr set rate_ 1mb \n $cbr set random_ false"

#    code += '\n'+ " $ns at 0.1 \"$cbr start\" \n $ns at 4.5 \"$cbr stop\" \n $ns at 5.0 \"finish\" \n $ns run "
            
    #element = ET.XML(tree)
    #for subelement in element:
    #    code += '\n'+ subelement.text

if __name__ == "__main__":
    # Someone is launching this directly
    #init()    
    main()




#Create four nodes
#set n0 [$ns node]
#set n1 [$ns node]


#Create links between the nodes
#$ns duplex-link $n0 $n1 2Mb 10ms DropTail

#Set Queue Size of link (n2-n3) to 10
#$ns queue-limit $n0 $n1 10

#Give node position (for NAM)
#$ns duplex-link-op $n0 $n1 orient right-down

#Monitor the queue for link (n2-n3). (for NAM)
#$ns duplex-link-op $n0 $n1 queuePos 0.5




#Setup a UDP connection
#set udp [new Agent/UDP]
#$ns attach-agent $n0 $udp
#set null [new Agent/Null]
#$ns attach-agent $n1 $null
#$ns connect $udp $null
#$udp set fid_ 2

#Setup a CBR over UDP connection
#set cbr [new Application/Traffic/CBR]
#$cbr attach-agent $udp
#$cbr set type_ CBR
#$cbr set packet_size_ 1000
#$cbr set rate_ 1mb
#$cbr set random_ false


#Schedule events for the CBR and FTP agents
#$ns at 0.1 "$cbr start"
#$ns at 4.5 "$cbr stop"

#Call the finish procedure after 5 seconds of simulation time
#$ns at 5.0 "finish"

#code += '\n'+ CBR packet size and interval
#puts "CBR packet size = [$cbr set packet_size_]"
#puts "CBR interval = [$cbr set interval_]"

#Run the simulation
#$ns run

