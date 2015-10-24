import sublime
import sublime_plugin

class RenameTabLabelCommand(sublime_plugin.WindowCommand):
	def run(self, text='', **kwargs):
		self.tab_index = kwargs['index']
		self.tab_group = kwargs['group']
		self.show_input_panel('Rename Tab Label:', text)

	def on_done(self, text):
		if self.tab_group == -1 or self.tab_index == -1:
			self.window.active_view().set_name(text)
		else:
			self.window.views_in_group(self.tab_group)[self.tab_index].set_name(text)

	def show_input_panel(self, label, text):
		text = self.window.active_view().name();
		view = self.window.show_input_panel(label, text, self.on_done, None, None)