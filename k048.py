'''
Randomモジュールに別名を付けて使い、おみくじを作成してください。
おみくじの結果は次のデータをこの順番でリストにまとめ、randomモジュールを使って得る0～5の乱数と対応するデータを、条件分岐命令を使わずに画面へ出力してください。
リストオブジェクトの名前は自由に決めて構いません。
0～5の乱数を得るコードは、すでに入力済みのコードを参考にしてください。

[ データ ] ※一番上のデータの添え字が0となるようにリストへ保存する
大吉
吉
中吉
小吉
末吉
凶

[ 実行結果 ] ※複数回実行し、大吉と凶が出ることを必ず確認してください
今日の運勢は末吉です
今日の運勢は大吉です
今日の運勢は中吉です
今日の運勢は大吉です
今日の運勢は凶です
'''


##### 変数数numberには0～5のいずれかの整数値が保存されます
number = rnd.randint(0, 5)

