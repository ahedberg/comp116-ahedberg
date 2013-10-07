require 'packetfu'

def write_alert(incident_number, attack, source_ip, protocol)
  puts "#{incident_number}. ALERT: #{attack} is detected from #{source_ip} (#{protocol})!"
end

stream = PacketFu::Capture.new(:start => true, :iface => 'lo', :promisc => true)
alert_num = 0

stream.stream.each do |raw|
  packet = PacketFu::Packet.parse(packet = raw)
  
  if (packet.kind_of? PacketFu::TCPPacket)
    flags = packet.tcp_flags

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
    if (packet.payload.include? "Nmap")
      alert_num += 1
      write_alert(alert_num, "Nmap scan", packet.ip_saddr, packet.proto()[-1])
    end
  end

  if (packet.payload.include? "PASS")
    alert_num += 1
    write_alert(alert_num, "Password leakage", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for in-the-clear credit card number leakage
  if (packet.payload.match(/\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}/))
    alert_num += 1
    write_alert(alert_num, "Credit card number in the clear", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for cross-site scripting
  if (packet.payload.include? "<script>")
    if (packet.payload.include? "alert")
      alert_num += 1
      write_alert(alert_num, "XSS", packet.ip_saddr, packet.proto()[-1])
    end
  end

end
