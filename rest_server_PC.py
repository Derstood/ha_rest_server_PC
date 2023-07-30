import pyautogui
from flask import Flask

app = Flask(__name__)

@app.route('/execute_ctrl_c', methods=['POST'])
def execute_ctrl_c():
    # 在这里执行Ctrl+C操作的代码
    pyautogui.hotkey('alt', 'tab')
    return 'Ctrl+C executed successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
