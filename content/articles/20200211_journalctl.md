Title: "jounald/journalctlの使い方"
Date: 2020-02-11
Category: Linux
Slug: journalctl-usage
Authors: liqsuq

journalctlが便利すぎた。dmesg使ったり/var/log/messages(もしくはsyslog)を見てたのが何だったのかと思う程。
具体的には`journalctl -b -o short-monotonic -p err`で今回のブートで(僕基準で)注視すべきログが抽出される>。
/var/log/messagesを目を皿にして眺めたり出力制限戻し忘れたりがなくなるえらい子だよ…。

## journald

[このサイト](https://www.school.ctc-g.co.jp/columns/nakai/nakai56.html)の図が非常に分かりやすかった。

![jounaldがログを収集する仕組み](/images/posts/2020-02-11-journalctl-1.png)

---<cite>RHEL7/CentOS7のjournaldでシステムログを一元管理(CTC教育サービス)</cite>

つまり、journaldは従来のrsyslogdの前段で包括したログを受け取りバイナリで保存しています。
加えてrsyslogdに流すべきメッセージは転送して従来の動作を維持しています。

journaldはデフォルトでは/run/log/journal/以下にログを保管していますが、
/runはtmpfsなために揮発し、確認できるログは前回ブートした時までとなります。
journalctlを使ってログ解析をしようと思ったら以下のコマンドで
/var/log/journald/を作成してログの保存場所を変更しましょう。(詳細はjournald.confのStorageを参照)

~~~
$ sudo mkdir -p /var/log/jounal
$ sudo systemctl restart systemd-journald
~~~

## journaldの設定

journaldの設定は/etc/systemd/journald.confによって行われています。デフォルトではファイル自体はあるが
全てコメントアウトされた状態になっているかと思います。
詳細な説明は[journald.conf(5)](https://www.freedesktop.org/software/systemd/man/journald.conf.html)を
見てもらうとして、特に重要な3点のみ書いておきます。

Storage
: バイナリデータを保存しておく場所を決めます。デフォルトは`auto`で以下の値が選択できます。

|persistent|書き込み不可で無い限り/var/log/journal/が作成され、データが保管されます。   |
|volatile  |/run/log/journal/にデータを置き、データの揮発を強制します。                 |
|auto      |/var/log/journal/があればこちらに置き、無ければ/run/log/journal/に置きます。|
|none      |どちらにもデータを置きません。ただしrsyslogd等への転送は機能します。        |

SystemMaxUse
: 保存されるデータのサイズを制限するために使われます。デフォルトではファイルシステムの大きさの10%と
  なる様に設定されています。

SystemKeepFree
: SystemMaxUseとは逆に、使用中のファイルシステムの空き容量をどれだけ残しておくか決めます。
  デフォルトでは15%で、より使用できる容量が少ない方が適用されます。

## jounalctlの使い方

journalctlは引数を取らず、多彩なオプションで挙動を変えます。
やっぱり詳細な説明は[journalctl(1)](https://www.freedesktop.org/software/systemd/man/journalctl.html#)に
任せますが、是非とも覚えて帰ってもらいたいオプションを抜粋します。
オプションの組み合わせで(journaldに対応しているモジュールのログなら)大抵のログ出力コマンドを代替できます
。

-b <var>ブートID</var>
: ブート毎にログを表示します。<var>ブートID</var>を省略すると前回のブートから(即ち現在)表示し、
  -1から減分でブートをさかのぼれます。また、--list-bootsオプションでブートの履歴を確認できます。

-o <var>出力フォーマット</var>
: ログの<var>出力フォーマット</var>を指定します。多いので使ってるフォーマットだけ以下に示します。

|short          |デフォルトでsyslogとほぼ同じフォーマットです             |
|short-monotonic|shortと似ていますがブートからのタイムスタンプを使用します|
|cat            |各エントリの実際の出力のみを表示します                   |

-p <var>ログレベル</var>
: ログレベル(優先度)でフィルタします。単一のログレベルの場合はその値より低い(重要な)ログを出力し、
  <var>ログレベル..ログレベル</var>の様にして範囲指定することもできます。
  ログレベルは以下の数値/テキストレベルどちらも使用可能です。

|数値|テキストレベル|
|:---|:-------------|
|0   |emerg         |
|1   |alert         |
|2   |crit          |
|3   |err           |
|4   |warning       |
|5   |notice        |
|6   |info          |
|7   |debug         |

-u <var>ユニット名</var>
: <var>ユニット名</var>でフィルタします。部分一致も含みます。

-t <var>syslog識別子</var>
: <var>syslog識別子</var>(ログに表示されてるモジュール名)でフィルタします。こちらは完全一致みたいです。

-e
: 最近のログを表示します。(多分1000件ログ出力してlessとかのページャで末尾表示するとかそんな動作)

-x
: 詳細なメッセージを表示します。

-f
: 最新のログを表示し、ログの更新を追いかけます。(tail -fの様な挙動)

-k
: カーネルメッセージを表示します。(dmesgと同等)


