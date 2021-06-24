## Problem [cyber-dojo Combined Number]()
Write a function accepting a list of non negative integers, and returning their largest possible combined number as a string. For example

### Sample output:
```
given [50, 2, 1, 9]  it returns "95021"    (9 + 50 + 2 + 1)
given [5, 50, 56]    it returns "56550"    (56 + 5 + 50)
given [420, 42, 423] it returns "42423420" (42 + 423 + 420)
```

[Source](https://blog.svpino.com/about)

### Specs.

```
TODO
[X] 入力引数の配列が破壊されない
[X] 要素数が1の場合
    [X] リスト[1]が与えられた時には文字列1を返す
[X] 要素数が2の場合
    [X] リスト[1, 0]が与えられた時には文字列10を返す
    [X] リスト[0, 1]が与えられた時には文字列10を返す
    [X] リスト[9, 10]が与えられた時には文字列910を返す
[X] 要素数が3の場合
    [X] リスト[5, 50, 56]が与えられた時には文字列56550を返す
    [X] リスト[420, 42, 423]が与えられたときには文字列42423420を返す
[X] 要素数が4の場合
    [X] リスト[50, 2, 1, 9]が与えられたときには文字列95021を返す
[ ] 要素数が大きい場合に現実的な時間で計算結果を返す
```

### 発展的な話題

授業時間では`O(N!)`解しか得られなかったが、`O(NlogN)`解が実装及びテストできたので報告する。
詳しい詳細は、[combinedn.pyに実装してある`slow_answer`と`fast_answer`のdocstring](./combinedn.py)を参照してほしい。

`fast_answer`の動作の正当性は100件のランダムテストケースを[generate.py](./generate.py)を用いて作成し、
すべて`slow_answer`と同じ解答が得られたことで確認した。
その作業は[online-judge-tools](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)を用いて自動化した。
その作業記録は[generate_and_test_randomcase.sh](./generate_and_test_randomcase.sh)に記録してある。
なお、入出力をパースし、指定したソルバーの解答を出力するプログラムは[solve.py](solve.py)に切り分けた。
以下のようにソルバーを指定して実行できる。

```
python3 solve.py --solver=slow_answer < random10/random-000.in
python3 solve.py --solver=fast_answer < random10/random-000.in
```
