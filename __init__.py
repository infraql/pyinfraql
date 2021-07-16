import sys, subprocess, platform

class InfraQL:
	def __init__(self, **kwargs):
		plat = platform.system()
		defaultbin = r'infraql'
		if plat == 'Windows':
			defaultbin = r'infraql.exe'
		self.exe = kwargs.get('exe', defaultbin)
		self.keyfilepath = kwargs.get('keyfilepath')
		self.dbfilepath = kwargs.get('dbfilepath')
		self.params = ['exec', '--keyfilepath', self.keyfilepath, '--output', 'json']
		if self.dbfilepath is not None:
			self.params.append('--dbfilepath')
			self.params.append(self.dbfilepath)
			
	def execute(self, query):
		local_params = self.params
		local_params.insert(1, query)
		try:
			iqlPopen = subprocess.Popen([self.exe] + local_params,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = iqlPopen.stdout.read()
			iqlPopen.terminate()
		except:
			e = sys.exc_info()[0]
			print("ERROR %s %s" % (str(e), e.__doc__))
			output = None
		return output