# rocketResX
# Description: 
	Change the string 'ResX=1920' in %MyDocuments_Location%\My Games\Rocket League\TAGame\Config\TASystemSettings.ini to 'ResX=3840'.

# Pre-req for creating exe:
	# Install py2exe and python

# Steps to set up:
	# Edit rocketResX.py with text editor
	# Change value of the MyDocuments variable
		# self.MyDocuments = r'C:\Users\Joe\Documents'
		# Example Change to match Jerry's computer:
			# self.MyDocuments = r'C:\Users\Jerrys_Username\Documents'
	# Save rocketResX.py

	# Open cmd and run:
		python py2exeSetup.py py2exe