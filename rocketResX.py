import os
import time

class RocketResX(object):
	"""Change the string 'ResX=1920' in $myDocuments_Location$\My Games\Rocket League\TAGame\Config\TASystemSettings.ini to 'ResX=3840'."""
	def __init__(self):
		super(RocketResX, self).__init__()
		# Edit the value below this line to your My Documents directory
		# Leave the quotation marks and the letter r prefix. DO NOT REMOVE
		self.MyDocuments = f = open('config.txt').read()[8:] + '\Rocket League\TAGame\Config\TASystemSettings.ini'

		# Only edit if the My Games folder isn't in the My Documents directory. 
		self.FilePathSuffix = r''
		
		self.ConfigFilePath = self.MyDocuments + self.FilePathSuffix
		self.Monitors1 = 'ResX=1920'
		self.Monitors2 = 'ResX=3840'
		

	def replace(self, FilePath, pattern, subst):
		""" Does an in-place substitution in a text file. Think find and replace. """
		FileContents = open(FilePath).read()
		if pattern in FileContents:
			print('Changing "{0}" to "{1}"'.format(pattern, subst))
			FileContents = FileContents.replace(pattern, subst)
			f = open(FilePath, 'w')
			f.write(FileContents)
			f.flush()
			f.close()
		elif subst in FileContents:
			# Break out of function
			return None
		else:
			print('An unexpected value has been entered for ResX or the parameter no longer exists.')


	def runtime(self):
		""" The container to execute the Class functions. """
		print('This script changes the X axis resolution value for Rocket League.\nThe game will launch after a value is entered.\n')
		inp = input('Enter 1 for 1 Monitor.\nEnter 2 for 2 Monitors.\nEnter C to cancel\n').lower()
		if inp == '1':
			self.replace(self.ConfigFilePath, self.Monitors2, self.Monitors1)
		elif inp == 'c':
			return None
		else:
			self.replace(self.ConfigFilePath, self.Monitors1, self.Monitors2)
		print('Starting Rocket League...')
		os.system(r'START /D "D:\STEAM GAMES\steamapps\common\rocketleague\Binaries\Win32\" "" /wait RocketLeague.exe')
		time.sleep(2)


execute = RocketResX()
execute.runtime()