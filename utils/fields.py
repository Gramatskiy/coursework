from rest_framework import serializers


class ChoicesField(serializers.ChoiceField):
    def __init__(self, choices, **kwargs):
        self._choices_tuple = choices
        super(ChoicesField, self).__init__(choices, **kwargs)

    def to_representation(self, obj):
        return [item for item in self._choices_tuple if item[0] == obj][0]

    def to_internal_value(self, data):
        try:
            return [item for item in self._choices_tuple if item[0] == data][0][0]
        except IndexError:
            self.fail('invalid_choice', input=data)
