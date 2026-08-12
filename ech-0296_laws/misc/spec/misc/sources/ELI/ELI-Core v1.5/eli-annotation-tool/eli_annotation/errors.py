# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl


class ELIError(Exception):
    def __init__(self, title, message, context=""):
        self.title = title
        self.context = context
        super().__init__(message)

    @property
    def message(self):
        return super().__str__()

    def to_json(self):
        return {"title": self.title,
                "title_suffix": self.context,
                "details": self.message}

    def __str__(self):
        if self.context != "":
            return "*** {0}\n{1}".format(self.context, self.message)
        else:
            return self.message


class ConversionError(ELIError):
    pass

class IncorrectResource(ELIError):
    pass



class ConversionWarnings:
    def __init__(self, title, context):
        self.title = title
        self.context = context
        self.messages = []

    def __len__(self):
        return len(self.messages)

    def log(self, message):
        self.messages.append(message)

    @property
    def message(self):
        return "\n".join(self.messages)

    def to_json(self):
        return {"title": self.title,
                "title_suffix": self.context,
                "details": self.message}

    def __str__(self):
        if self.context != "":
            return "*** {0}\n{1}".format(self.context, self.message)
        else:
            return self.message
