import sublime 
import sublime_plugin
import os 


class file_handler(sublime_plugin.ListInputHandler):

	def __init__(self,listed_file):
		self.listed_file=listed_file

	def name(self):
		return 'name'

	def placeholder(self):
		return 'file_to_be_selected'

	def list_items(self):
		return self.listed_file

	def preview(self, arg):
		return f'you selected: {arg}'

	def next_input(self, args):
		try:
			global file_path
			file_path=file_path+'//'+args['name']
			print(file_path)
			return file_handler(os.listdir(file_path))
		except NotADirectoryError:
			print(file_path,'is opened')



class file_handling_proCommand(sublime_plugin.WindowCommand):
	def run(self,name):
		global file_path
		openi=file_path
		openi=openi.replace('//','/')
		print('->>>',openi)
		self.window.run_command('open_file',{'file':openi})


	def input(self, args):
		global file_path
		file_path='D://sublime_text_build_4106_x64//Data'
		main_list=os.listdir(file_path)
		return file_handler(main_list)


