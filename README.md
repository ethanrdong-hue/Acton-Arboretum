# 🌳 Acton Arboretum Website

> A beautiful, fully responsive website for the Acton Arboretum built with Python Flask and a serene green color scheme.

![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Mobile Friendly](https://img.shields.io/badge/Mobile-Friendly-green?style=flat-square&logo=mobile)

## ✨ Features

- 🌍 **Fully Responsive Design** - Works perfectly on mobile, tablet, and desktop
- 🎨 **Beautiful Green Theme** - Calming, nature-inspired color palette
- 🌲 **Tree Database** - Browse and learn about trees in the collection
- 📅 **Events Calendar** - Upcoming programs and activities
- 📍 **Visitor Information** - Hours, admission, directions, and amenities
- 💬 **Contact Form** - Easy way for visitors to get in touch
- ♿ **Accessible** - Built with accessibility in mind
- ⚡ **Fast & Lightweight** - Built with Flask for optimal performance

## 📋 Pages Included

| Page | Description |
|------|-------------|
| **Home** | Welcome page with highlights and quick links |
| **About** | Mission, history, and facility information |
| **Trees** | Browse the tree collection with details |
| **Tree Details** | Individual pages for each tree species |
| **Events** | Calendar of upcoming programs and activities |
| **Visit** | Hours, admission, directions, and amenities |
| **Contact** | Contact form and visitor information |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ethanrdong-hue/acton-arboretum.git
cd acton-arboretum
```

2. **Create a virtual environment:**
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

5. **Open in browser:**
Navigate to `http://localhost:5000`

## 📁 Project Structure

```
acton-arboretum/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet (responsive, green theme)
│   └── images/                # Image assets (add your images here)
└── templates/
    ├── base.html              # Base template with navigation
    ├── index.html             # Home page
    ├── about.html             # About page
    ├── trees.html             # Tree collection browse
    ├── tree_detail.html       # Individual tree details
    ├── events.html            # Events calendar
    ├── visit.html             # Visitor information
    └── contact.html           # Contact form
```

## 🎨 Design Features

### Color Palette
- **Primary Green**: #2d5016 (Dark forest green)
- **Secondary Green**: #4a7023 (Medium green)
- **Accent Green**: #6ba632 (Bright green)
- **Light Green**: #d4e8c1 (Pale green)
- **Background**: #f0f5ea (Very light green)

### Responsive Breakpoints
- **Desktop**: Full layout with multi-column grids
- **Tablet**: Adjusted spacing and 2-column layouts
- **Mobile**: Stacked single-column layout (<768px)

## 📱 Mobile Optimization

✅ Touch-friendly buttons and links  
✅ Optimized font sizes for readability  
✅ Responsive images and layouts  
✅ Mobile-optimized navigation  
✅ Fast loading on all devices  

## 🛠️ Customization

### Adding Trees
Edit the `TREES` list in `app.py`:
```python
TREES = [
    {
        'id': 1,
        'name': 'Tree Name',
        'scientific_name': 'Scientific Name',
        'description': 'Description here',
        'height': '50-60 ft',
        'location': 'Location in arboretum'
    },
    # Add more trees here
]
```

### Adding Events
Edit the `EVENTS` list in `app.py`:
```python
EVENTS = [
    {
        'id': 1,
        'title': 'Event Name',
        'date': 'YYYY-MM-DD',
        'time': 'HH:MM AM/PM',
        'description': 'Event description'
    },
    # Add more events here
]
```

### Modifying Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
  --primary-green: #2d5016;
  --secondary-green: #4a7023;
  --accent-green: #6ba632;
  /* ... more colors ... */
}
```

## 📚 Technologies Used

- **Backend**: Flask 2.3.2 (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Responsive CSS Grid and Flexbox
- **Deployment Ready**: Can be deployed to Heroku, PythonAnywhere, AWS, etc.

## 🌐 Deployment

### Option 1: Heroku
```bash
heroku create your-app-name
git push heroku main
```

### Option 2: PythonAnywhere
1. Sign up at pythonanywhere.com
2. Upload your repository
3. Configure web app settings
4. Visit your-username.pythonanywhere.com

### Option 3: AWS, Azure, Google Cloud
Follow their respective Python/Flask deployment guides.

## 📖 Usage

### Access the website
- Home: `http://localhost:5000/`
- Trees: `http://localhost:5000/trees`
- Events: `http://localhost:5000/events`
- Visit: `http://localhost:5000/visit`
- Contact: `http://localhost:5000/contact`

### API Endpoints
- Get all trees: `http://localhost:5000/api/trees`
- Get all events: `http://localhost:5000/api/events`

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Created for the Acton Arboretum Community

## 🙋 Support

For questions or issues:
- 📧 Email: info@actonarboretum.org
- 📍 Visit: 123 Forest Lane, Acton, MA 01720
- 📞 Phone: (555) 123-4567

## 🌱 Future Enhancements

- [ ] Image gallery for trees and events
- [ ] Online ticket booking system
- [ ] Membership management portal
- [ ] Photo upload from visitors
- [ ] Interactive map of the arboretum
- [ ] Email newsletter subscription
- [ ] Mobile app version
- [ ] Donation system
- [ ] Search functionality
- [ ] Multi-language support

---

**Made with 🌳 for nature lovers everywhere**

*Last updated: July 2024*
