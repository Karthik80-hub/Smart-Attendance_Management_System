# AI-Powered Projects Portfolio

This repository showcases two major AI/ML projects developed by Karthik Chunchu, demonstrating expertise in full-stack development, cloud deployment, and artificial intelligence.

## 🎯 Projects

### 1. SmartAttend - Intelligent Attendance Management System
A modern, AI-powered attendance management system that uses facial recognition technology to automate attendance tracking.

#### 🌟 Key Features
- **Face Recognition**: Advanced CNN and HOG algorithms for accurate face detection
- **Real-time Tracking**: Instant attendance marking with live face detection
- **Secure Storage**: Reliable data management with Django's built-in database
- **User Management**: Easy registration and management of users
- **Analytics**: Track attendance patterns and generate reports
- **Responsive Design**: Modern UI that works on all devices

#### 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Django
- **Database**: SQLite (Django ORM)
- **AI/ML**: OpenCV, dlib, face_recognition
- **Cloud Infrastructure**: AWS EC2, Route 53, Nginx, SSL (Certbot)
- **DevOps**: Jenkins CI/CD, Gunicorn WSGI
- **Icons**: Font Awesome 6

#### 🚀 Cloud Deployment
- Deployed on AWS EC2 with domain routing via Route 53
- Secured with Nginx and SSL via Certbot
- Configured Jenkins for CI/CD to automate deployments on GitHub pushes
- Production-ready with Gunicorn WSGI server
- Optimized static file handling for production

#### 📱 Live Demo
[SmartAttend Live Demo](your-demo-url-here)

### 2. AI Job Applier Bot
An intelligent automation system that helps streamline the job application process using AI/ML techniques.

#### 🌟 Key Features
[To be added based on project specifics]

#### 🛠️ Tech Stack
[To be added based on project specifics]

#### 🚀 Cloud Deployment
[To be added based on project specifics]

## 📋 Prerequisites

### SmartAttend
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

### SmartAttend
1. Clone the repository:
   ```bash
   git clone https://github.com/Karthik80-hub/Smart-Attendance_Management_System.git
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

### SmartAttend
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

## 👥 Author

- **Karthik Chunchu** - Full Stack Developer & AI/ML Engineer
  - GitHub: [@Karthik80-hub](https://github.com/Karthik80-hub)
  - LinkedIn: [Your LinkedIn Profile]

## 🙏 Acknowledgments

- OpenCV community
- Django framework
- Bootstrap team
- Font Awesome
- AWS Cloud Services
- Jenkins CI/CD community
