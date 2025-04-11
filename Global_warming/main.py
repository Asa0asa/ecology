from flask import Flask, render_template,request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  """Отображает главную страницу."""
  return render_template('index.html')

@app.route('/reasons')
def reason():
  """Отображает страницу с причинами глобального потепления."""
  return render_template('reasons.html')

@app.route('/consequences')
def consequence():
  """Отображает страницу с последствиями глобального потепления."""
  return render_template('consequences.html')

@app.route('/about')
def abouts():
  """Отображает страницу "О нас"."""
  return render_template('about.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Отображает страницу политики конфиденциальности."""
    return render_template('privacy_policy.html')

@app.route('/terms-of-service')
def terms_of_service():
    """Отображает страницу условий использования."""
    return render_template('terms_of_service.html')



if __name__ == '__main__':
  app.run(debug=True)

