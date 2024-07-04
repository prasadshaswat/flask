from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'description': 'We are looking for a software engineer to join our team.',
        'salary': '100,000 - 150,000 USD'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'description': 'We are looking for a data scientist to join our team.',
        'salary': '120,000 - 160,000 USD'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Seattle, WA',
        'description': 'We are looking for a product manager to join our team.',
        'salary': '130,000 - 170,000 USD'
    },
    {
        'id': 4,
        'title': 'UX Designer',
        'location': 'Los Angeles, CA',
        'description': 'We are looking for a UX designer to join our team.',
        'salary': '110,000 - 150,000 USD'
    },
    {
        'id': 5,
        'title': 'Marketing Manager',
        'location': 'Chicago, IL',
        'description': 'We are looking for a marketing manager to join our team.',
        'salary': '90,000 - 130,000 USD'
    },
]

@app.route('/')
def careers():
    return render_template('careers.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(debug=True)
