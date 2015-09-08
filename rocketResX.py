import time
import subprocess

class RocketResX(object):
	"""Change the string 'ResX=1920' in $myDocuments_Location$\My Games\Rocket League\TAGame\Config\TASystemSettings.ini to 'ResX=3840'."""
	def __init__(self):
		super(RocketResX, self).__init__()
		self.ConfigFilePath = open('config.txt').readlines()[0][8:-1] + '\Rocket League\TAGame\Config\TASystemSettings.ini'
		self.Monitors1 = 'ResX=1920'
		self.Monitors2 = 'ResX=3840'
		

	def replace(self, FilePath, pattern, subst):
		""" Does an in-place substitution in a text file. Think find and replace. """
		FileContents = open(FilePath).read()

		if pattern in FileContents:
			FileContents = FileContents.replace(pattern, subst)
			f = open(FilePath, 'w')
			f.write(FileContents)
			f.flush()
			f.close()


	def runtime(self, inp):
		""" The container to execute the Class functions. """
		path = open('config.txt').readlines()[1][11:] + '\\common\\rocketleague\\Binaries\\Win32\\RocketLeague.exe'

		if inp == 1:
			self.replace(self.ConfigFilePath, self.Monitors2, self.Monitors1)
		elif inp == 2:
			self.replace(self.ConfigFilePath, self.Monitors1, self.Monitors2)
		else:
			return None

		process = subprocess.call(path)
		time.sleep(10)