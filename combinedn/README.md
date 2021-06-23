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
