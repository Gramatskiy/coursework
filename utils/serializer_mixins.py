from rest_framework import serializers
from rest_framework.utils.field_mapping import get_nested_relation_kwargs


# class to include, exclude fields set depth on model serializer, typically when use serializer as field
class SerializerFieldsDepthMixin:
    include_arg_name = 'include_fields'
    exclude_atg_name = 'exclude_fields'
    delimiter = ','

    def __init__(self, *args, **kwargs):
        include_field_names = kwargs.pop('include_fields', None)
        exclude_field_names = kwargs.pop('exclude_fields', None)
        depth = kwargs.pop('depth', None)
        # set appropriate depth
        if depth:
            try:
                depth = int(depth)
                if depth < 0:
                    raise TypeError  # only 0+
                self.Meta.depth = depth
            except TypeError:
                pass

        super(SerializerFieldsDepthMixin, self).__init__(*args, **kwargs)
        try:
            request = self.context['request']
            method = request.method

            if method != 'GET':
                return
        except (AttributeError, TypeError, KeyError):
            # The serializer was not initialized with request context.
            pass

        if include_field_names:
            include_field_names = set(include_field_names.split(self.delimiter))
        if exclude_field_names:
            exclude_field_names = set(exclude_field_names.split(self.delimiter))

        if not include_field_names and not exclude_field_names:
            # No user fields filtering was requested, we have nothing to do here.
            return

        serializer_field_names = set(self.fields)
        fields_to_drop = set()
        if exclude_field_names:
            fields_to_drop = serializer_field_names & exclude_field_names
        if include_field_names:
            fields_to_drop |= serializer_field_names - include_field_names

        for field in fields_to_drop:
            self.fields.pop(field, None)


#  mixin to include, exclude specified fields from get params
class QueryFieldsDepthMixin:
    # If using Django filters in the API, these labels mustn't conflict with any model field names.
    include_arg_name = 'fields'
    exclude_arg_name = 'fields!'

    # Split field names by this string.  It doesn't necessarily have to be a single character.
    # Avoid RFC 1738 reserved characters i.e. ';', '/', '?', ':', '@', '=' and '&'
    delimiter = ','

    def __init__(self, *args, **kwargs):
        super(QueryFieldsDepthMixin, self).__init__(*args, **kwargs)

        try:
            request = kwargs['context']['request']
            method = request.method
        except (AttributeError, TypeError, KeyError):
            # The serializer was not initialized with request context.
            super(QueryFieldsDepthMixin, self).__init__(*args, **kwargs)
            return

        if method != 'GET':
            super(QueryFieldsDepthMixin, self).__init__(*args, **kwargs)
            return

        try:
            query_params = request.query_params
        except AttributeError:
            # DRF 2
            query_params = getattr(request, 'QUERY_PARAMS', request.GET)
        includes = query_params.getlist(self.include_arg_name)
        include_field_names = {name for names in includes for name in names.split(self.delimiter) if name}

        excludes = query_params.getlist(self.exclude_arg_name)
        exclude_field_names = {name for names in excludes for name in names.split(self.delimiter) if name}

        if not include_field_names and not exclude_field_names:
            # No user fields filtering was requested, we have nothing to do here.
            return

        serializer_field_names = set(self.fields)

        fields_to_drop = serializer_field_names & exclude_field_names
        if include_field_names:
            fields_to_drop |= serializer_field_names - include_field_names

        for field in fields_to_drop:
            self.fields.pop(field)




class FieldsDepthModelSerializer(SerializerFieldsDepthMixin, serializers.ModelSerializer):
    pass


class QueryModelSerializer(QueryFieldsDepthMixin, serializers.ModelSerializer):
    pass


class QueryFieldsDepthModelSerializer(QueryFieldsDepthMixin, SerializerFieldsDepthMixin, serializers.ModelSerializer):
    pass
