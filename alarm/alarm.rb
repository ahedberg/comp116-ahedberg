require 'packetfu'

def write_alert(incident_number, attack, source_ip, protocol)
  puts "#{incident_number}. ALERT: #{attack} is detected from #{source_ip} (#{protocol})!"
end

stream = PacketFu::Capture.new(:start => true, :iface => 'lo', :promisc => true)
alert_num = 0

stream.stream.each do |raw|
  packet = PacketFu::Packet.parse(packet = raw)
  protocol = "Unknown"  # for default

  # determine type of packer we're dealing with
  if (packet.kind_of? PacketFu::TCPPacket)
    flags = packet.tcp_flags
    protocol = "TCP"
  elsif (packet.kind_of? PacketFu::IPPacket)
      protocol = "HTTP"
  elsif (packet.kind_of? PacketFu::ARPPacket)
    protocol = "ARP"
  elsif (packet.kind_of? PacketFu::IPv6Packet)
    protocol = "IPv6"
  elsif (packet.kind_of? PacketFu::HSRPPacket)
    protocol = "HSRP"
  elsif (packet.kind_of? PacketFu::ICMPPacket)
    protocol = "ICMP"
  elsif (packet.kind_of? PacketFu::LLDPPacket)
    protocol = "LLDP"
  elsif (packet.kind_of? PacketFu::UDPPacket)
    protocol = "UDP"
  elsif (packet.kind_of? PacketFu::EthPacket)
    protocol = "Eth"
  end

  if (protocol == "TCP")
    # Check for NULL scans
    if ((flags.urg == 0) && (flags.ack == 0) && (flags.psh == 0) && (flags.rst == 0) && (flags.syn == 0) && (flags.fin) == 0)
      alert_num += 1
      write_alert(alert_num, "NULL scan", packet.ip_saddr, packet.proto()[-1])
    end

    # Check for Xmas tree scans
    if ((flags.urg == 1) && (flags.psh == 1) && (flags.fin == 1))
      alert_num += 1
      write_alert(alert_num, "Xmas scan", packet.ip_saddr, packet.proto()[-1])
    end
    
    # Check for other nmap scans
    if (packet.payload.index(/nmap/i) != nil)
      alert_num += 1
      write_alert(alert_num, "Nmap scan", packet.ip_saddr, packet.proto()[-1])
    end
  end

  if (packet.payload.index("PASS") != nil)
    alert_num += 1
    write_alert(alert_num, "Password leakage", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for in-the-clear credit card number leakage
  if (packet.payload.index(/\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}/) != nil)
    alert_num += 1
    write_alert(alert_num, "Credit card number in the clear", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for cross-site scripting
  if (packet.payload.index(/<script>\s*(alert|window.location)/i) != nil)
    alert_num += 1
    write_alert(alert_num, "XSS", packet.ip_saddr, packet.proto()[-1])
  end

  if (packet.payload.index(/<script>/i) != nil && packet.payload.index(/\s*(GET|POST)/) != nil)
    alert_num += 1
    write_alert(alert_num, "XSS", packet.ip_addr, packet.proto()[-1])
  end
end
