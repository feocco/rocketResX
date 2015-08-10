class RocketResX(object):
	"""Change the string 'ResX=1920' in $myDocuments_Location$\My Games\Rocket League\TAGame\Config\TASystemSettings.ini to 'ResX=3840'."""
	def __init__(self):
		super(RocketResX, self).__init__()
		# Edit the value below this line to your My Documents directory
		# Leave the quotation marks and the letter r prefix. DO NOT REMOVE
		self.MyDocuments = r'C:\Users\Nate\Documents'

		# Only edit if the My Games folder isn't in the My Documents directory. 
		self.FilePathSuffix = r'\My Games\Rocket League\TAGame\Config\TASystemSettings.ini'
		
		self.ConfigFilePath = self.MyDocuments + self.FilePathSuffix
		self.Monitors1 = 'ResX=1920'
		self.Monitors2 = 'ResX=3840'
		

	def replace(self, FilePath, pattern, subst):
		FileContents = open(FilePath).read()
		if pattern in FileContents:
			print('Changing "{0}" to "{1}"'.format(pattern, subst))
			FileContents = FileContents.replace(pattern, subst)
			f = open(FilePath, 'w')
			f.write(FileContents)
			f.flush()
			f.close()
		else:
			print('An unexpected value has been entered for ResX or the parameter no longer exists.')


	def runtime(self):
		inp = input('Press 1 for 1 Monitor.\nPress 2 for 2 Monitors.\n')
		if inp == '1':
			self.replace(self.ConfigFilePath, self.Monitors2, self.Monitors1)
		else:
			self.replace(self.ConfigFilePath, self.Monitors1, self.Monitors2)

execute = RocketResX()
execute.runtime()
