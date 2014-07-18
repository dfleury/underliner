import sublime, sublime_plugin


class UnderlinerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            text = self.view.substr(sel)
            new_text = text.replace(' ', '_')
            self.view.replace(edit, sel, new_text)
        sublime.status_message('Underlined successfully')
