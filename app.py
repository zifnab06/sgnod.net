from flask import Flask, jsonify, render_template

app = Flask(__name__)

with app.app_context():
    import local_config
    app.config.from_object(local_config)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
       
    @app.route('/comingsoon')
    def comingsoon():
        return render_template('comingsoon.html')

if __name__ == "__main__":
    app.run(
        host=app.config.get('HOST', None),
        port=app.config.get('PORT', None)
    )

