require 'packetfu'

stream = PacketFu::Capture.new(:start => true, :iface => 'eth0', 
                               :promisc => true)

stream.stream.each do |raw|
  # ...
end
