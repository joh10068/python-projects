import 'package:flutter/cupertino.dart';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _text = 'Scan Barcode';
  String inputStr = "";

  void onEventKey(RawKeyEvent event) async {
    if (event is RawKeyDownEvent && event.character != null) {
      inputStr = inputStr + event.character!;
      print(inputStr);
      setState(() {
        _text = inputStr;
      });
    }
    if (event is RawKeyDownEvent &&
        event.isKeyPressed(LogicalKeyboardKey.tab)) {
      print("barcode done");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Barcode Scanner'),
      ),
      body: RawKeyboardListener(
        focusNode: FocusNode(),
        onKey: onEventKey,
        autofocus: true,
        child: Center(
          child: Text(_text),
        ),
      ),
      drawer: const Drawer(
        child: ListTile(
          leading: Icon(Icons.person),
          title: Switch(),
        ),
      ),
    );
  }
}
