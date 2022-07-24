# 数理最適化 API と Web application の開発
## 目的・意義
- 数理 Model の活用方法の幅を広げる
- 実装した数理 Model を System や Product のなかで動かす
- Engineer と議論できるようになり、作業が効率化する
- どのような業務でも使用できる汎用的な機能を開発したときに、その機能を API として公開することで誰でも気軽に使えるようになる。
- Programming を主業務としない Business 職の人も簡単に機能を使えるようになる。
- 機能を再開発する手間がかからず、開発を効率化できる
- Internet に接続してればどこでも利用できる
- Speed 感をもって PoC(Proof of Concept: 概念実証) を推進できる場面が増える。  
  検討 ~ 数理 Modeling ~ Application まで、一気通貫して開発することが可能になる。
- Counter-part \(数理 Model 開発の依頼者や Project owner) に Prot-type を見せながら提案できるようになるため、Image が付きやすく意思決定しやすくなる
- Product を俯瞰的に理解できるようになる。

API と Web application の基礎と Merit を学ぶことで、数理 Model をより効果的に利用できるようになる。

---

### API (Application Programming Interface) とは？
- 汎用性の高い機能を、誰でも手軽に利用できるように提供される便利なしくみ
- API の利用者は、公開された API を通じて、欲しい機能を一から開発することなく使用可能なる。
- 利用者が API に対してやってほしいことをの Request を送ると、API がなんらかの処理を行なったうえで適切な Response を返してくれる。

#### Samples
- Shift 作成用の Data を request したら最適化してくれた結果を response してくれる API.
- User ID を request したら Recommend 結果を response してくる API.
- 画像を request したら分類結果を response してくれる API.
- 文章を投げたら Positive | Negative を response してくれる API.

---

### Web application とは？
一般的に Internet などの Network を経由して利用する Application Software のこと。
- Web server 上で動いている。
- 大量の Data を管理する Database も同時に利用されることが一般的。

#### API と Web application　との違い
- Web application は、Website を介して利用者が機能を操作 \(Interaction) する。
- API は基本的に利用者との Interaction は発生せず、Data を送信したら Data が返却される、といった Systematic な機能。  
※ API は Web application の裏側で使用されることが多くなる。

