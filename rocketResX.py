from tempfile import mkstemp
from shutil import move
from os import remove, close

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
		#Create temp file
		fh, abs_path = mkstemp()
		with open(abs_path, 'w') as new_file:
			with open(file_path) as old_file:
				for line in old_file:
					new_file.write(line.replace(pattern, subst))
		close(fh)
		#Remove original file
		remove(file_path)
		#Move new file
		move(abs_path, file_path)


	def Monitor1(self):
		self.replace(self.file_path, Monitors2, Monitors1)


	def Monitors2(self):
		self.replace(self.file_path, Monitors1, Monitors2)