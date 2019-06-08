from flask import Flask, render_template, url_for
app = Flask(__name__)

'''posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

'''
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

'''
@app.route("/about")
def about():
    return render_template('about.html', title='About')

'''

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
