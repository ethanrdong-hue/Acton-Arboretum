from flask import Flask, render_template, request

app = Flask(__name__)

# Sample tree data
TREES = [
    {
        'id': 1,
        'name': 'Red Oak',
        'scientific_name': 'Quercus rubra',
        'description': 'A large, fast-growing deciduous tree native to eastern North America.',
        'height': '60-75 ft',
        'location': 'North Section'
    },
    {
        'id': 2,
        'name': 'Sugar Maple',
        'scientific_name': 'Acer saccharum',
        'description': 'Known for beautiful fall colors and sweet sap used for maple syrup.',
        'height': '50-80 ft',
        'location': 'East Section'
    },
    {
        'id': 3,
        'name': 'Eastern Hemlock',
        'scientific_name': 'Tsuga canadensis',
        'description': 'A native evergreen conifer with soft, feathery foliage.',
        'height': '40-70 ft',
        'location': 'West Section'
    },
    {
        'id': 4,
        'name': 'White Birch',
        'scientific_name': 'Betula pendula',
        'description': 'Distinctive white bark and delicate leaves that turn golden in fall.',
        'height': '40-60 ft',
        'location': 'Central Meadow'
    }
]

# Sample events data
EVENTS = [
    {
        'id': 1,
        'title': 'Spring Tree Planting',
        'date': '2024-04-15',
        'time': '10:00 AM',
        'description': 'Join us for a community tree planting event!'
    },
    {
        'id': 2,
        'title': 'Summer Nature Walk',
        'date': '2024-06-20',
        'time': '3:00 PM',
        'description': 'Guided tour through the arboretum highlighting seasonal blooms.'
    },
    {
        'id': 3,
        'title': 'Fall Colors Festival',
        'date': '2024-10-01',
        'time': '9:00 AM',
        'description': 'Celebrate the vibrant colors of autumn with family activities.'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trees')
def trees():
    return render_template('trees.html', trees=TREES)

@app.route('/trees/<int:tree_id>')
def tree_detail(tree_id):
    tree = next((t for t in TREES if t['id'] == tree_id), None)
    if tree:
        return render_template('tree_detail.html', tree=tree)
    return "Tree not found", 404

@app.route('/events')
def events():
    return render_template('events.html', events=EVENTS)

@app.route('/visit')
def visit():
    return render_template('visit.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', success=True)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
