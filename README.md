# Smart Attendance Management System

A modern, AI-powered attendance management system built with Django that leverages facial recognition technology for automated attendance tracking. Deployed on AWS EC2 with full CI/CD pipeline integration.

## Key Features

### CI/CD Pipeline
- **Jenkins Integration**: Automated deployment via Jenkins pipeline
- **GitHub Webhooks**: Real-time triggers on code changes
- **Quality Assurance**: Automated testing and deployment
- **Production Ready**: Streamlined deployment process

### AI-Powered Features
- **Face Recognition System**
  - Real-time facial detection and recognition
  - Advanced CNN and HOG algorithms for accurate face detection
  - Automated attendance marking through facial recognition
  - Multi-face detection and processing
  - High-accuracy attendance tracking

### Core Attendance Features
- **Automated Attendance Tracking**
  - Real-time attendance monitoring
  - Automated attendance marking through facial recognition
  - Multiple attendance marking methods
  - Bulk attendance management

- **User Management**
  - Secure user authentication
  - Role-based access control
  - User profile management with facial data
  - Department-wise organization

- **Analytics & Reporting**
  - Real-time attendance analytics
  - Customizable reports
  - Attendance statistics
  - Export functionality

- **Admin Dashboard**
  - Comprehensive admin interface
  - User management
  - Attendance oversight
  - System configuration

## Cloud Deployment

### AWS Infrastructure
- **EC2 Instance**: Hosted on AWS EC2
- **Domain Management**: Route 53 for domain routing
- **Security**: Nginx and SSL via Certbot
- **CI/CD**: Jenkins pipeline for automated deployments
- **Production Server**: Gunicorn WSGI server
- **Static Files**: Optimized handling for production

### Deployment Features
- Automated deployment on GitHub pushes
- SSL certificate management
- Production-grade server configuration
- Optimized static file serving
- Secure domain routing

## Technical Stack

### Backend
- **Framework**: Django
- **Database**: SQLite (Django ORM)
- **Authentication**: Django Authentication System
- **Template Engine**: Django Templates
- **AI/ML**: OpenCV, dlib, face_recognition
- **Server**: Gunicorn WSGI
- **Web Server**: Nginx
- **CI/CD**: Jenkins

### Frontend
- **HTML5 & CSS3**
- **Bootstrap 5**
- **JavaScript**
- **jQuery**

### Security
- Django's built-in security features
- CSRF protection
- Session management
- Password hashing
- Secure authentication
- SSL/TLS encryption
- Nginx security features

## Usage

### For Administrators
1. Log in to the admin dashboard
2. Manage users and departments
3. Configure attendance settings
4. Generate and export reports
5. Monitor attendance analytics

### For Users
1. Log in to the system
2. Register facial data (one-time setup)
3. Mark attendance through facial recognition
4. View attendance history
5. Access personal reports
6. Update profile information

## Project Structure
```
Smart-Attendance_Management_System/
├── home/                 # Main application directory
├── templates/           # HTML templates
├── static/             # Static files (CSS, JS, images)
├── web_project/        # Project settings
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── db.sqlite3         # Database file
```

## Development

### Key Components
- **Models**: User, Attendance, Department, FacialData
- **Views**: Authentication, Attendance, Reports, FaceRecognition
- **Templates**: Dashboard, Forms, Reports, FaceRegistration
- **Static Files**: CSS, JavaScript, Images
- **AI Components**: Face detection, recognition algorithms

### Database Schema
- User profiles with facial data
- Attendance records
- Department information
- System settings
- Facial recognition metadata

## Live Demo
Visit [https://smart.karthikchunchu.com](https://smart.karthikchunchu.com) to experience the live application.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author
- **Karthik Chunchu** - AI/ML Engineer & Full Stack Developer 
  - GitHub: [@Karthik80-hub](https://github.com/Karthik80-hub)
  - Live Demo: [Smart Attendance System](https://smart.karthikchunchu.com)

## Acknowledgments
- Django framework
- OpenCV community
- Bootstrap team
- AWS Cloud Services
- Jenkins CI/CD community
- All contributors to the project

## Contact
For any queries or support, please open an issue in the repository.
