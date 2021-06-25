import sublime_plugin
import os


# plugin mainly revolves around the plugin idea of file_navigationusing via input_handlers. 


class file_system_inputhandler(sublime_plugin.ListInputHandler):

	# a list input handler that is maintaining the inputs in input handlers ,basically
	# taking selected list that has to be listed in the input handlers. 
	# `file_system_inputhandler(argument)` since 'argument' is list defined by init_method

	def __init__(self,files_to_be_listed):
		self.files_to_be_listed=files_to_be_listed		

	def name(self):
		return 'name'

	def preview(self, arg):
		# method to get a preview in the bottom of input panel give sout the preview
		# in return (~~description~~) method `description` being the file that has on overlay

		return f'you selected: {arg}'



	def list_items(self):
		return ['~~']+self.files_to_be_listed

	def next_input(self, args):
		global file_path

		# a method to get functionality of selecting items after the main input listener
		# given the output.  
		# basically consists of 2 components one is to get into file_navigation opening file 
		# if residing in it via `file_handlerCommand()` via sublimeAPI method `run_command()`
		# and the other part bring back the input_handler to few steps back a step.

		# operation 1 includes finding `~~`if in selected  and if returns `True` 
		# uses its file_path to get back to the root ``ListInputHandler()``

	# -----------------------------------------------------------------------------------

		if args['name']=='~~':
			if file_path != 'C://Users//Ayoush//AppData//Roaming//Sublime Text//Packages':
				file_path=file_path.split('//')		
				file_path.pop(len(file_path)-1)
				file_path='//'.join(file_path)
				return file_system_inputhandler(os.listdir(file_path))

			else:
				return file_system_inputhandler(os.listdir(file_path))
		# operation 2 

		else:
			try:
				file_path=file_path+'//'+args['name']
				iterated_list=os.listdir(file_path)
				return file_system_inputhandler(iterated_list)

			except NotADirectoryError:
				return None

	# ----------------------------------------------------------------------------------------



class file_handlerCommand(sublime_plugin.WindowCommand):
	def run(self,name):
		global file_path

		# window command dealing with taking file_path from `next_input()` method 
		# converting the '//' to '/' since sublimeAPI recognize appopriate_filetype 
		# only when founds  '/' in the file_name.

		if name != '~~':
			file_opened=str(file_path).replace('//','/')
			self.window.run_command('open_file',{'file': file_opened})

	def input(self, args):

		# this sort of method `input`in `WindowCommand(file_handler)` is the first 
		# instance giving the file_system_inputhandler()  for original filesystem 
		# after the instance makes the call the `next_input` method takes over the 

		global file_path
		file_path='://Users//Ayoush//AppData//Roaming//Sublime Text//Packages'
		begin_list=os.listdir(file_path)
		return file_system_inputhandler(begin_list)
	

