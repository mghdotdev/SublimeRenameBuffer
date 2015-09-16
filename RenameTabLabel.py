import sublime
import sublime_plugin

class RenameTabLabelCommand(sublime_plugin.WindowCommand):
	def run(self, text='', execute=False):
		# if not self.window.active_view():
		# 	return
		self.show_input_panel('Rename Tab Label:', text)

	def on_done(self, text):
		self.window.active_view().set_name(text)

	def show_input_panel(self, label, text):
		print('label')
		view = self.window.show_input_panel(label, text, self.on_done, None, None)
		# settings = view.settings()
		# settings.set('is_widget', False)
		# settings.set('gutter', False)
		# settings.set('rulers', [])
		# settings.set('spell_check', False)
		# settings.set('word_wrap', False)
		# settings.set('draw_minimap_border', False)
		# settings.set('draw_indent_guides', False)
		# settings.set('highlight_line', False)
		# settings.set('line_padding_top', 0)
		# settings.set('line_padding_bottom', 0)
		# settings.set('auto_complete', False)