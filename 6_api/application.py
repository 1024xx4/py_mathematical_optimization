from flask import Flask, redirect, render_template, request
from problem import CarGroupProblem

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def solve():
    # TOP page を表示する（GET request がきた場合)
    if request.method == 'GET':
        return render_template('index.html', solution_html=None)

        # POST request である「最適化を実行」Button が押された場合に実行
        # Data が Upload されているか check する。適切でなければもとの Page (TOP page) に戻る
        if not check_request(request):
            return redirect(request.url)

        # 前処理 (Data 読み込み)
        students_df, cars_df = preprocess(request)
        # 最適化実行
        solution_df = CarGroupProblem(students_df, cars_df).solve()
        # 後処理（最適化結果を HTML に表示できる形式にする）
        solution_html = postprocess(solution_df)
        return render_template('index.html', solution_html=solution_html)
