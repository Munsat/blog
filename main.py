from flask import Flask, render_template
import requests


blog_response = requests.get(url='https://api.npoint.io/9d47b5aea74d44e3c0af')
all_blogs = blog_response.json()
print(all_blogs)


app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('index.html', blogs=all_blogs)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def get_post(post_id):
    return render_template('post.html', id=post_id, posts=all_blogs)

if __name__ == "__main__":
    app.run(debug=True)
