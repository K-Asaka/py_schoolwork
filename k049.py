'''
外部ライブラリ「matplotlib」を使い、次のデータをグラフ化して出力するプログラムを作成してください。
なお、参考書の内容だけではグラフの出力ができないため、グラフ出力にはすでに入力済みのサンプルコードを参考にしてください。
実行時に「ModuleNotFoundError: No module named 'matplotlib'」と出力される場合は、matplotlibパッケージをインストールしてから実行結果を確認してください。
インストール方法は環境によって異なります。
Anacondaの場合は「conda」コマンド、Pythonをインストールして環境を整えた場合は「pip」コマンドでインストールができます。
もし「pip」コマンドが使えない場合は、「py -m pip install パッケージ名」を試してください。
詳細なインストール方法はインターネットを検索してください。

[ データ ]
622890
627073
631973
635947
639107
640906

'''
##### [ サンプルコード ]
import matplotlib.pyplot as plt
plt.plot([ 1,2,3 ]) # グラフ生成
plt.show()          # グラフ作成の後に呼び出すことでグラフを出力


