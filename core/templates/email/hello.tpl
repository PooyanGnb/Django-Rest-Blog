{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activation
{% endblock %}

{% block body %}

{% endblock %}

{% block html %}
{{token}}
{% endblock %}