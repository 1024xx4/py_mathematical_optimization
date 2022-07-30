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

---

### 要件と仕様の定義

#### 要件

API に学生 Data と車 Data を投げると、学生の乗車 Group 分け問題を解いた結果を得られる。

#### 仕様

- HTTP Protocol による API との通信 (Request と Response)  
  Request (入力) : 学生 Data, 車 Data の csv File  
  Response (出力) : 最適化結果の csv File
- 最適化を実行  
  学生の乗車 Group 分けを行なう Module の作成

### 数理 Model の Module化

- 類似の最適化 Program の開発の際に毎回その数理 Model の Code を copy する必要がなくなり、それぞれの Program で再利用できるようになる。
- 機能ごとに Code が分かれて疎結合になるので、maintenance 性が高められる。
- 実務において 最適化 Model の実装をして、その機能を提供するまでが DS の責任領域になる場合が多く、数理 Model の Module 化ができていると、入出力
  の形式が定まることと同義であるため別領域の開発をしている Engineer と入出力形式を決めるだけでそれぞれの開発を独立して進めることができる

#### 実務での設計

- solive() の帰り値として最適化 Status を返す方が親切。
- すでに解き終わっている問題に対して solve() が呼ばれた場合は、前回の結果を Cache などで Instance が保持しておいて返す方が効率的
- 初期化時に意図しない Data が渡ってきたときの Error handling を実装することも重要。

---
### Web application
#### 要件と使用の定義
##### 要件
Browse から特定の URL に access し、学生 Data と車 Data を upload すると、学生の乗車 Group 分け問題を解いた結果を Download できる。

#### 仕様
- HTTP protocol による Web server との通信ができる
- TOP page では学生の Data と車 Data の csv file を upload できる。
- 最適化後の Page では結果を表示し、csv file の download ができる。

### UI Design
#### TOP page
![top](https://user-images.githubusercontent.com/7993391/181908669-f420f315-d842-4b85-97ba-ed4a2c36bfb8.png)

#### students.csv と cars.csv を upload した状態の TOP page
![top_uploaded](https://user-images.githubusercontent.com/7993391/181908729-b2734759-005e-4245-9b86-76530024be25.png)

#### 「最適化を実行」する Button を押下した後の page
- 結果を画面に表示する。
- Download する機能がある。
![after_optimization_execution](https://user-images.githubusercontent.com/7993391/181908747-742cae7d-ee20-4ca2-9361-12c1d6a078ec.png)
