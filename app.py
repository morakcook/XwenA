from flask import Flask, request, jsonify, render_template
from Generation import generation
import pandas as pd

def get_web_service_app(main):

    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('Inference.html')

    @app.route('/<path:page>')
    def dynamic_page(page):
        if page == 'TestLog':
            score = []
            label = []
            df = pd.read_excel('/home/dacon_project/Data/Excel_Files/데이콘 제출로그.xlsx')
            for i in range(len(df)):
                score.append(df.loc[i, '점수'])
                label.append(i)
            print(score)
            print(label)
            table_html = df.to_html()
            return render_template(f'{page}.html',table_html=table_html, scores=score, labels=label)
        return render_template(f'{page}.html')

    @app.route('/api', methods=['POST'])
    def api():
        query = request.json
        prompt = query["prompt"]  # 클라이언트가 보낸 입력 텍스트
        generated_texts = main(prompt)  # 생성된 텍스트들을 main() 함수를 호출하여 받음
        response_data = {"prompt": prompt, "generated_texts": generated_texts}  # 입력 텍스트와 생성된 텍스트들을 JSON 데이터로 만듦
        print(response_data)
        response = jsonify(response_data)  # JSON 응답 생성
        return response  # JSON 응답 반환

    return app

if __name__ == "__main__":
    app = get_web_service_app(generation.main)
    app.run(debug=True)
