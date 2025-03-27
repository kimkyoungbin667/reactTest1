from flask import Flask, render_template, jsonify
import main_views
import uuid  # 고유 주문 번호 생성을 위한 모듈

app = Flask(__name__)

# main_views.py를 app 객체에 적용
app.register_blueprint(main_views.bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goToPayment')
def goToPayment():
    return render_template('payment.html')

@app.route('/pay', methods=['POST'])
def pay():
    order_id = str(uuid.uuid4())  # 랜덤한 고유 주문번호 생성

    # 결제에 필요한 정보들을 프론트로 JSON 형식으로 넘겨줌
    return jsonify({
        "clientKey": "test_ck_ex6BJGQOVDv6WZ4Axb4q8W4w2zNb",  # [토스 테스트용 클라이언트 키]로 변경
        "amount": 5000,  # 결제 금액 (원)
        "orderId": order_id,  # 고유 주문 ID
        "orderName": "김기현님의 아령",  # 결제창에 표시될 상품명
        "successUrl": "http://localhost:5000/success",  # 결제 성공 시 이동할 URL
        "failUrl": "http://localhost:5000/fail"  # 결제 실패 시 이동할 URL
    })

# 결제 성공 시 표시될 페이지
@app.route('/success')
def success():
    return "결제 성공!"

# 결제 실패 시 표시될 페이지
@app.route('/fail')
def fail():
    return "결제 실패"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
