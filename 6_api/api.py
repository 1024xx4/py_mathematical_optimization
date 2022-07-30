# 必要な Library の import
from flask import Flask, make_response, request
import pandas as pd

from problem import CarGroupProblem

# Flask の Application を作成
app = Flask(__name__)


def preprocess(request):
    """
    Request data を受け取り、DataFrame に変換する関数
    """
    # 各 File を取得する
    students = request.files['students']
    cars = request.files['cars']
    # pandas で読み込む
    students_df = pd.read_csv(students)
    cars_df = pd.read_csv(cars)

    return students_df, cars_df


def postprocess(solution_df):
    """
    DataFrame を csv に変換する関数
    """
    solution_csv = solution_df.to_csv(index=False)
    response = make_response()
    response.data = solution_csv
    response.headers['Content-Type'] = 'text/csv'
    return response


# 最適化問題を解く API の関数
@app.route('/api', methods=['POST'])
def solve():
    # 1. Reauest 受信
    students_df, cars_df = preprocess(request)
    # 2. 最適化実行
    solution_df = CarGroupProblem(students_df, cars_df).solve()
    # 3. Response 返送
    response = postprocess(solution_df)
    return response
