# シンプルなしょうもないツール達

## Firebase event generator
(((build_runnerとかで書けよ)))

base yamlファイル
```yaml
AUTH:
  description: 認証イベント
  group:
    sign_in:
      description: サインインした
      version: 1.0.0
      enabled: True
      parameters:
        - required: True
          type: String
          parameter_name: provider
    skip_auth:
      description: 認証をスキップした
      version: 1.0.0
      enabled: True
```

generated dart

```dart
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/cupertino.dart';

class FirebaseEventKind {
  FirebaseEventKind._(this._eventName, this._params);

  /// -------------------------------------------
  /// GROUP: AUTH -> 認証イベント
  /// -------------------------------------------

  /// StartVersion: 1.0.0
  /// About: サインインした
  FirebaseEventKind.signIn({required String provider}) //
    : this._('sign_in', <String, dynamic>{'provider': provider});

  /// StartVersion: 1.0.0
  /// About: 認証をスキップした
  FirebaseEventKind.skipAuth() //
    : this._('skip_auth', <String, dynamic>{});


  final String _eventName;

  final Map<String, dynamic> _params;

  void sendEvent() {
    debugPrint('SEND FIREBASE EVENT: _eventName (parameter: _params)');
    FirebaseAnalytics.instance.logEvent(
      name: _eventName,
      parameters: _params,
    );
  }  
}
```

## クオーテーションマーク添加マン
postman叩くときにジミーに不便だったから作った

base data
```text
    name: John,
    age : 30,
    color  :  red,
    size :small,
    gender :  male,
    hobby:running,
    type:animal,
    name:cat,
    brand:apple,
    price:1000,
    shape:square,
    length:10,
    country:japan,
    language:japanese,
    job:programmer,
    language:python,
    item:cpu,
    model:ryzen,
    material:wood,
    color:brown
```

generated data
```text
	"name":"John",
	"age":"30",
	"color":"red",
	"size":"small",
	"gender":"male",
	"hobby":"running",
	"type":"animal",
	"name":"cat",
	"brand":"apple",
	"price":"1000",
	"shape":"square",
	"length":"10",
	"country":"japan",
	"language":"japanese",
	"job":"programmer",
	"language":"python",
	"item":"cpu",
	"model":"ryzen",
	"material":"wood",
	"color":"brown"
```