# Network Mapper

Realizați un utilitar care să primească o clasă de IP-uri în format CIDR și să afișeze nodurile
din rețea care sunt online, cât și porturile care acceptă conexiuni (se vor testa doar cele mai
utilizate porturi, sau cele dintr-o listă dată la linia de comandă).

INPUT: network_mapper.py 192.168.0.0/24 [port1, port2, ...]

OUTPUT: 192.168.0.1:80 (HTTP)
:443 (HTTPS)
192.168.0.105:445 (SMB)
