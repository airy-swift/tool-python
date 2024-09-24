import csv, os
import pandas as pd
import numpy as np
import pyperclip


def copy_to_clipboard(text):
    pyperclip.copy(text)


def snake_to_lower_camel(word):
    parts = word.split('_')
    return parts[0] + "".join(x.title() for x in parts[1:])


class DfHandler:
    def __init__(self, csv_path):
        self.set_df_from_csv(csv_path)
        self.dfs = []

    def set_df_from_csv(self, csv_path):
        file_path = os.path.join(".", csv_path)
        print("file name:" + file_path)
        self.df = pd.read_csv(file_path)

    def fill_event_name_with_none(self):
        current_event_name = None
        for i, row in self.df.iterrows():
            if pd.notna(row['event_name']):
                current_event_name = row['event_name']  # イベントがある場合はそれを保持
            else:
                self.df.at[i, 'event_name'] = current_event_name  # イベントがない場合は前のイベントを入れる

    def thrash_df_by_event(self):
        # イベントごとにデータフレームを分割する
        current_df = pd.DataFrame(columns=self.df.columns)

        for i, row in self.df.iterrows():
            # 新しいイベントが出たとき、前のイベントのデータフレームを保存してリセット
            if i == 0 or self.df.at[i, 'event_name'] != self.df.at[i - 1, 'event_name']:
                if not current_df.empty:
                    self.dfs.append(current_df)
                current_df = pd.DataFrame(columns=self.df.columns)  # 新しいデータフレームを作成
            current_df = pd.concat([current_df, pd.DataFrame([row], columns=self.df.columns)], ignore_index=True)

        # 最後のイベントのデータフレームを追加
        self.dfs.append(current_df)


base_template = """
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/foundation.dart';

class FirebaseEventKind {{
  FirebaseEventKind._(this._eventName, this._params);
{defines}
  final String _eventName;

  final Map<String, dynamic> _params;

  void sendEvent() {{
    debugPrint('SEND FIREBASE EVENT: _eventName (parameter: _params)');
    FirebaseAnalytics.instance.logEvent(
      name: _eventName,
      parameters: Map<String, Object>.from(_params),
    );
  }}  
}}
"""
param_template = "{required}{type} {variable}"
map_template = "'{key}': {variable}"
each_template = """
  /// StartVersion: {version}
  /// About: {description}
  FirebaseEventKind.{camel}({params}) //
    : this._('{snake}', <String, dynamic>{{{map}}});
"""


def fill_template(template, values):
    return template.format(**values)


def get_param_value(df):
    params_df = df[['param_name', 'required', 'type', 'param_description']].dropna(subset=['param_name'])
    return params_df


def fill_parts_template(df):
    map_list = []
    param_list = []
    params = get_param_value(df)
    for param in params.iterrows():
        name = param[1]["param_name"]
        base_data = {
            "key": name,
            "required": "required " if param[1]["required"] else "",
            "type": param[1]["type"] + ("" if param[1]["required"] else "?"),
            "variable": snake_to_lower_camel(name)
        }
        map_filled = fill_template(map_template, base_data)
        map_list.append(map_filled)
        param_filled = fill_template(param_template, base_data)
        param_list.append(param_filled)
    return map_list, param_list


def fill_event(df, map_list, param_list):
    event_list = []
    for row in df.iterrows():
        event_name = row[1]["event_name"]
        maps = ', '.join(map_list)
        params = "" if not param_list else "{{{0}}}".format(', '.join(param_list))
        one = {
            "version": row[1]["start_version"],
            "description": row[1]["description"],
            "camel": snake_to_lower_camel(event_name),
            "snake": event_name,
            "map": maps,
            "params": params,
        }

        out = fill_template(each_template, one)
        return out

def generate_event_list(dfs):
    event_list = []
    for df in dfs:
        params = get_param_value(df)
        map_list, param_list = fill_parts_template(df)
        event = fill_event(df, map_list, param_list)
        event_list.append(event)
    return '\n'.join(event_list)


if __name__ == "__main__":
    handler = DfHandler('csv/sample.csv')
    handler.fill_event_name_with_none()
    handler.thrash_df_by_event()

    event_parts = generate_event_list(handler.dfs)
    result = fill_template(base_template, {"defines": event_parts})
    print(result)
    copy_to_clipboard(result)
