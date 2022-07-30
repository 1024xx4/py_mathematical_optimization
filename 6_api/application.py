from flask import Flask, make_response, redirect, render_template, request
import pandas as pd
from problem import CarGroupProblem

app = Flask(__name__)


def check_request(request):
    """Request に学生 Data と車 Data が含まれているか確認する関数"""
    # 各 File を取得する
    students = request.files['students']
    cars = request.files['cars']

    # File が選択されているか確認
    if students.filename == '':
        # 学生 Data が選ばれていません
        return False
    if cars.filename == '':
        # 車 Data が選ばれていません
        return False

    return True


def preprocess(request):
    """Request data を受け取り、DataFrame に変換する関数"""
    # 各 File を取得する
    students = request.files['students']
    cars = request.files['cars']
    # pandas で読み込む
    students_df = pd.read_csv(students)
    cars_df = pd.read_csv(cars)

    return students_df, cars_df


def postprocess(solution_df):
    """最適化結果を HTML 形式に変換する関数"""
    solution_html = solution_df.to_html(header=True, index=False)
    return solution_html


@app.route('/', methods=['GET', 'POST'])
def solve():
    """最適化の実行と結果の表示を行なう関数"""
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


@app.route('/download', methods=['POST'])
def download():
    """Request に含まれる HTML の表形式 Data を csv 形式に変換して download する関数"""
    solution_html = request.form.get('solution_html')
    solution_df = pd.read_html(solution_html)[0]
    solution_csv = solution_df.to_csv(index=False)
    response = make_response()
    response.data = solution_csv
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=solution.csv'
    return response
