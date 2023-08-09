'''
「関数の仕様」を満たす関数を作り、その関数を使って実行結果の通り出力するプログラムを作成してください。
仮引数の指定順は、関数の仕様にかかれた順番である必要はありません。
エラーの出ないように調整してください。
実行結果の出力は、次のデータをそれぞれ順番に関数へ与えた時の結果です。
実引数の指定順は、作成した関数の仮引数に合わせて指定してください。
　名前：省略(データを与えません), メッセージ：この電車は千葉までですか？
　名前：船橋太郎, メッセージ：快速だから千葉まで行くんじゃないかな？
　名前：津田沼夫, メッセージ：千葉？そいつはここで止まるぜ
　名前：オルガ・イナゲ, メッセージ：止まるんじゃねぇぞ
メインプログラムで必要になる変数などは自由に作成してください。

[ 関数の仕様 ]
- 関数名：post_message
- 引数：name(デフォルト値：名無し), message
- 戻り値：なし
- 処理内容：
引数nameに名前、引数messageにメッセージを受け取り、画面に
「【名前】　メッセージ」
の形式で受け取ったデータを出力する。
関数呼び出し時に名前の実引数が省略された場合のために、引数nameにはデフォルト値として「名無し」を設定しておく。

[ 実行結果 ]
【名無し】　この電車は千葉までですか？
【船橋太郎】　快速だから千葉まで行くんじゃないかな？
【津田沼夫】　千葉？そいつはここで止まるぜ
【オルガ・イナゲ】　止まるんじゃねぇぞ
'''

