.. _{{ objname }}:

{{ fullname | escape | underline}}

.. automodule:: {{ fullname | module | class | function}}
    :members:
    :undoc-members:
    :inherited_members:
    :show-inheritance:
    :currentmodule:
    :recursive:

Description
-----------

.. automodule:: {{ fullname | escape }}

{% if classes %}
Classes
-------
.. autosummary:
    :toctree: _autosummary

    {% for class in classes %}
        {{ class }}
    {% endfor %}

{% endif %}

{% if functions %}
Functions
---------
.. autosummary:
    :toctree: _autosummary

    {% for function in functions %}
        {{ function }}
    {% endfor %}

{% endif %}