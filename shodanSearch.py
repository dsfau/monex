import requests
import time
import output
import json
url="https://api.shodan.io/shodan/"
class shodan:
	def __init__(self, api_key):
		self.api = api_key
		self.startTime=time.strftime('%c --- %X')

	def __uniSearchHost(self, host, openports, outformat):
		p = {'key': self.api}
		results = requests.get(url + "host/" + host, params=p)
		if results.status_code == 200:
			self.endTime = time.strftime('%c --- %X')
			out = output.Output(format=outformat)
			if outformat=="monitor":
				out.output(results=results.text, obj=self, openports=openports)
			elif outformat == "multiHTML":
				return results.text
			else:
				out.output(results=results.text, obj=self)

	def searchHost(self, host, outformat):
		self.__uniSearchHost(host=host, openports=None, outformat=outformat)

	def searchQuery(self, query, outformat):
		p={'key': self.api, 'query': '{0}'.format(query)}
		results = requests.get(url+"host/search", params=p)
		if results.status_code == 200:
			if outformat=="multiHTML":
				self.hosts = []
				for host in json.loads(results.text)["matches"]:
					self.hosts.append(self.__uniSearchHost(host=host['ip_str'], outformat=outformat, openports=None))
				out = output.Output(format=outformat)
				out.outMultiHTML(self, query.replace(":", "-"))
			else:
				for host in json.loads(results.text)["matches"]:
					self.searchHost(host['ip_str'], outformat)

	def monHost(self, host, openports):
		self.__uniSearchHost(host=host, openports=openports, outformat='monitor')
