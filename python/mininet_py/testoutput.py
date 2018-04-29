import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
turn=0
def getTheTime():  #fuction to create a timestamp
  then = "[%s-%s-%s" %(str(flock.tm_year),str(flock.tm_mon),str(flock.tm_mday))
  if int(flock.tm_hour)<10:
  if int(flock.tm_min)<10:
    mins = str(flock.tm_min)
  then +="]%s.%s.%s" % (hrs,mins,secs)
  return then
def _timer_func ():
  global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid,turn
  #print getTheTime(), "sent the port stats request to s1_dpid"
  if turn==0:
      msg.command=of.OFPFC_MODIFY_STRICT
      msg.match.nw_dst = "10.0.0.4"
      msg.actions.append(of.ofp_action_output(port = 5))
      core.openflow.getConnection(s1_dpid).send(msg)
      turn=1
      return
  if turn==1:
      msg.command=of.OFPFC_MODIFY_STRICT
      msg.match.nw_dst = "10.0.0.4"
      msg.actions.append(of.ofp_action_output(port = 6))
      core.openflow.getConnection(s1_dpid).send(msg)
      turn=2
      return
  if turn==2:
      msg.command=of.OFPFC_MODIFY_STRICT
      msg.match.nw_dst = "10.0.0.4"
      msg.actions.append(of.ofp_action_output(port = 4))
      turn=0
      return
def _handle_portstats_received (event):
  if event.connection.dpid==s1_dpid:
    for f in event.stats:
      if int(f.port_no)<65534:
        if f.port_no==1:
        if f.port_no==4:
        if f.port_no==5:
        if f.port_no==6:
     for f in event.stats:
       if int(f.port_no)<65534:
         if f.port_no==1:
  if event.connection.dpid==s3_dpid:
     for f in event.stats:
       if int(f.port_no)<65534:
         if f.port_no==1:
  if event.connection.dpid==s4_dpid:
     for f in event.stats:
       if int(f.port_no)<65534:
         if f.port_no==1:
def _handle_ConnectionUp (event):
  print "ConnectionUp: ",dpidToStr(event.connection.dpid)
  #remember the connection dpid for switch
  for m in event.connection.features.ports:
    if m.name == "s1-eth1":
      s1_dpid = event.connection.dpid
      print "s1_dpid=", s1_dpid
    elif m.name == "s2-eth1":
      s2_dpid = event.connection.dpid
      print "s2_dpid=", s2_dpid
    elif m.name == "s3-eth1":
      s3_dpid = event.connection.dpid
    elif m.name == "s4-eth1":
      s4_dpid = event.connection.dpid
      print "s4_dpid=", s4_dpid
    elif m.name == "s5-eth1":
      s5_dpid = event.connection.dpid
      print "s5_dpid=", s5_dpid
  if s1_dpid<>0 and s2_dpid<>0 and s3_dpid<>0 and s4_dpid<>0:
    Timer(1, _timer_func, recurring=True)
def _handle_PacketIn(event):
  packet=event.parsed
  if event.connection.dpid==s1_dpid:
     a=packet.find('arp')
     if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=4))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=5))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=6))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.1"
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.2"
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.3"
     msg.actions.append(of.ofp_action_output(port = 3))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.4"
     msg.actions.append(of.ofp_action_output(port = 4))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.5"
     msg.actions.append(of.ofp_action_output(port = 5))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.6"
     msg.actions.append(of.ofp_action_output(port = 6))
     event.connection.send(msg)
  elif event.connection.dpid==s2_dpid:
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
  elif event.connection.dpid==s3_dpid:
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
  elif event.connection.dpid==s4_dpid:
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 1
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
     msg.match.in_port = 2
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
  elif event.connection.dpid==s5_dpid:
     a=packet.find('arp')
     if a and a.protodst=="10.0.0.4":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=4))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.5":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=5))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.6":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=6))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.1":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=1))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.2":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=2))
       event.connection.send(msg)
     if a and a.protodst=="10.0.0.3":
       msg = of.ofp_packet_out(data=event.ofp)
       msg.actions.append(of.ofp_action_output(port=3))
       event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.1"
     msg.actions.append(of.ofp_action_output(port = 1))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.2"
     msg.actions.append(of.ofp_action_output(port = 2))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.3"
     msg.actions.append(of.ofp_action_output(port = 3))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.4"
     msg.actions.append(of.ofp_action_output(port = 4))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.5"
     msg.actions.append(of.ofp_action_output(port = 5))
     event.connection.send(msg)
     msg.match.nw_dst = "10.0.0.6"
     msg.actions.append(of.ofp_action_output(port = 6))
     event.connection.send(msg)
def launch ():
  core.openflow.addListenerByName("PortStatsReceived",_handle_portstats_received)
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
  core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
