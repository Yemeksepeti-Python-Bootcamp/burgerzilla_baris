# **Burgerzilla - Python Flask Web Development Capstone Project**

## Overview
A REST-API micro-service that takes orders from hamburger restaurants, can view the status of the order, and enables transactions with the customer/restaurant authority regarding the order. Written with Flask and love. 

Mostly used libraries
- `flask` 
- `flask_bcrypt` 
- `flask_cors`  
- `flask_jwt_extended` 
- `flask_migrate`  
- `flask_sqlalchemy`
- `flask_marshmallow`

## Installation
- Clone repo
```
https://github.com/thealibrs/burgerzilla.git
``` 
- Go to project directory and run the following
```
docker build -t burgerzilla:latest .
```
- Run following
```
docker compose up --build web
```

- **API documentation** [Postman Documentation](https://documenter.getpostman.com/view/15782430/UVeNm2dM) 

- Also all endpoints are available in the Postman Collection that named **BurgerZilla.postman_collection.json**


## Endpoints

- ### Endpoints for Customer
| Method | Endpoint    | DESCRIPTON                        |
| :-------- | :------- | :-------------------------------- | 
| `POST`| `http://127.0.0.1:5000/auth/user_login` | User Login | 
| `POST`| `http://127.0.0.1:5000/auth/user_register` | User Register | 
| `POST`| `http://127.0.0.1:5000/api/user/order/<int:restaurant-id>` | Create an order | 
| `GET`| `http://127.0.0.1:5000/api/user/orders/<int:restaurant-id>` | Get Specific Order | 
| `GET`| `http://127.0.0.1:5000/api/user/orders` | Get All Orders |
| `GET`| `http://127.0.0.1:5000/api/user/orders/active_orders` | Get Active Orders |  
| `PUT`| `http://127.0.0.1:5000/api/user/order/<int:order-id>` | Cancel Order | 
| `GET`| `http://127.0.0.1:5000/api/user/restaurants` | Get All Restaurants | 
| `GET`| `http://127.0.0.1:5000/api/user/restaurant/<int:restaurant-id>` | Get Specific Restaurant | 

- ### Endpoints for Restaurant
| Method | Endpoint    | DESCRIPTON                        |
| :-------- | :------- | :-------------------------------- | 
| `POST`| `http://127.0.0.1:5000/auth/restaurant_register` | Restaurant Login | 
| `POST`| `http://127.0.0.1:5000/auth/restaurant_login` | Restaurant Register | 
| `POST`| `http://127.0.0.1:5000/api/restaurant/menu` | Create a Menu | 
| `GET`| `http://127.0.0.1:5000/api/restaurant/menu` | Get Menu Details | 
| `PUT`| `http://127.0.0.1:5000/api/restaurant/menu/<int:menu-id>` | Update Menu | 
| `DELETE`| `http://127.0.0.1:5000/api/restaurant/menu/<int:menu-id>` | Delete Menu | 
| `DELETE`| `http://127.0.0.1:5000/api/restaurant/products/<int:product-id>` | Delete Product from Menu |
| `POST`| `http://127.0.0.1:5000/api/restaurant/menu/add` | Add Product to Menu |
| `GET`| `http://127.0.0.1:5000/api/restaurant/products` | Get All Products |
| `PUT`| `http://127.0.0.1:5000/api/restaurant/product/<int:product-id>` | Update Product|
| `GET`| `http://127.0.0.1:5000/api/restaurant/orders` | Get All Orders|
| `PUT`| `http://127.0.0.1:5000/api/restaurant/order/update/<int:order-id>` | Update Order Status|
| `PUT`| `http://127.0.0.1:5000/api/restaurant/order/cancel/<int:order-id>` | Cancel Order|


## Database Schema
![Database Schema](https://i.hizliresim.com/a5zl3po.png)

## Folder Structure

```
BURGERZILLA
├── app
│   ├── api
│   │   ├── menu
│   │   │   ├── init.py
│   │   │   ├── dto.py
│   │   │   └── utils.py
│   │   ├── order
│   │   │   ├── dto.py
│   │   │   └── utils.py
│   │   ├── order_detail
│   │   │   ├── dto.py
│   │   │   └── utils.py
│   │   ├── product
│   │   │   ├── init.py
│   │   │   ├── dto.py
│   │   │   └── utils.py
│   │   ├── restaurant
│   │   │   ├── init.py
│   │   │   ├── controller.py
│   │   │   ├── dto.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   ├── user
│   │   │   ├── init.py
│   │   │   ├── controller.py
│   │   │   ├── dto.py
│   │   │   ├── service.py
│   │   │   └── utils.py
│   │   └── init.py  
│   ├── auth
│   │   ├── init.py
│   │   ├── controller.py
│   │   ├── dto.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── models
│   │   ├── menu
│   │   │   ├── menu.py
│   │   │   └── menu_schema.py
│   │   ├── order_detail
│   │   │   ├── order_detail.py
│   │   │   └── order_detail_schema.py
│   │   ├── orders
│   │   │   ├── orders.py
│   │   │   └── orders_schema.py
│   │   ├── product
│   │   │   ├── product.py
│   │   │   └── product_schema.py
│   │   ├── restaurant
│   │   │   ├── restaurant.py
│   │   │   └── restaurant_schema.py
│   │   └── user
│   │       ├── user.py
│   │       └── user_schema.py
│   ├── utils
│   │   ├── helpers
│   │   │   ├── database_helper.py
│   │   │   └── string_helper.py
│   │   └── messages
│   │       └── responses.py
│   ├── init.py
│   └── extensions.py
├── venv
├── migrations
├── tests
├── .venv
├── boot.sh
├── config.p
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── runservice.py
```