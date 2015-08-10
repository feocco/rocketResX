class RocketResX(object):
	"""Change the string 'ResX=1920' in $myDocuments_Location$\My Games\Rocket League\TAGame\Config\TASystemSettings.ini to 'ResX=3840'."""
	def __init__(self, arg):
		super(RocketResX, self).__init__()
		self.arg = arg
		
		# Edit the value below this line to your My Documents directory
		# Leave the quotation marks and the letter r prefix. DO NOT REMOVE
		MyDocuments = r'C:\Users\Joe\Documents'

		# Only edit if the My Games folder isn't in the My Documents directory. 
		FilePathSuffix = r'\My Games\Rocket League\TAGame\Config\TASystemSettings.ini'
		
		File_path = MyDocuments + FilePathSuffix
		Monitors1 = 'ResX=1920'
		Monitors2 = 'ResX=3840'
		

	def replace(self, file_path, pattern, subst):
		FileContents = open(file_path).read()
		if pattern in FileContents:
			print('Changing "{pattern}" to "{subst}"'.format(pattern, subst))
			FileContents = FileContents.replace(pattern, subst)
			f = open(file_path, 'w')
			f.write(FileContents)
			f.flush()
			f.close()
		else:
			print('An unexpected value has been entered for ResX or the parameter no longer exists.')


	def Monitor1(self):
		self.replace(self.file_path, Monitors2, Monitors1)


	def Monitors2(self):
		self.replace(self.file_path, Monitors1, Monitors2)