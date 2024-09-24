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

## Firebase event generator(csv version)
(((build_runnerとかで書けよ)))

base csvファイル
```csv
event_name,description,start_version,finish_version,param_name,required,type,param_description
shop_purchase,購入ボタン押下,1.0.0,2.0.0,item_ids,TRUE,List<String>,購入したアイテムidリスト
,,,,amount,TRUE,int,購入金額
,,,,coupon_id,FALSE,String,クーポンid
open_drawer,ドロワー開いた,1.0.0,
open_mypage,マイページ開いた,1.0.0,,follower_count,TRUE,int,フォロワー数
```


generated dart

```dart

import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/foundation.dart';

class FirebaseEventKind {
  FirebaseEventKind._(this._eventName, this._params);

  /// StartVersion: 1.0.0
  /// About: 購入ボタン押下
  FirebaseEventKind.shopPurchase({required List<String> itemIds, required int amount, String? couponId}) //
    : this._('shop_purchase', <String, dynamic>{'item_ids': itemIds, 'amount': amount, 'coupon_id': couponId});


  /// StartVersion: 1.0.0
  /// About: ドロワー開いた
  FirebaseEventKind.openDrawer() //
    : this._('open_drawer', <String, dynamic>{});


  /// StartVersion: 1.0.0
  /// About: マイページ開いた
  FirebaseEventKind.openMypage({required int followerCount}) //
    : this._('open_mypage', <String, dynamic>{'follower_count': followerCount});

  final String _eventName;

  final Map<String, dynamic> _params;

  void sendEvent() {
    debugPrint('SEND FIREBASE EVENT: _eventName (parameter: _params)');
    FirebaseAnalytics.instance.logEvent(
      name: _eventName,
      parameters: Map<String, Object>.from(_params),
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
