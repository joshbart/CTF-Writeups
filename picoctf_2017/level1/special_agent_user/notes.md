# Challenge: Special Agent User
## Clue Text:
We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using.  Perhaps this information is located in a network packet capture we took: [data.pcap][data.pcap]. Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)

## 14 Oct 2018
**0448** Since I just finished Digital Camouflage, I've got the juices flowing.  But, it's really early, so I'm going to go sleep some more.

**1036** I downloaded the pcap file and opened it up in Wireshark.  It's again a single client `10.0.0.5` talking to a server `10.0.0.1`.  There were a number of UDP requests with ICMP responses.  These were incoherent, so I skipped them.  I also found a couple of TCP streams containing basic HTTP traffic.  The User-Agent reported in both of the requests I saw was `Wget/1.16`.  I entered that, but it reports as wrong.  Taking a look at the side view I noticed there were quite a few packets in the capture, so I filtered them down to just HTTP requests from the client using `ip.src == 10.0.0.5 && http`.  This left seven remaining packets, all but one of which contained Wget as the User-Agent.  The User-Agents reported in this last packet were: Mozilla/5.0, AppleWebKit/537.36, Chrome/36.0.1985, and Safari/537.36.  Chrome seemed like the most likely candidate, so I started there.  Success!
