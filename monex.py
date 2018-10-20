import shodanSearch
import Scanner
api_key=""
s=shodanSearch.shodan(api_key)
#s.searchHost('82.223.200.60', 'text')
#s.searchHost('82.223.200.60', 'html')
#s.searchQuery('net:82.223.200.0/24', "text")
#s.monHost('82.223.200.60', [80, 22])
s.searchQuery('net:82.223.200.0/24', "multiHTML")
