# SmartAttend - Intelligent Attendance Management System

A modern, AI-powered attendance management system that uses facial recognition technology to automate attendance tracking.

## 🚀 Features

- **Face Recognition**: Advanced CNN and HOG algorithms for accurate face detection
- **Real-time Tracking**: Instant attendance marking with live face detection
- **Secure Storage**: Reliable data management with Django's built-in database
- **User Management**: Easy registration and management of users
- **Analytics**: Track attendance patterns and generate reports
- **Responsive Design**: Modern UI that works on all devices

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Django
- **Database**: SQLite (Django ORM)
- **AI/ML**: OpenCV, dlib, face_recognition
- **Icons**: Font Awesome 6

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Smart-Attendance_Management_System.git
   cd Smart-Attendance_Management_System
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to access the application.

## 📱 Usage

1. **Register Users**: Add new users with their photos
2. **Take Attendance**: Use the webcam to detect and mark attendance
3. **View Records**: Access attendance data and generate reports
4. **Manage Data**: Admin interface for data management

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- OpenCV community
- Django framework
- Bootstrap team
- Font Awesome
