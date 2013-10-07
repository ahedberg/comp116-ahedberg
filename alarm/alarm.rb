require 'packetfu'

def write_alert(incident_number, attack, source_ip, protocol)
  puts "#{incident_number}. ALERT: #{attack} is detected from #{source_ip} (#{protocol})!"
end

stream = PacketFu::Capture.new(:start => true, :iface => 'lo', :promisc => true)
alert_num = 0

stream.stream.each do |raw|
  packet = PacketFu::Packet.parse(packet = raw)
  
  payload = packet.eth_header.body  # in string form when not encrypted

  begin
    # Check for nmap scans - Non-TCP packets will throw errors here
    flags = packet.tcp_flags

    if (!(flags.urg || flags.ack || flags.psh || flags.rst || flags.syn || flags.fin))
      # Found a NULL scan
      alert_num += 1
      write_alert(alert_num, "NULL scan", packet.ip_saddr, packet.proto()[-1])

    else if ((flags.urg == 1) && (flags.psh == 1) && (flags.fin == 1))
      # Found an Xmas scan
      alert_num += 1
      write_alert(alert_num, "Xmas scan", packet.ip_saddr, packet.proto()[-1])

    end
    
    # Check for other nmap scans
    if (payload.include? "nmap")
      alert_num += 1
      write_alert(alert_num, "Nmap scan", packet.ip_saddr, packet.proto()[-1])
    end
    if (payload.include? "NMAP")
      alert_num += 1
      write_alert(alert_num, "Nmap scan", packet.ip_saddr, packet.proto()[-1])
    end
    if (payload.include? "Nmap")
      alert_num += 1
      write_alert(alert_num, "Nmap scan", packet.ip_saddr, packet.proto()[-1])
    end
  end

  rescue NoMethodError
  end


  # Check for in-the-clear password leakage
  if (payload.include? "PASS")
    alert_num += 1
    write_alert(alert_num, "Password leakage", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for in-the-clear credit card number leakage
  if (/\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}/.match(payload))
    alert_num += 1
    write_alert(alert_num, "Credit card number in the clear", packet.ip_saddr, packet.proto()[-1])
  end

  # Check for cross-site scripting
  if (payload.include? "<script>")
    alert_num += 1
    write_alert(alert_num, "XSS", packet.ip_saddr, packet.proto()[-1])
  end
end

