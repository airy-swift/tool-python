import parse_yaml
import pyperclip


def copy_to_clipboard(text):
    pyperclip.copy(text)


base_template = """
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/cupertino.dart';

class FirebaseEventKind {{
  FirebaseEventKind._(this._eventName, this._params);
{defines}
  final String _eventName;

  final Map<String, dynamic> _params;

  void sendEvent() {{
    debugPrint('SEND FIREBASE EVENT: $_eventName (parameter: $_params)');
    FirebaseAnalytics.instance.logEvent(
      name: _eventName,
      parameters: _params,
    );
  }}  
}}
"""

group_template = """
  /// -------------------------------------------
  /// GROUP: {group} -> {description}
  /// -------------------------------------------
{defined}
"""

each_template = """
  /// StartVersion: {version}
  /// About: {description}
  FirebaseEventKind.{camel}({params}) //
    : this._('{snake}', <String, dynamic>{{{map}}});
"""

param_template = "{required}{type} {variable}"
map_template = "'{key}': {variable}"


def fill_template(template, values):
    return template.format(**values)


def snake_to_lower_camel(word):
    parts = word.split('_')
    return parts[0] + "".join(x.title() for x in parts[1:])


def apply_parameters_to_template(parameters):
    params = value["parameters"] if 'parameters' in parameters else None
    map_list = []
    param_list = []

    if params is None:
        return "", ""
    if len(params) == 0:
        return "", ""

    for param in params:
        if "parameter_name" not in param:
            return "", ""

        name = param["parameter_name"]
        base_data = {
            "key": name,
            "required": "required " if param["required"] else "",
            "type": param["type"],
            "variable": snake_to_lower_camel(name)
        }
        map_filled = fill_template(map_template, base_data)
        map_list.append(map_filled)
        param_filled = fill_template(param_template, base_data)
        param_list.append(param_filled)
    return ', '.join(map_list), "{{{0}}}".format(', '.join(param_list))


if __name__ == "__main__":
    dictionary = parse_yaml.parse()
    filled_list = []
    for group in dictionary:
        group_list = []
        print(group)
        for top_key in dictionary[group]["group"]:
            print(top_key)
            value = dictionary[group]["group"][top_key]
            maps, params = apply_parameters_to_template(value)
            if not value["enabled"]:
                continue
            one = {
                "version": value["version"],
                "description": value["description"],
                "camel": snake_to_lower_camel(top_key),
                "snake": top_key,
                "map": maps,
                "params": params,
            }
            filled = fill_template(each_template, one)
            group_list.append(filled)
        group_filled = fill_template(group_template, {
            "group": group,
            "description": dictionary[group]["description"],
            "defined": ''.join(group_list)
        })
        filled_list.append(group_filled)

    result = fill_template(base_template, {"defines": ''.join(filled_list)})
    print(result)
    copy_to_clipboard(result)
    print("... and copied!!")
