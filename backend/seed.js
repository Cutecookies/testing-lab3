const mongoose = require('mongoose');
const dns = require('dns');
dns.setServers(['8.8.8.8', '8.8.4.4']);
require('dotenv').config();
const Product = require('./models/ProductModel'); 

const products = [
  {
    title: "Игрушка Freddy",
    category: "Toys",
    description: "Мягкая игрушка Freddy",
    brand: "ToysCreation",
    price: 25,
    rating: 4.5,
    images: ["/images/freddy.jpg"],
    quantity: 10,
    sizes: ["15cm", "50cm", "65cm"]
  },
  {
    title: "Игрушка Bonnie",
    category: "Toys",
    description: "Мягкая игрушка Bonnie",
    brand: "ToysCreation",
    price: 20,
    rating: 4.2,
    images: ["/images/bonnie.png"],
    quantity: 5,
    sizes: ["15cm", "50cm"]
  },
  {
    title: "Игрушка Foxy",
    category: "Toys",
    description: "Мягкая игрушка Foxy",
    brand: "ToysCreation",
    price: 25,
    rating: 4.8,
    images: ["/images/foxy.jpg"],
    quantity: 5,
    sizes: ["15cm", "50cm", "65cm", "80cm"]
  },
  {
    title: "Игрушка Chica",
    category: "Toys",
    description: "Мягкая игрушка Chica",
    brand: "ToysCreation",
    price: 20,
    rating: 4.2,
    images: ["/images/chica.jpg"],
    quantity: 5,
    sizes: ["15cm", "65cm"]
  }
];

mongoose.connect(process.env.MONGO_URI)
  .then(async () => {
    console.log("Connected to DB. Adding products...");
    await Product.deleteMany({}); 
    await Product.insertMany(products);
    console.log("Products added successfully!");
    process.exit(0);
  })
  .catch(err => {
    console.error("Error:", err);
    process.exit(1);
  });