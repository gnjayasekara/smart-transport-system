# Smart Transport System

## Project Overview
The Smart Transport System is a comprehensive digital solution designed to streamline transport operations in the city of Neotropolis. It integrates parking management, public transport access, real-time tracking, cashless payments, and traffic optimization into a user-friendly web application.

---

## Features

### 1. **Digital Transport Pass**
- Issue digital passes upon vehicle parking.
- Seamless access to public transport systems.
- Cashless payments for parking and public transport.

### 2. **Real-Time Transport Tracking**
- Real-time location updates for public transport vehicles.
- Accurate arrival times and route information.

### 3. **Integrated Payment System**
- Top-up transport passes directly through the web interface.
- Contactless payments for all transport-related services.

### 4. **Traffic Optimization and Management**
- Analyze traffic patterns to optimize signal timings.
- Suggest alternative routes to reduce travel time during congestion.

### 5. **User-Friendly Web Interface**
- Manage transport passes, payments, and journey history.
- Futuristic and responsive dashboard design.

---

## Technologies Used

### **Frontend**
- **React**: For building an interactive and responsive user interface.
- **Redux**: For managing application state.
- **Material-UI (MUI)**: For UI components and styling.
- **Axios**: For API integration.

### **Backend**
- **Django**: For handling backend logic and APIs.
- **Django REST Framework (DRF)**: For building and exposing RESTful APIs.
- **Django Channels**: For real-time data updates (e.g., WebSockets).

### **Database**
- **PostgreSQL**: For managing structured relational data.
- **MongoDB/Redis**: For handling real-time transport tracking data.

### **Other Tools & Services**
- **Docker**: For containerization and deployment.
- **Nginx**: For load balancing and serving static files.
- **Stripe API**: For payment processing.
- **Google Maps API**: For route suggestions and traffic data.
- **Firebase**: For notifications.

---

## Installation and Setup

### Prerequisites
1. Node.js and npm
2. Python 3.8+
3. PostgreSQL
4. MongoDB or Redis (optional for real-time tracking)
5. Docker (optional for deployment)

### Steps to Run Locally

#### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/neotropolis-transport-system.git
cd neotropolis-transport-system
```

#### 2. **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

#### 3. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### 4. **Database Configuration**
- Update `settings.py` in the Django project to connect to your PostgreSQL database.
- Example:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'neotropolis',
          'USER': 'yourusername',
          'PASSWORD': 'yourpassword',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

#### 5. **Environment Variables**
- Create a `.env` file in the root of the project for sensitive information:
  ```env
  SECRET_KEY=your_django_secret_key
  STRIPE_API_KEY=your_stripe_api_key
  GOOGLE_MAPS_API_KEY=your_google_maps_api_key
  ```

---

## Usage

1. **Accessing the Web App**
   - Open the web application in your browser at `http://localhost:3000`.
   - Sign up and log in to create and manage your transport pass.

2. **Admin Dashboard**
   - Access the admin dashboard for managing users, public transport, and parking lots via the Django admin interface at `http://localhost:8000/admin`.

3. **Real-Time Tracking**
   - View real-time transport locations and arrival times on the dashboard.

4. **Payments**
   - Top up transport passes and pay for services directly from the app.

---

## Future Enhancements

1. **AI-Powered Traffic Predictions**: Use machine learning to predict congestion patterns.
2. **Mobile App**: Develop a companion app for Android and iOS.
3. **Multilingual Support**: Add language options for a global audience.
4. **Integration with Ride-Sharing**: Connect transport passes with ride-sharing services.

---

## Contributions
Contributors:
- Mr. Nimtharu Jayasekara (https://github.com/gnjayasekara)
- Mr.Tharindu Darshana (https://github.com/Thandu-darshana)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


