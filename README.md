# Amazon Clone - Django E-commerce Platform

A full-featured e-commerce platform built with Django, inspired by Amazon's functionality. This project includes product management, shopping cart, order processing, user authentication, and multi-language support.

## 🚀 Features

### Core E-commerce Features
- **Product Management**: Complete product catalog with categories, brands, and detailed product information
- **Shopping Cart**: Add/remove products, quantity management, and cart persistence
- **Order Management**: Full order lifecycle from cart to delivery tracking
- **User Authentication**: JWT-based authentication with registration and login
- **Product Reviews**: User reviews and ratings system
- **Coupon System**: Discount coupons with expiration dates and usage limits
- **Search & Filtering**: Advanced product search with filters and sorting options

### Technical Features
- **REST API**: Complete RESTful API for all functionalities
- **Multi-language Support**: Arabic and English localization
- **Responsive Design**: Mobile-friendly interface
- **Admin Panel**: Django admin interface for content management
- **Image Management**: Product image uploads and gallery
- **Pagination**: Efficient data pagination for large datasets

## 🛠️ Technology Stack

- **Backend**: Django 5.1.2, Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: JWT (Simple JWT)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Image Processing**: Pillow
- **Internationalization**: Django i18n framework
- **Additional Libraries**:
  - django-filter (filtering)
  - django-taggit (tagging system)
  - django-debug-toolbar (development)
  - Faker (dummy data generation)

## 📁 Project Structure

```
src/
├── product/           # Product management app
├── orders/            # Cart and order management
├── settings/          # Company settings and configuration
├── project/           # Main Django project settings
├── templates/         # HTML templates
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploaded files
├── locale/           # Translation files
└── utils/            # Utility functions
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hossamesmail2003/Amazon-clone.git
   cd Amazon-clone/src
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Generate dummy data (optional)**
   ```bash
   python dummy_data.py
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API endpoints: http://127.0.0.1:8000/products/api/

## 📚 API Documentation

### Authentication Endpoints
- `POST /dj-rest-auth/login/` - User login
- `POST /dj-rest-auth/registration/` - User registration
- `POST /dj-rest-auth/logout/` - User logout

### Product Endpoints
- `GET /products/api/` - List all products (with filtering, search, pagination)
- `GET /products/api/{id}/` - Get product details
- `GET /products/brands/api/` - List all brands
- `GET /products/brands/api/{id}/` - Get brand details

### Cart & Order Endpoints
- `GET /orders/cart/{username}/` - Get user's cart
- `POST /orders/cart/{username}/` - Add product to cart
- `DELETE /orders/cart/{username}/` - Remove product from cart
- `GET /orders/create-order/{username}/` - Create order from cart
- `GET /orders/{username}/` - List user's orders
- `POST /orders/apply-coupon/{username}/` - Apply coupon to cart

### Filtering & Search
Products can be filtered by:
- `flag` - Product flags (Sale, New, Feature)
- `brand` - Brand ID
- `search` - Search in name, subtitle, description
- `ordering` - Sort by price, quantity

Example: `/products/api/?flag=Sale&brand=1&search=laptop&ordering=price`

## 🌐 Multi-language Support

The application supports both English and Arabic:
- Language switching via `/i18n/setlang/`
- RTL support for Arabic
- Translated interface elements
- Admin interface for managing translations via Rosetta

## 🎨 Frontend Features

- Responsive design with Bootstrap
- Product image galleries
- Shopping cart with real-time updates
- User-friendly product filtering
- Multi-language interface
- Clean and modern UI

## 🔧 Development Features

- Django Debug Toolbar for development
- Comprehensive admin interface
- Automated slug generation
- Image optimization
- Code generation utilities
- Faker integration for test data

## 📝 Models Overview

### Product App
- **Product**: Main product model with images, pricing, inventory
- **Brand**: Product brands with logos
- **ProductImages**: Additional product images
- **Review**: User reviews and ratings

### Orders App
- **Cart**: Shopping cart management
- **CartDetail**: Individual cart items
- **Order**: Order information and tracking
- **OrderDetail**: Order line items
- **Coupon**: Discount coupon system

### Settings App
- **Company**: Site configuration and company information

## 🚧 Roadmap

Based on the todo.md file, upcoming features include:
- [ ] Enhanced API documentation with Postman
- [ ] User management improvements
- [ ] Advanced order tracking
- [ ] Enhanced cart functionality
- [ ] Extended coupon system
- [ ] Docker containerization
- [ ] Celery for background tasks
- [ ] Redis caching
- [ ] Production deployment
- [ ] AJAX enhancements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Hossam Esmail**
- GitHub: [@Hossamesmail2003](https://github.com/Hossamesmail2003)
- Project Link: [https://github.com/Hossamesmail2003/Amazon-clone](https://github.com/Hossamesmail2003/Amazon-clone)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap for the responsive design components
- All contributors and testers

---

⭐ If you found this project helpful, please give it a star on GitHub!
