import sublime
import sublime_plugin


class UnderlinerCommand(sublime_plugin.TextCommand):

    replacements = {
        ' ': '_',
        '_': ' ',
    }

    names = {
        ' ': 'spaces',
        '_': 'underlines',
    }

    def run(self, edit):
        sels = self.view.sel()
        replace_char = self.get_prevailing_char(sels)
        for sel in sels:
            text = self.view.substr(sel)
            new_text = text.replace(
                replace_char,
                self.replacements[replace_char])
            self.view.replace(edit, sel, new_text)

        replaced_char = self.names[replace_char]
        unreplaced_chard = self.names[self.replacements[replace_char]]
        message = 'It was found more %s than %s, so it was replaced'
        sublime.status_message(message % (replaced_char, unreplaced_chard))

    def get_prevailing_char(self, sels):
        '''decide which char will be replaced'''
        all_text = ''
        for sel in sels:
            all_text += self.view.substr(sel)
        spaces_count = all_text.count(' ')
        underlines_count = all_text.count('_')
        if spaces_count > underlines_count:
            return ' '
        else:
            return '_'
