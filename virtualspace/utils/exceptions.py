# Copyright (c) 2017 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.


class ValidationError(Exception):
    def __init__(self, *args, **kwargs):
        self.error_dict = kwargs.pop('error_dict')
        super(ValidationError, self).__init__(*args, **kwargs)
