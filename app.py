from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    profile = {
        'name': 'سارا بهبودی',
        'student_id': '40113011005',
        'major': 'دانشجوی علوم کامپیوتر',
        'role': 'نوازنده و مدرس گیتار پاپ و کلاسیک'
    }
    return render_template('index.html', profile=profile)


if __name__ == '__main__':
    # تنظیم برای اجرا روی همه‌ی آدرس‌ها (نه فقط لوکال)
    app.run(host='0.0.0.0', port=5000, debug=True)
