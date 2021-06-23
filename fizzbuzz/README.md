## Problem [cyber-dojo Fizz Buzz](https://cyber-dojo.org/creator/choose_ltf?type=single&exercise_name=Fizz%20Buzz)

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

### Sample output:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc up to 100
```

### Specs.

```
TODO
[x] 関数single_line_answerが各行の入力に対して正しい答えを返す
    [x] 出力はstrである
    [x] 3の倍数でないかつ5の倍数でない時の出力は数値を10進数で表した文字列である
        [x] intの1を渡したら文字列1を返す
        [x] intの2を渡したら文字列2を返す
    [x] 3の倍数かつ5の倍数でない時の出力はFizzである
        [x] intの3を渡したら文字列Fizzを返す
        [x] intの6を渡したら文字列Fizzを返す
    [x] 5の倍数かつ3の倍数でない時の出力はBuzzである
        [x] intの5を渡したら文字列Buzzを返す
        [x] intの10を渡したら文字列Buzzを返す
    [x] 3の倍数かつ5の倍数の時の出力はFizzBuzzである
        [x] intの15を渡したら文字列FizzBuzzを返す
    [ ] 1から100まで
[ ] 関数multiple_line_answerが長さ100の文字列のリストを返す
    [ ] 出力の長さが100である
    [ ] 出力の要素がすべてstrである
[ ] 関数print_answerが最終的な要件(ref:readme.txt)を満たす
```
