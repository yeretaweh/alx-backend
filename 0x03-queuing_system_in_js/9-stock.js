import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Redis client setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Products array
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
  { id: 5, name: 'Bag 250', price: 70, stock: 0 },
];

// Helper function to get item by id
const getItemById = (id) => listProducts.find((product) => product.id === id);

// Reserve stock by id in Redis
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Get current reserved stock by id from Redis
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock, 10) : null;
};

// Express app
const app = express();
const port = 1245;

// Route to list all products
app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

// Route to get product details by item id
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? currentStock : product.stock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Route to reserve a product by item id
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableStock = currentStock !== null ? currentStock : product.stock;

  if (availableStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  // Decrease the stock by 1
  await reserveStockById(itemId, availableStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
