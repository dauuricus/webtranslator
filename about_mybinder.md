https://rentry.co/3xiki/raw

https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org

![](https://mybinder.readthedocs.io/en/latest/_static/logo.png)

## Get started with Binder 
このページは、独自のリポジトリを構築し、それらをBinderと共有するのに役立ちます。一般的なバインダープロジェクトの詳細については、‌mybinder.orgについて✧1✧‌を参照してください。

link✧1: [About mybinder.org](https://mybinder.readthedocs.io/en/latest/about/index.html)

別の有用なリソース
TheTuringWay✧2✧‌は、3つの一般的なプログラミング言語で‌Zero-to-Binderチュートリアル✧3✧‌もあります。

	![](https://the-turing-way.netlify.app/_static/logo.jpg)
link✧2: [The Turing Way](https://github.com/alan-turing-institute/the-turing-way)
link✧3: [Zero-to-Binder tutorial](https://the-turing-way.netlify.app/communication/binder/zero-to-binder.html)

## What is a Binder? 
バインダー（バインダー対応リポジトリーとも呼ばれます）は、少なくとも2つのものを含むコードリポジトリーです。

* 人々に実行してもらいたいコードまたはコンテンツ。これは、アイデアを説明するJupyter Notebook、または視覚化を行うRスクリプトである可能性があります。

* ご使用の環境の構成ファイル。これらのファイルは、コードの実行に必要な環境を構築するためにBinderによって使用されます。使用可能なすべての構成ファイルのリストについては、‌構成ファイル✧4✧‌ページを参照してください。

link✧4: [Configuration Files](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/using/config_files.html#config-files)
構成ファイルは、リポジトリのルートまたはリポジトリのルート（つまり、myproject/binder/）。

Binderリポジトリは、BinderHubによって構築できます。これにより、他のユーザーと共有できるリンクが生成され、他のユーザーがリポジトリ内のコンテンツと対話できるようになります。

## What is mybinder.org ? 
mybinder.orgは、オンラインリポジトリから再現可能でインタラクティブな計算環境を構築および共有するためのオンラインサービスです。内部的には、‌Binderコミュニティ✧6✧‌によって維持されているのは、BinderHubデプロイメントのフェデレーションです。これは、BinderHubinの唯一の存在ではありませんが、公共サービスとBinderHubテクノロジーのデモンストレーションの両方の役割を果たします。独自のBinderHubを自分の用途に展開することに興味がある場合は、‌BinderHubのドキュメント✧5✧‌を参照し、‌Binderコミュニティ✧6✧‌に連絡することを躊躇しないでください。

✦link✧✸5: [BinderHub documentation](https://binderhub.readthedocs.io/en/latest)
✦link✧✸6: [Binder community](https://gitter.im/jupyterhub/binder)

## What is the Binder community? 
計算資料（Jupyterノートブック、Rスクリプト、environmentfilesなど）を計算環境（Dockerイメージ）に簡単に変換し、クラウドを介してこの環境にサービスを提供することを目的とした人々の集まり。このプロセスを管理する基盤となるテクノロジーは、‌BinderHub✧7✧‌と呼ばれます。

✦link✧✸7: [BinderHub](https://binderhub.readthedocs.io/en/latest)
詳細については、：ref：aboutをご覧ください。

## What is BinderHub? 
‌BinderHub✧8✧‌は、計算材料をクラウド内のインタラクティブな計算環境に変えるサーバーテクノロジーです。展開プロセスを簡素化し、拡張を容易にするために、‌KubernetesとJupyterHub✧9✧‌を利用します。

✦link✧✸8: [BinderHub](https://binderhub.readthedocs.io/en/latest)
✦link✧✸9: [Kubernetes and JupyterHub](https://z2jh.jupyter.org/)

## How can I prepare a repository for Binder? 
mybinder.orgのBinderHubで使用するためにリポジトリを準備するには、次の条件が満たされていることを確認する必要があります。

* リポジトリはオンラインの公開場所にあります（GitHubやBitBucketなど）

* リポジトリには、個人情報や機密情報（パスワードなど）は必要ありません。

* リポジトリには、その環境を指定する構成ファイルがあります（例については以下を参照してください）。

* リポジトリには、人々が読むために設計されたコンテンツが含まれています。

### ヒント
バインダーで使用するサンプルリポジトリのリストについては、‌サンプルバインダーリポジトリ✧10✧‌ページを参照してください。

✦link✧✸10: [Sample Binder Repositories](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/examples/sample_repos.html)

## How can I customize my Binder environment? 
バインダー環境をカスタマイズする方法はたくさんあります。たとえば、‌多くのオープンソース言語を使用する✧11✧‌、‌ユーザーインターフェイスを構成する✧12✧‌などがあります。

✦link✧✸11: [use many open source languages](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/howto/languages.html)
✦link✧✸12: [configure the user interface](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/howto/user_interface.html)
詳細については、‌ハウツーガイド✧13✧‌または‌サンプルリポジトリの例✧14✧‌をご覧ください。

✦link✧✸13: [the How-to guides](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/howto/index.html)
✦link✧✸14: [the sample repository examples](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/examples/index.html)

## A Binder example 
たとえば、実行するためにいくつかのパッケージを必要とする単純なリポジトリを見てみましょう。

### Explore the repository contents 
このリポジトリの内容を調べると、次のファイルが表示されます。

## この場合、2つの重要なファイルがあります。
```
./
├── environment.yml
├── index.ipynb
└── README.md
```

* コンテンツファイル：index.ipynbは、プロットを生成する短いJupyterNotebookです。

* 環境構成ファイル：environment.ymlは、Anaconda環境を指定する標準ファイルです。

### 重要
environment.ymlはバインダー固有ではないことに気付くかもしれません。これは意図的なものです。バインダーは、データサイエンスコミュニティですでに標準となっている環境構成ファイルを使用しようとします。使用可能なすべての構成ファイルのリストについては、‌構成ファイル✧15✧‌ページを参照してください。

✦link✧✸15: [Configuration Files](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/using/config_files.html#config-files)

## Get your own copy of this repository 
これらのファイルを含むリポジトリは、次のリンクにあります。

‌https：//github.com/binder-examples/conda✧16✧‌

✦link✧✸16: https://github.com/binder-examples/conda
Binderの動作を監視するには、最初にこのリポジトリをフォークします。これにより、condaリポジトリの独自のコピーが提供されます。

## Build your repository 
次に、バインダーリポジトリを構築しましょう。 ‌https：//mybinder.org✧17✧‌にアクセスします。mybinder.orgをビルドするためのリポジトリを指定するように求めるフォームが表示されます。最初のフィールドに、フォークされたリポジトリのURLを貼り付けます。これは次のようになります。

✦link✧✸17: https://mybinder.org

```
https://github.com/<your-username>/conda
```

最後に、起動ボタンをクリックします。これにより、mybinder.orgは、リポジトリの実行に必要な環境を構築するように求められます。 [ログのビルド]ボタンをクリックすると、ビルドプロセスによって生成されたログを確認できます。

バインダーリポジトリの構築中に、一意のバインダーを指すURLをメモします。このURLを友人と共有して、リポジトリのインタラクティブバージョンにアクセスできるようにすることができます。

BinderHubユーザーインターフェイスの簡単なレイアウトについては、以下を参照してください。

![](https://mybinder.readthedocs.io/en/latest/_images/mybinder-ui-start.png)

バインダーリポジトリがすでに一度ビルドされている場合は、その後のバインダーリンクをクリックしてもビルドプロセスは再トリガーされません。ただし、リポジトリに変更をプッシュすると、次に誰かがリンクをクリックしたときにリポジトリが再構築されます。

環境ファイルとコンテンツファイルが同じリポジトリの同じブランチに格納されていない場合、URLの生成方法については、‌コンテンツと環境に異なるリポジトリを使用する✧18✧‌ページを参照してください。

✦link✧✸18: [Use different repositories for content and environment](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/howto/external_binder_setup.html#external-binder-setup)
Binderに慣れてきたので、Binderでできることの詳細については、‌一般的な使用例✧19✧‌ページを参照してください。

✦link✧✸19: [Common use-cases](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-mybinder-org\/using/using.html#using-binder)
