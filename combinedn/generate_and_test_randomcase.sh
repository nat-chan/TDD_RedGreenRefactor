#!/bin/bash

# 作成するランダムケースはリストの長さが1~10の一様乱数からサンプリングするものとする
length_max=10
# サンプルケース数は100とする
case_num=100
# generate.pyを用いてランダムケースを作成
oj g/i -d "random${length_max}" "python3 generate.py --length_max=${length_max}" "${case_num}"
# ソルバーslow_answerを用いてランダムケースに対する解答を作成
oj g/o -d "random${length_max}" -c "python3 solve.py --solver=slow_answer"
# ソルバーfast_answerが正しい答えを返すことをテストする
oj t -d "random${length_max}" -c "python3 solve.py --solver=fast_answer"

# 以下は筆者の環境での最遅実行時間及び最大使用メモリである
: << EOF
[INFO] slowest: 0.309337 sec  (for random-040)
[INFO] max memory: 9.576000 MB  (for random-026)
[SUCCESS] test success: 100 cases
EOF


# slow_answerが現実的な時間での解答が不可能なほど巨大なサンプルケースを作成してfast_answerをプロファイルする
# 作成するランダムケースはリストの長さが1~100の一様乱数からサンプリングするものとする
length_max=100
# サンプルケース数は10とする
case_num=10
# generate.pyを用いてランダムケースを作成
oj g/i -d "random${length_max}" "python3 generate.py --length_max=${length_max}" "${case_num}"
# 今回は、slow_answerが現実的な時間での解答が不可能であるので解答は作成しない
# oj g/o -d "random${length_max}" -c "python3 solve.py --solver=slow_answer"
# ソルバーfast_answerをプロファイルする
oj t -d "random${length_max}" -c "python3 solve.py --solver=fast_answer"

# 以下は筆者の環境での最遅実行時間及び最大使用メモリである
# ちなみにslow_answerでは1時間ほど待っても終わらなかった
: << EOF
[INFO] slowest: 0.274804 sec  (for random-001)
[INFO] max memory: 9.576000 MB  (for random-004)
[SUCCESS] test success: 10 cases
EOF

