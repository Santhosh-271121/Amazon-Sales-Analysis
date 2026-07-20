{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "36f67fb0-a21a-47bf-a696-473d5cd3874d",
   "metadata": {},
   "source": [
    "<h1 style=\"color:#3B82F6;\">🛒 Amazon Sales Analysis</h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fac189dd-1ddc-4599-b704-633c7a40a02f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "df = pd.read_csv(r\"C:\\\\Users\\\\santh\\\\OneDrive\\\\Amazon Sales Anonalysis\\\\Dataset\\Amaz.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c6e693c-d804-481b-a681-de5427d1b700",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#3B82F6;\">🧹 Data Cleaning</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5631f2d0-716a-4ccb-a317-6d648edd87d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>OrderID</th>\n",
       "      <th>OrderDate</th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>CustomerName</th>\n",
       "      <th>ProductID</th>\n",
       "      <th>ProductName</th>\n",
       "      <th>Category</th>\n",
       "      <th>Brand</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>UnitPrice</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Tax</th>\n",
       "      <th>ShippingCost</th>\n",
       "      <th>TotalAmount</th>\n",
       "      <th>PaymentMethod</th>\n",
       "      <th>OrderStatus</th>\n",
       "      <th>City</th>\n",
       "      <th>State</th>\n",
       "      <th>Country</th>\n",
       "      <th>SellerID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ORD0000001</td>\n",
       "      <td>2023-01-31</td>\n",
       "      <td>CUST001504</td>\n",
       "      <td>Vihaan Sharma</td>\n",
       "      <td>P00014</td>\n",
       "      <td>Drone Mini</td>\n",
       "      <td>Books</td>\n",
       "      <td>BrightLux</td>\n",
       "      <td>3</td>\n",
       "      <td>106.59</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.09</td>\n",
       "      <td>319.86</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Washington</td>\n",
       "      <td>DC</td>\n",
       "      <td>India</td>\n",
       "      <td>SELL01967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ORD0000002</td>\n",
       "      <td>2023-12-30</td>\n",
       "      <td>CUST000178</td>\n",
       "      <td>Pooja Kumar</td>\n",
       "      <td>P00040</td>\n",
       "      <td>Microphone</td>\n",
       "      <td>Home &amp; Kitchen</td>\n",
       "      <td>UrbanStyle</td>\n",
       "      <td>1</td>\n",
       "      <td>251.37</td>\n",
       "      <td>0.05</td>\n",
       "      <td>19.10</td>\n",
       "      <td>1.74</td>\n",
       "      <td>259.64</td>\n",
       "      <td>Amazon Pay</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Fort Worth</td>\n",
       "      <td>TX</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL01298</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ORD0000003</td>\n",
       "      <td>2022-05-10</td>\n",
       "      <td>CUST047516</td>\n",
       "      <td>Sneha Singh</td>\n",
       "      <td>P00044</td>\n",
       "      <td>Power Bank 20000mAh</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>UrbanStyle</td>\n",
       "      <td>3</td>\n",
       "      <td>35.03</td>\n",
       "      <td>0.10</td>\n",
       "      <td>7.57</td>\n",
       "      <td>5.91</td>\n",
       "      <td>108.06</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Austin</td>\n",
       "      <td>TX</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL00908</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ORD0000004</td>\n",
       "      <td>2023-07-18</td>\n",
       "      <td>CUST030059</td>\n",
       "      <td>Vihaan Reddy</td>\n",
       "      <td>P00041</td>\n",
       "      <td>Webcam Full HD</td>\n",
       "      <td>Home &amp; Kitchen</td>\n",
       "      <td>Zenith</td>\n",
       "      <td>5</td>\n",
       "      <td>33.58</td>\n",
       "      <td>0.15</td>\n",
       "      <td>11.42</td>\n",
       "      <td>5.53</td>\n",
       "      <td>159.66</td>\n",
       "      <td>Cash on Delivery</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Charlotte</td>\n",
       "      <td>NC</td>\n",
       "      <td>India</td>\n",
       "      <td>SELL01164</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ORD0000005</td>\n",
       "      <td>2023-02-04</td>\n",
       "      <td>CUST048677</td>\n",
       "      <td>Aditya Kapoor</td>\n",
       "      <td>P00029</td>\n",
       "      <td>T-Shirt</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>KiddoFun</td>\n",
       "      <td>2</td>\n",
       "      <td>515.64</td>\n",
       "      <td>0.25</td>\n",
       "      <td>38.67</td>\n",
       "      <td>9.23</td>\n",
       "      <td>821.36</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>Cancelled</td>\n",
       "      <td>San Antonio</td>\n",
       "      <td>TX</td>\n",
       "      <td>Canada</td>\n",
       "      <td>SELL01411</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>ORD0000006</td>\n",
       "      <td>2022-12-31</td>\n",
       "      <td>CUST042705</td>\n",
       "      <td>Karan Sharma</td>\n",
       "      <td>P00023</td>\n",
       "      <td>Cookware Set</td>\n",
       "      <td>Books</td>\n",
       "      <td>ReadMore</td>\n",
       "      <td>4</td>\n",
       "      <td>449.73</td>\n",
       "      <td>0.00</td>\n",
       "      <td>215.87</td>\n",
       "      <td>2.74</td>\n",
       "      <td>2017.53</td>\n",
       "      <td>UPI</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>CA</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL01494</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ORD0000007</td>\n",
       "      <td>2024-09-20</td>\n",
       "      <td>CUST037667</td>\n",
       "      <td>Aarav Verma</td>\n",
       "      <td>P00030</td>\n",
       "      <td>Dress Shirt</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>UrbanStyle</td>\n",
       "      <td>2</td>\n",
       "      <td>219.81</td>\n",
       "      <td>0.20</td>\n",
       "      <td>28.14</td>\n",
       "      <td>14.97</td>\n",
       "      <td>394.81</td>\n",
       "      <td>UPI</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Chicago</td>\n",
       "      <td>IL</td>\n",
       "      <td>Australia</td>\n",
       "      <td>SELL01676</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ORD0000008</td>\n",
       "      <td>2022-11-10</td>\n",
       "      <td>CUST031165</td>\n",
       "      <td>Rohit Kumar</td>\n",
       "      <td>P00028</td>\n",
       "      <td>Jeans</td>\n",
       "      <td>Toys &amp; Games</td>\n",
       "      <td>KiddoFun</td>\n",
       "      <td>2</td>\n",
       "      <td>306.51</td>\n",
       "      <td>0.05</td>\n",
       "      <td>29.12</td>\n",
       "      <td>6.24</td>\n",
       "      <td>617.73</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Pending</td>\n",
       "      <td>Denver</td>\n",
       "      <td>CO</td>\n",
       "      <td>India</td>\n",
       "      <td>SELL00510</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>ORD0000009</td>\n",
       "      <td>2024-06-26</td>\n",
       "      <td>CUST026965</td>\n",
       "      <td>Aman Kapoor</td>\n",
       "      <td>P00031</td>\n",
       "      <td>Kids Toy Car</td>\n",
       "      <td>Sports &amp; Outdoors</td>\n",
       "      <td>Apex</td>\n",
       "      <td>4</td>\n",
       "      <td>146.09</td>\n",
       "      <td>0.00</td>\n",
       "      <td>46.75</td>\n",
       "      <td>7.03</td>\n",
       "      <td>638.14</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Washington</td>\n",
       "      <td>DC</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL01895</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ORD0000010</td>\n",
       "      <td>2020-05-01</td>\n",
       "      <td>CUST029472</td>\n",
       "      <td>Aarav Reddy</td>\n",
       "      <td>P00001</td>\n",
       "      <td>Wireless Earbuds</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>Apex</td>\n",
       "      <td>2</td>\n",
       "      <td>278.21</td>\n",
       "      <td>0.10</td>\n",
       "      <td>60.09</td>\n",
       "      <td>4.88</td>\n",
       "      <td>565.75</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Houston</td>\n",
       "      <td>TX</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL01584</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      OrderID   OrderDate  CustomerID   CustomerName ProductID  \\\n",
       "0  ORD0000001  2023-01-31  CUST001504  Vihaan Sharma    P00014   \n",
       "1  ORD0000002  2023-12-30  CUST000178    Pooja Kumar    P00040   \n",
       "2  ORD0000003  2022-05-10  CUST047516    Sneha Singh    P00044   \n",
       "3  ORD0000004  2023-07-18  CUST030059   Vihaan Reddy    P00041   \n",
       "4  ORD0000005  2023-02-04  CUST048677  Aditya Kapoor    P00029   \n",
       "5  ORD0000006  2022-12-31  CUST042705   Karan Sharma    P00023   \n",
       "6  ORD0000007  2024-09-20  CUST037667    Aarav Verma    P00030   \n",
       "7  ORD0000008  2022-11-10  CUST031165    Rohit Kumar    P00028   \n",
       "8  ORD0000009  2024-06-26  CUST026965    Aman Kapoor    P00031   \n",
       "9  ORD0000010  2020-05-01  CUST029472    Aarav Reddy    P00001   \n",
       "\n",
       "           ProductName           Category       Brand  Quantity  UnitPrice  \\\n",
       "0           Drone Mini              Books   BrightLux         3     106.59   \n",
       "1           Microphone     Home & Kitchen  UrbanStyle         1     251.37   \n",
       "2  Power Bank 20000mAh           Clothing  UrbanStyle         3      35.03   \n",
       "3       Webcam Full HD     Home & Kitchen      Zenith         5      33.58   \n",
       "4              T-Shirt           Clothing    KiddoFun         2     515.64   \n",
       "5         Cookware Set              Books    ReadMore         4     449.73   \n",
       "6          Dress Shirt           Clothing  UrbanStyle         2     219.81   \n",
       "7                Jeans       Toys & Games    KiddoFun         2     306.51   \n",
       "8         Kids Toy Car  Sports & Outdoors        Apex         4     146.09   \n",
       "9     Wireless Earbuds           Clothing        Apex         2     278.21   \n",
       "\n",
       "   Discount     Tax  ShippingCost  TotalAmount     PaymentMethod OrderStatus  \\\n",
       "0      0.00    0.00          0.09       319.86        Debit Card   Delivered   \n",
       "1      0.05   19.10          1.74       259.64        Amazon Pay   Delivered   \n",
       "2      0.10    7.57          5.91       108.06        Debit Card   Delivered   \n",
       "3      0.15   11.42          5.53       159.66  Cash on Delivery   Delivered   \n",
       "4      0.25   38.67          9.23       821.36       Credit Card   Cancelled   \n",
       "5      0.00  215.87          2.74      2017.53               UPI   Delivered   \n",
       "6      0.20   28.14         14.97       394.81               UPI   Delivered   \n",
       "7      0.05   29.12          6.24       617.73        Debit Card     Pending   \n",
       "8      0.00   46.75          7.03       638.14        Debit Card   Delivered   \n",
       "9      0.10   60.09          4.88       565.75       Credit Card   Delivered   \n",
       "\n",
       "          City State        Country   SellerID  \n",
       "0   Washington    DC          India  SELL01967  \n",
       "1   Fort Worth    TX  United States  SELL01298  \n",
       "2       Austin    TX  United States  SELL00908  \n",
       "3    Charlotte    NC          India  SELL01164  \n",
       "4  San Antonio    TX         Canada  SELL01411  \n",
       "5  Los Angeles    CA  United States  SELL01494  \n",
       "6      Chicago    IL      Australia  SELL01676  \n",
       "7       Denver    CO          India  SELL00510  \n",
       "8   Washington    DC  United States  SELL01895  \n",
       "9      Houston    TX  United States  SELL01584  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "69caae77-83e1-4fd0-a935-fd3d6f567d2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Quantity</th>\n",
       "      <th>UnitPrice</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Tax</th>\n",
       "      <th>ShippingCost</th>\n",
       "      <th>TotalAmount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.001400</td>\n",
       "      <td>302.905748</td>\n",
       "      <td>0.074226</td>\n",
       "      <td>68.468902</td>\n",
       "      <td>7.406660</td>\n",
       "      <td>918.256479</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.413548</td>\n",
       "      <td>171.840797</td>\n",
       "      <td>0.082583</td>\n",
       "      <td>74.131180</td>\n",
       "      <td>4.324057</td>\n",
       "      <td>724.508332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.270000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>154.190000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>15.920000</td>\n",
       "      <td>3.680000</td>\n",
       "      <td>340.890000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>303.070000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>45.250000</td>\n",
       "      <td>7.300000</td>\n",
       "      <td>714.315000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>451.500000</td>\n",
       "      <td>0.100000</td>\n",
       "      <td>96.060000</td>\n",
       "      <td>11.150000</td>\n",
       "      <td>1349.765000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>599.990000</td>\n",
       "      <td>0.300000</td>\n",
       "      <td>538.460000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>3534.980000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Quantity      UnitPrice       Discount            Tax  \\\n",
       "count  100000.000000  100000.000000  100000.000000  100000.000000   \n",
       "mean        3.001400     302.905748       0.074226      68.468902   \n",
       "std         1.413548     171.840797       0.082583      74.131180   \n",
       "min         1.000000       5.000000       0.000000       0.000000   \n",
       "25%         2.000000     154.190000       0.000000      15.920000   \n",
       "50%         3.000000     303.070000       0.050000      45.250000   \n",
       "75%         4.000000     451.500000       0.100000      96.060000   \n",
       "max         5.000000     599.990000       0.300000     538.460000   \n",
       "\n",
       "        ShippingCost    TotalAmount  \n",
       "count  100000.000000  100000.000000  \n",
       "mean        7.406660     918.256479  \n",
       "std         4.324057     724.508332  \n",
       "min         0.000000       4.270000  \n",
       "25%         3.680000     340.890000  \n",
       "50%         7.300000     714.315000  \n",
       "75%        11.150000    1349.765000  \n",
       "max        15.000000    3534.980000  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ac29533c-a30c-462f-b844-b9514532a21f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100000, 20)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7cb183a4-bff2-4407-bd3a-5989c39edc3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.DataFrame'>\n",
      "RangeIndex: 100000 entries, 0 to 99999\n",
      "Data columns (total 20 columns):\n",
      " #   Column         Non-Null Count   Dtype  \n",
      "---  ------         --------------   -----  \n",
      " 0   OrderID        100000 non-null  str    \n",
      " 1   OrderDate      100000 non-null  str    \n",
      " 2   CustomerID     100000 non-null  str    \n",
      " 3   CustomerName   100000 non-null  str    \n",
      " 4   ProductID      100000 non-null  str    \n",
      " 5   ProductName    100000 non-null  str    \n",
      " 6   Category       100000 non-null  str    \n",
      " 7   Brand          100000 non-null  str    \n",
      " 8   Quantity       100000 non-null  int64  \n",
      " 9   UnitPrice      100000 non-null  float64\n",
      " 10  Discount       100000 non-null  float64\n",
      " 11  Tax            100000 non-null  float64\n",
      " 12  ShippingCost   100000 non-null  float64\n",
      " 13  TotalAmount    100000 non-null  float64\n",
      " 14  PaymentMethod  100000 non-null  str    \n",
      " 15  OrderStatus    100000 non-null  str    \n",
      " 16  City           100000 non-null  str    \n",
      " 17  State          100000 non-null  str    \n",
      " 18  Country        100000 non-null  str    \n",
      " 19  SellerID       100000 non-null  str    \n",
      "dtypes: float64(5), int64(1), str(14)\n",
      "memory usage: 15.3 MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ff12075c-a756-4f11-8838-c0e0d757069f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['OrderID', 'OrderDate', 'CustomerID', 'CustomerName', 'ProductID',\n",
       "       'ProductName', 'Category', 'Brand', 'Quantity', 'UnitPrice', 'Discount',\n",
       "       'Tax', 'ShippingCost', 'TotalAmount', 'PaymentMethod', 'OrderStatus',\n",
       "       'City', 'State', 'Country', 'SellerID'],\n",
       "      dtype='str')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c21fda39-7e80-40dd-8c7c-0868002e813b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OrderID          0\n",
       "OrderDate        0\n",
       "CustomerID       0\n",
       "CustomerName     0\n",
       "ProductID        0\n",
       "ProductName      0\n",
       "Category         0\n",
       "Brand            0\n",
       "Quantity         0\n",
       "UnitPrice        0\n",
       "Discount         0\n",
       "Tax              0\n",
       "ShippingCost     0\n",
       "TotalAmount      0\n",
       "PaymentMethod    0\n",
       "OrderStatus      0\n",
       "City             0\n",
       "State            0\n",
       "Country          0\n",
       "SellerID         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "db137e2f-96e7-455a-954e-22337fbad182",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e0c863e2-ea3b-4f7c-ab9a-9843eeb4b76d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OrderID              str\n",
       "OrderDate            str\n",
       "CustomerID           str\n",
       "CustomerName         str\n",
       "ProductID            str\n",
       "ProductName          str\n",
       "Category             str\n",
       "Brand                str\n",
       "Quantity           int64\n",
       "UnitPrice        float64\n",
       "Discount         float64\n",
       "Tax              float64\n",
       "ShippingCost     float64\n",
       "TotalAmount      float64\n",
       "PaymentMethod        str\n",
       "OrderStatus          str\n",
       "City                 str\n",
       "State                str\n",
       "Country              str\n",
       "SellerID             str\n",
       "dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8e42c0e6-1eb9-4454-84f9-2786dc713050",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['OrderDate'] = pd.to_datetime(df['OrderDate'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7839a54e-3e65-4355-b0e4-dfd49b989668",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OrderID                     str\n",
       "OrderDate        datetime64[us]\n",
       "CustomerID                  str\n",
       "CustomerName                str\n",
       "ProductID                   str\n",
       "ProductName                 str\n",
       "Category                    str\n",
       "Brand                       str\n",
       "Quantity                  int64\n",
       "UnitPrice               float64\n",
       "Discount                float64\n",
       "Tax                     float64\n",
       "ShippingCost            float64\n",
       "TotalAmount             float64\n",
       "PaymentMethod               str\n",
       "OrderStatus                 str\n",
       "City                        str\n",
       "State                       str\n",
       "Country                     str\n",
       "SellerID                    str\n",
       "dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "33c71679-dec3-454a-8fc7-4f646fad5356",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Year'] = df['OrderDate'].dt.year\n",
    "df['Month'] = df['OrderDate'].dt.month_name()\n",
    "df['Day'] = df['OrderDate'].dt.day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e2a043b0-b7cb-4161-8813-313a942b7535",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>OrderID</th>\n",
       "      <th>OrderDate</th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>CustomerName</th>\n",
       "      <th>ProductID</th>\n",
       "      <th>ProductName</th>\n",
       "      <th>Category</th>\n",
       "      <th>Brand</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>UnitPrice</th>\n",
       "      <th>...</th>\n",
       "      <th>TotalAmount</th>\n",
       "      <th>PaymentMethod</th>\n",
       "      <th>OrderStatus</th>\n",
       "      <th>City</th>\n",
       "      <th>State</th>\n",
       "      <th>Country</th>\n",
       "      <th>SellerID</th>\n",
       "      <th>Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>Day</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ORD0000001</td>\n",
       "      <td>2023-01-31</td>\n",
       "      <td>CUST001504</td>\n",
       "      <td>Vihaan Sharma</td>\n",
       "      <td>P00014</td>\n",
       "      <td>Drone Mini</td>\n",
       "      <td>Books</td>\n",
       "      <td>BrightLux</td>\n",
       "      <td>3</td>\n",
       "      <td>106.59</td>\n",
       "      <td>...</td>\n",
       "      <td>319.86</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Washington</td>\n",
       "      <td>DC</td>\n",
       "      <td>India</td>\n",
       "      <td>SELL01967</td>\n",
       "      <td>2023</td>\n",
       "      <td>January</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ORD0000002</td>\n",
       "      <td>2023-12-30</td>\n",
       "      <td>CUST000178</td>\n",
       "      <td>Pooja Kumar</td>\n",
       "      <td>P00040</td>\n",
       "      <td>Microphone</td>\n",
       "      <td>Home &amp; Kitchen</td>\n",
       "      <td>UrbanStyle</td>\n",
       "      <td>1</td>\n",
       "      <td>251.37</td>\n",
       "      <td>...</td>\n",
       "      <td>259.64</td>\n",
       "      <td>Amazon Pay</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Fort Worth</td>\n",
       "      <td>TX</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL01298</td>\n",
       "      <td>2023</td>\n",
       "      <td>December</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ORD0000003</td>\n",
       "      <td>2022-05-10</td>\n",
       "      <td>CUST047516</td>\n",
       "      <td>Sneha Singh</td>\n",
       "      <td>P00044</td>\n",
       "      <td>Power Bank 20000mAh</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>UrbanStyle</td>\n",
       "      <td>3</td>\n",
       "      <td>35.03</td>\n",
       "      <td>...</td>\n",
       "      <td>108.06</td>\n",
       "      <td>Debit Card</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Austin</td>\n",
       "      <td>TX</td>\n",
       "      <td>United States</td>\n",
       "      <td>SELL00908</td>\n",
       "      <td>2022</td>\n",
       "      <td>May</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ORD0000004</td>\n",
       "      <td>2023-07-18</td>\n",
       "      <td>CUST030059</td>\n",
       "      <td>Vihaan Reddy</td>\n",
       "      <td>P00041</td>\n",
       "      <td>Webcam Full HD</td>\n",
       "      <td>Home &amp; Kitchen</td>\n",
       "      <td>Zenith</td>\n",
       "      <td>5</td>\n",
       "      <td>33.58</td>\n",
       "      <td>...</td>\n",
       "      <td>159.66</td>\n",
       "      <td>Cash on Delivery</td>\n",
       "      <td>Delivered</td>\n",
       "      <td>Charlotte</td>\n",
       "      <td>NC</td>\n",
       "      <td>India</td>\n",
       "      <td>SELL01164</td>\n",
       "      <td>2023</td>\n",
       "      <td>July</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ORD0000005</td>\n",
       "      <td>2023-02-04</td>\n",
       "      <td>CUST048677</td>\n",
       "      <td>Aditya Kapoor</td>\n",
       "      <td>P00029</td>\n",
       "      <td>T-Shirt</td>\n",
       "      <td>Clothing</td>\n",
       "      <td>KiddoFun</td>\n",
       "      <td>2</td>\n",
       "      <td>515.64</td>\n",
       "      <td>...</td>\n",
       "      <td>821.36</td>\n",
       "      <td>Credit Card</td>\n",
       "      <td>Cancelled</td>\n",
       "      <td>San Antonio</td>\n",
       "      <td>TX</td>\n",
       "      <td>Canada</td>\n",
       "      <td>SELL01411</td>\n",
       "      <td>2023</td>\n",
       "      <td>February</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      OrderID  OrderDate  CustomerID   CustomerName ProductID  \\\n",
       "0  ORD0000001 2023-01-31  CUST001504  Vihaan Sharma    P00014   \n",
       "1  ORD0000002 2023-12-30  CUST000178    Pooja Kumar    P00040   \n",
       "2  ORD0000003 2022-05-10  CUST047516    Sneha Singh    P00044   \n",
       "3  ORD0000004 2023-07-18  CUST030059   Vihaan Reddy    P00041   \n",
       "4  ORD0000005 2023-02-04  CUST048677  Aditya Kapoor    P00029   \n",
       "\n",
       "           ProductName        Category       Brand  Quantity  UnitPrice  ...  \\\n",
       "0           Drone Mini           Books   BrightLux         3     106.59  ...   \n",
       "1           Microphone  Home & Kitchen  UrbanStyle         1     251.37  ...   \n",
       "2  Power Bank 20000mAh        Clothing  UrbanStyle         3      35.03  ...   \n",
       "3       Webcam Full HD  Home & Kitchen      Zenith         5      33.58  ...   \n",
       "4              T-Shirt        Clothing    KiddoFun         2     515.64  ...   \n",
       "\n",
       "   TotalAmount     PaymentMethod  OrderStatus         City State  \\\n",
       "0       319.86        Debit Card    Delivered   Washington    DC   \n",
       "1       259.64        Amazon Pay    Delivered   Fort Worth    TX   \n",
       "2       108.06        Debit Card    Delivered       Austin    TX   \n",
       "3       159.66  Cash on Delivery    Delivered    Charlotte    NC   \n",
       "4       821.36       Credit Card    Cancelled  San Antonio    TX   \n",
       "\n",
       "         Country   SellerID  Year     Month Day  \n",
       "0          India  SELL01967  2023   January  31  \n",
       "1  United States  SELL01298  2023  December  30  \n",
       "2  United States  SELL00908  2022       May  10  \n",
       "3          India  SELL01164  2023      July  18  \n",
       "4         Canada  SELL01411  2023  February   4  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c7d9a0fa-1818-4b25-bf34-a1c7d1ee2908",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OrderID                     str\n",
       "OrderDate        datetime64[us]\n",
       "CustomerID                  str\n",
       "CustomerName                str\n",
       "ProductID                   str\n",
       "ProductName                 str\n",
       "Category                    str\n",
       "Brand                       str\n",
       "Quantity                  int64\n",
       "UnitPrice               float64\n",
       "Discount                float64\n",
       "Tax                     float64\n",
       "ShippingCost            float64\n",
       "TotalAmount             float64\n",
       "PaymentMethod               str\n",
       "OrderStatus                 str\n",
       "City                        str\n",
       "State                       str\n",
       "Country                     str\n",
       "SellerID                    str\n",
       "Year                      int32\n",
       "Month                       str\n",
       "Day                       int32\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ddc7d630-53f9-4b54-8590-b2357bab61c0",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#6366F1;\">📊 Exploratory Data Analysis</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12095078-811a-4b08-a820-361859960f90",
   "metadata": {},
   "source": [
    "<h4>Total Sales</h4>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6667e266-0159-45ce-9b4d-3126ff57fb95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(91825647.92)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['TotalAmount'].sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7441acf-e2c0-43f4-9145-27f23be87a37",
   "metadata": {},
   "source": [
    "<h4>Average Order Value</h4>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a84a17f6-01b5-4d0b-b468-b8323bfb8ec6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.float64(918.26)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['TotalAmount'].mean().round(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16f1f625-ad1f-4076-9f8e-68d266afb613",
   "metadata": {},
   "source": [
    "<h4>Total Number of Orders</h4>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "14c10c57-9993-422f-bd6d-f8ac5b00c214",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100000"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['OrderID'].nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e392ffe2-3c63-4391-a25c-25602dde481f",
   "metadata": {},
   "source": [
    "<h3>Top 10 Selling Products</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "179cc6c7-630a-4b34-bce5-bcf364c9495a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ProductName\n",
       "LED Desk Lamp          6344\n",
       "Water Bottle           6275\n",
       "Memory Card 128GB      6240\n",
       "Router                 6202\n",
       "Board Game             6200\n",
       "Microphone             6196\n",
       "Gaming Mouse           6170\n",
       "Electric Kettle        6165\n",
       "Mechanical Keyboard    6161\n",
       "Vacuum Cleaner         6139\n",
       "Name: Quantity, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_products = df.groupby(\"ProductName\")['Quantity'].sum().sort_values(ascending = False)\n",
    "top_product.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c16f5e8-8729-47dd-9aa2-b598c8c5244e",
   "metadata": {},
   "source": [
    "<h3>Sales by Category</h3>\n",
    "Which product category generates the highest revenue?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e06ea24f-a1f5-405a-a4f0-7934d4cedf22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Category\n",
      "Electronics          15584217.18\n",
      "Sports & Outdoors    15345571.88\n",
      "Books                15261837.01\n",
      "Clothing             15253397.50\n",
      "Toys & Games         15216684.99\n",
      "Home & Kitchen       15163939.36\n",
      "Name: TotalAmount, dtype: float64\n",
      "Top Category\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Category\n",
       "Electronics    15584217.18\n",
       "Name: TotalAmount, dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_sales = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending = False)\n",
    "print(category_sales)\n",
    "print(\"Top Category\")\n",
    "category_sales.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa2e2717-4935-4feb-ae52-4635fc8ffc10",
   "metadata": {},
   "source": [
    "<h3>Sales by Brand</h3>\n",
    "Which brands bring the highest revenue?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "2ea92988-dcdd-4908-b080-569c1fbfae02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Brand\n",
      "CoreTech      9343720.59\n",
      "KiddoFun      9324749.55\n",
      "ReadMore      9278406.63\n",
      "UrbanStyle    9249027.45\n",
      "Zenith        9239960.39\n",
      "Apex          9147604.72\n",
      "NexPro        9078824.97\n",
      "FitLife       9061444.68\n",
      "BrightLux     9056816.11\n",
      "HomeEase      9045092.83\n",
      "Name: TotalAmount, dtype: float64\n",
      "Top Brands:\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Brand\n",
       "CoreTech    9343720.59\n",
       "Name: TotalAmount, dtype: float64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_brands = df.groupby('Brand')['TotalAmount'].sum().sort_values(ascending = False)\n",
    "print(top_brands)\n",
    "print('Top Brands:')\n",
    "top_brands.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0da3654-3f53-4a0d-9b5b-c2ac3b4628c3",
   "metadata": {},
   "source": [
    "<h3>Sales by State</h3>\n",
    "Which states generate the highest sales?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f27354b2-5c64-40e9-8b97-3b1a105e9459",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "State\n",
      "TX    22862540.54\n",
      "CA    18231196.79\n",
      "NC     4747701.73\n",
      "WA     4660962.17\n",
      "PA     4650673.88\n",
      "CO     4638498.97\n",
      "IL     4632847.44\n",
      "OH     4615442.32\n",
      "IN     4609048.43\n",
      "FL     4597177.27\n",
      "NY     4554358.08\n",
      "DC     4520876.11\n",
      "AZ     4504324.19\n",
      "Name: TotalAmount, dtype: float64\n",
      "Top Sales generate State is\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "State\n",
       "TX    22862540.54\n",
       "Name: TotalAmount, dtype: float64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_sales_state = df.groupby('State')['TotalAmount'].sum().sort_values(ascending = False)\n",
    "print(top_sales_state)\n",
    "print('Top Sales generate State is')\n",
    "top_sales_state.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a32d069-510d-46fc-a1fe-0215acd5f719",
   "metadata": {},
   "source": [
    "<h3>Sales by Payment Method</h3>\n",
    "Which payment method contributes the most revenue?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "b4d25d89-f991-4ac7-858b-8550625459e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PaymentMethod\n",
      "Credit Card         32122158.69\n",
      "Debit Card          18538678.53\n",
      "UPI                 13896028.55\n",
      "Amazon Pay          13697498.42\n",
      "Net Banking          9055674.57\n",
      "Cash on Delivery     4515609.16\n",
      "Name: TotalAmount, dtype: float64\n",
      "Payment method contributes the most revenue is:\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "PaymentMethod\n",
       "Credit Card    32122158.69\n",
       "Name: TotalAmount, dtype: float64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "payment_sales = df.groupby('PaymentMethod')['TotalAmount'].sum().sort_values(ascending = False)\n",
    "print(payment_sales)\n",
    "print('Payment method contributes the most revenue is:')\n",
    "payment_sales.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6a05cf3-9f95-4cd6-b60c-1216cc119571",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#3B82F6;\">📈 Business Insights</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6acf1da6-35db-46db-a25a-8995702a59ee",
   "metadata": {},
   "source": [
    "<h3>Top 10 Selling Products (Bar Chart)</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "ae5e0f8a-9e26-4cb8-8764-7057215d1d04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/gAAALkCAYAAAC7uJ7DAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQABAABJREFUeJzsvQe4XUX1uD0JEELovYaiIL1IjxTpHaUqiIA0pYkEKaL0IogUaYIFKT9Byl9FujRp0jsCIgIKSlVKqEkg+3veeVz32/dwyj733pCw877Pc3Jz7zln79kza9astWbNzKCiKIokIiIiIiIiIp9qBk/oAoiIiIiIiIhI/9HBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcREZFKDBo0KB1xxBE9v5933nn5b//4xz96/rbGGmvk16QIdUN9iIiITCh08EVEpPbgdFV53XLLLeO9LGeddVbaeuut07zzzpvv+Y1vfKPlZ9988830zW9+M80666xp6qmnTmuuuWZ68MEHK91n3Lhx6YILLkgrrbRSmmmmmdK0006bPve5z6Uddtgh3X333amOzD///L3ac7bZZkurrbZa+v3vf5/qwBNPPJGDCOWAioiISJnJe/0mIiJSQ/7v//6v1+84vjfccMPH/r7ooouO97L86Ec/Sm+//XZaccUV00svvdTWQd94443TI488kg444IA0yyyzpJ/+9Kd5dvyBBx5ICy20UNv77LPPPunMM89MX/7yl9N2222XJp988vTUU0+la6+9Nn3mM59JK6+88nh4upSuv/76NCFZZpll0ne/+938/xdffDH97Gc/S1tssUUOrOy+++7p0+7gH3nkkVkGCGaIiIg0ooMvIiK15+tf/3qv35nBxsFv/Psnwa233tozez/NNNO0/Nz/+3//L915553psssuS1tttVX+21e+8pU8C3/44Yeniy66qOV3X3nllRwM2G233dLPf/7zXu/95Cc/Sa+99loaXwwZMiRNSOaee+5e7UrGwoILLphOOeWUlg7+hx9+mAMqE7rsIiIi/cUUfRERkZTSu+++m2d+hw8fnqaccsq08MILpxNPPDEVRdGrfnDM995773ThhRfmzwwdOjQtt9xy6bbbbqtUj/PNN1+lddo4+LPPPnuefQ5I1cfJ/8Mf/pBGjx7d8rvPPfdcLvcqq6zysfcidb1xKcC+++7b8+w4xGQa4PR2S+MafJY9cM9LL700HXvssWmeeebJdbb22munv//97x/7PlkHZBhMNdVUOcvh9ttv79e6/jnmmCNnZlAnQHo75aFtCXZ89rOfzc/M7DjcfPPNOa2fJREzzDBDzoB48sknP3bdO+64I62wwgr5WbgGmQKNxL3Yq6DTfgbw73//O+2yyy5prrnmymVaYIEF0h577JHGjBmTr8HSDmCpRuOykvvvvz+tv/76OdODuuO7O++8c5/qTEREPr04gy8iIpM8OMNf+tKX0p/+9KfsYJHm/cc//jGnxuN0MfvbOAt/ySWX5DR4HDFmyzfYYIN07733piWWWGJA6vOhhx5Kyy67bBo8uHcsHqeXWfm//e1vackll2wZRABm/3EKhw0b1vI+7733XvriF7+Yn/Nb3/pWzi4gc+Dggw/OSwhwggeC448/Pj/L/vvvn9566610wgkn5KUD99xzT89nSKMneIKDPXLkyOwgb7bZZmnGGWfMgYG+MHbs2PTCCy+kmWeeudffzz333PTBBx/kPQ5oQ/YpuPHGG9OGG26YAww43++//346/fTTc6CEvQ8iLf6xxx5L6623Xg648DkyAMiqICDTV1hOQNvGvguLLLJIbhMCPbTR6quvnuXttNNOS9///vd7lpPw89VXX+0pz/e+970cmKDufve73/W5PCIi8imlEBERmcTYa6+9mJbv+f3yyy/Pvx9zzDG9PrfVVlsVgwYNKv7+97/3/I3P8br//vt7/vbPf/6zGDp0aLH55pt3VY6pp5662HHHHVu+t/POO3/s71dffXW+/3XXXdf22jvssEP+3IwzzpjLdeKJJxZPPvnkxz539NFH53v97W9/6/X3733ve8Vkk01WPP/88z1/43qHH354z+/nnntu/ttzzz3X87cvfvGL+RX86U9/yp9ZdNFFi9GjR/f8/dRTT81/f+yxx/LvvDfzzDMXK6ywQjF27Niez5133nn5c+VrtmK++eYr1ltvveK1117Lr0ceeaTYZptt8ve//e1v589QVn6fbrrpildffbXX95dZZplittlmK/773//2/I1rDB48ONdnsNlmm+X2pt2DJ554ItdXWa7iXtRTI411yfW5z333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ERGRT4pulom7yZ6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1YPIJXYBPM/N/7+qOn/nH8Rt/ImURERERERGRSRtn8EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjXATfYmEtywT0RERERERPqDM/giIiIiIiIiNcAZ/EkwEwA8vk9ERERERKReOIMvIiIiIiIiUgN08EVERERERERqgCn6Mt43/hvIZQNuRigiIiIiItIcZ/BFREREREREaoAz+DLJYoaCiIiIiIjUCWfwRURERERERGqAM/giNcTjEkVEREREJj108EXkE9vYcGJcFiEiIiIiUhd08EVkksagg4iIiIjUBR18EZGJDI+DFBEREZG+oIMvIlJjJsYMBQMYIiIiIuMHHXwREflU4l4MIiIiIhPZMXn//ve/09e//vU088wzp6mmmiotueSS6f777+95vyiKdNhhh6U555wzv7/OOuukp59+utc1Xn/99bTddtul6aabLs0wwwxpl112Se+8806vzzz66KNptdVWS0OHDk3Dhw9PJ5xwwif2jCIiIiIiIiK1nsF/44030iqrrJLWXHPNdO2116ZZZ501O+8zzjhjz2dwxE877bR0/vnnpwUWWCAdeuihaf31109PPPFEdtYB5/6ll15KN9xwQxo7dmzaaaed0je/+c100UUX5fdHjRqV1ltvvRwcOPvss9Njjz2Wdt555xwM4HMiIjJp47IBERERqQMT1MH/0Y9+lGfTzz333J6/4cSXZ+9/8pOfpEMOOSR9+ctfzn+74IIL0uyzz54uv/zytM0226Qnn3wyXXfddem+++5Lyy+/fP7M6aefnjbaaKN04oknprnmmitdeOGFacyYMelXv/pVGjJkSFp88cXTww8/nE4++WQdfBEREREREakFE9TBv+KKK/Js/NZbb51uvfXWNPfcc6c999wz7bbbbvn95557Lr388st55j2Yfvrp00orrZTuuuuu7ODzk5n4cO6Bzw8ePDjdc889afPNN8+fWX311bNzH3BfAgxkEZQzBmD06NH5FZABICIi8mnd2FBEREQmDSaog//ss8+ms846K+23337p+9//fp6F32effbIjvuOOO2bnHpixL8Pv8R4/Z5tttl7vTz755GmmmWbq9ZlyZkD5mrzX6OAfd9xx6cgjjxwPTywiIvLJMzEGHQZyWYRLLERERCYCB3/cuHF55v2HP/xh/v3zn/98+stf/pLXyePgTygOPvjgHHQoz+CzlEBERETqy8QYwDCTQ0REPjUOPjvjL7bYYr3+tuiii6bf/va3+f9zzDFH/vnKK6/kzwb8vswyy/R85tVXX+11jQ8//DDvrB/f5yffKRO/x2fKTDnllPklIiIiUhfMdBARqT8T1MFnB/2nnnqq19/+9re/pfnmmy//n7R6HPCbbrqpx6FnNp219XvssUf+fcSIEenNN99MDzzwQFpuueXy326++eacHcBa/fjMD37wg7zD/hRTTJH/xo77Cy+88MfS80VERESkPWYoiIhMnExQB3/kyJHpC1/4Qk7R/8pXvpLuvffe9POf/zy/YNCgQWnfffdNxxxzTFpooYV6jsljZ/zNNtusZ8Z/gw02yBvzkdqPE7/33nvnDfj4HHzta1/La+p32WWXdNBBB+VlAKeeemo65ZRTJuTji4iIiMgAYdBBRGQCO/grrLBC+v3vf5/XvB911FHZgedYPM61Dw488MD07rvv5uPsmKlfddVV87F4Q4cO7fkMx+Dh1K+99tp59/wtt9wynXbaab123r/++uvTXnvtlWf5Z5lllnTYYYd5RJ6IiIiIjDdcFiEik5SDD5tsskl+tYJZfJx/Xq1gx/yLLrqo7X2WWmqpdPvtt/errCIiIiIiIiITKxPcwRcRERERkfaYDSAiVdDBFxERERGZRPA4SJF6o4MvIiIiIiK1wEwHmdTRwRcREREREWnAkxnk04gOvoiIiIiIyKcAMxSkE4M7fkJEREREREREJnqcwRcREREREZmEGMjNFmXiQgdfRERERERE+oTLBiYudPBFRERERERkgmOwoP+4Bl9ERERERESkBjiDLyIiIiIiIrVh/kl4jwFn8EVERERERERqgDP4IiIiIiIiIjXYF8AZfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjXAY/JEREREREREJvBxewNx5J4z+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqwAR18I844og0aNCgXq9FFlmk5/0PPvgg7bXXXmnmmWdO00wzTdpyyy3TK6+80usazz//fNp4443TsGHD0myzzZYOOOCA9OGHH/b6zC233JKWXXbZNOWUU6YFF1wwnXfeeZ/YM4qIiIiIiIhMEjP4iy++eHrppZd6XnfccUfPeyNHjkxXXnlluuyyy9Ktt96aXnzxxbTFFlv0vP/RRx9l537MmDHpzjvvTOeff3523g877LCezzz33HP5M2uuuWZ6+OGH07777pt23XXX9Mc//vETf1YRERERERGR8cXkE7wAk0+e5phjjo/9/a233krnnHNOuuiii9Jaa62V/3buueemRRddNN19991p5ZVXTtdff3164okn0o033phmn332tMwyy6Sjjz46HXTQQTk7YMiQIenss89OCyywQDrppJPyNfg+QYRTTjklrb/++p/484qIiIiIiIjUcgb/6aefTnPNNVf6zGc+k7bbbruccg8PPPBAGjt2bFpnnXV6Pkv6/rzzzpvuuuuu/Ds/l1xyyezcBzjto0aNSo8//njPZ8rXiM/ENZoxevTofI3yS0RERERERGRiZoI6+CuttFJOqb/uuuvSWWedldPpV1tttfT222+nl19+Oc/AzzDDDL2+gzPPe8DPsnMf78d77T6D0/7+++83Lddxxx2Xpp9++p7X8OHDB/S5RURERERERGqVor/hhhv2/H+ppZbKDv98882XLr300jTVVFNNsHIdfPDBab/99uv5nWCATr6IiIiIiIhMzEzwFP0yzNZ/7nOfS3//+9/zunw2z3vzzTd7fYZd9GPNPj8bd9WP3zt9ZrrppmsZRGC3fd4vv0REREREREQmZiYqB/+dd95JzzzzTJpzzjnTcsstl6aYYop000039bz/1FNP5TX6I0aMyL/z87HHHkuvvvpqz2duuOGG7JAvtthiPZ8pXyM+E9cQERERERERqQMT1MHff//98/F3//jHP/Ixd5tvvnmabLLJ0rbbbpvXvu+yyy45Vf5Pf/pT3nRvp512yo45O+jDeuutlx357bffPj3yyCP56LtDDjkk7bXXXnkWHnbffff07LPPpgMPPDD99a9/TT/96U/zEgCO4BMRERERERGpCxN0Df6//vWv7Mz/97//TbPOOmtaddVV8xF4/B84ym7w4MFpyy23zDvbs/s9DnpAMOCqq65Ke+yxR3b8p5566rTjjjumo446quczHJF39dVXZ4f+1FNPTfPMM0/65S9/6RF5IiIiIiIiUismqIN/8cUXt31/6NCh6cwzz8yvVrAp3zXXXNP2OmussUZ66KGH+lxOERERERERkYmdiWoNvoiIiIiIiIj0DR18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaMNE4+Mcff3waNGhQ2nfffXv+9sEHH6S99torzTzzzGmaaaZJW265ZXrllVd6fe/5559PG2+8cRo2bFiabbbZ0gEHHJA+/PDDXp+55ZZb0rLLLpumnHLKtOCCC6bzzjvvE3suERERERERkUnGwb/vvvvSz372s7TUUkv1+vvIkSPTlVdemS677LJ06623phdffDFtscUWPe9/9NFH2bkfM2ZMuvPOO9P555+fnffDDjus5zPPPfdc/syaa66ZHn744RxA2HXXXdMf//jHT/QZRURERERERGrt4L/zzjtpu+22S7/4xS/SjDPO2PP3t956K51zzjnp5JNPTmuttVZabrnl0rnnnpsd+bvvvjt/5vrrr09PPPFE+vWvf52WWWaZtOGGG6ajjz46nXnmmdnph7PPPjstsMAC6aSTTkqLLrpo2nvvvdNWW22VTjnllAn2zCIiIiIiIiK1c/BJwWeGfZ111un19wceeCCNHTu2198XWWSRNO+886a77ror/87PJZdcMs0+++w9n1l//fXTqFGj0uOPP97zmcZr85m4RjNGjx6dr1F+iYiIiIiIiEzMTD4hb37xxRenBx98MKfoN/Lyyy+nIUOGpBlmmKHX33HmeS8+U3bu4/14r91ncNrff//9NNVUU33s3scdd1w68sgjB+AJRURERERERGo+g//CCy+k73znO+nCCy9MQ4cOTRMTBx98cF4iEC/KKiIiIiIiIvKpn8F/9NFHK1+wcaO8VpCC/+qrr+bd7cub5t12223pjDPOyJvgsY7+zTff7DWLzy76c8wxR/4/P++9995e141d9sufadx5n9+nm266prP3wG77vERERERERERq5eCzgR1H2BVFkX+2Aye9CmuvvXZ67LHHev1tp512yuvsDzrooDR8+PA0xRRTpJtuuikfjwdPPfVUPhZvxIgR+Xd+HnvssTlQwBF5cMMNN2TnfbHFFuv5zDXXXNPrPnwmriEiIiIiIiIyyTj4HDUXPPTQQ2n//ffP582Hk8yGdexSf8IJJ1S+8bTTTpuWWGKJXn+beuqp85n38fdddtkl7bfffmmmmWbKTvu3v/3tfM+VV145v7/eeutlR3777bfP92a9/SGHHJI37osZ+N133z1nBBx44IFp5513TjfffHO69NJL09VXX125rCIiIiIiIiK1cPDnm2++nv9vvfXW6bTTTksbbbRRr7R8ZtwPPfTQtNlmmw1Y4TjKbvDgwXkGn53t2f3+pz/9ac/7k002WbrqqqvSHnvskR1/AgQ77rhjOuqoo3o+wxF5OPMjR45Mp556appnnnnSL3/5y3wtERERERERkUl2F33S6nGaG+FvnEnfH2655ZZev7P5Hmfa82oXfGhMwW9kjTXWyJkHIiIiIiIiInWl6130F1100XyMHBvgBfyfv/GeiIiIiIiIiHwKZvDPPvvstOmmm+ZU99gxn1322XzvyiuvHB9lFBEREREREZGBdvBXXHHF9Oyzz+bz6//617/mv331q19NX/va1/IaeBERERERERH5FDj4gCP/zW9+c+BLIyIiIiIiIiLjz8G/4oorKl/wS1/6Ut9KIiIiIiIiIiLj18GvevQd6/A/+uijvpdGRERERERERMafgz9u3Li+XV1EREREREREJs5j8kRERERERESkJg7+rbfemo/KW3DBBfOLdfe33377wJdORERERERERMaPg//rX/86rbPOOmnYsGFpn332ya+pppoqrb322umiiy7q9nIiIiIiIiIiMiGOyTv22GPTCSeckEaOHNnzN5z8k08+OR199NHpa1/72kCUS0RERERERETG5wz+s88+m9PzGyFN/7nnnuv2ciIiIiIiIiIyIRz84cOHp5tuuuljf7/xxhvzeyIiIiIiIiLyKUjR/+53v5tT8h9++OH0hS98If/tz3/+czrvvPPSqaeeOj7KKCIiIiIiIiID7eDvscceaY455kgnnXRSuvTSS/PfFl100XTJJZekL3/5y91eTkREREREREQmhIMPm2++eX6JiIiIiIiIyKfYwQ8++OCDPHP/3nvv5aPzFlpooYErmYiIiIiIiIgMvIO/3377pbFjx6bTTz89/z5mzJi08sorpyeeeCINGzYsHXDAAemGG25II0aMqH53EREREREREflkd9G//vrr07rrrtvz+4UXXpief/759PTTT6c33ngjbb311umYY44ZmFKJiIiIiIiIyPhx8HHmF1tssV4O/1ZbbZXmm2++NGjQoPSd73wnPfTQQ93dXUREREREREQ+WQd/8ODBqSiKnt/vvvvunKIfzDDDDHkmX0REREREREQmYgefo/CuvPLK/P/HH388z+ivueaaPe//85//TLPPPvv4KaWIiIiIiIiIDMwmewceeGDaZptt0tVXX50d/I022igtsMACPe9fc801acUVV6x6ORERERERERGZEDP4nHuPE7/UUkulkSNH5uPxyrCT/p577jmQZRMRERERERGRgZ7Bh7XXXju/mnH44Yd3cykRERERERERmRAz+CIiIiIiIiIy8aKDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiMik6OCzmR5n3ouIiIiIiIjIp9jB/8Mf/pA++9nP5t30L7roojR69OjxUzIRERERERERGX8O/sMPP5zuu+++tPjii6fvfOc7aY455kh77LFH/puIiIiIiIiIfIrW4H/+859Pp512WnrxxRfTOeeck/71r3+lVVZZJS211FLp1FNPTW+99dbAl1RERERERERExs8me0VRpLFjx6YxY8bk/88444zpjDPOSMOHD0+XXHJJfy4tIiIiIiIiIuPbwX/ggQfS3nvvneacc840cuTIPKP/5JNPpltvvTU9/fTT6dhjj0377LNPXy4tIiIiIiIiIp+Eg7/kkkumlVdeOT333HM5Pf+FF15Ixx9/fFpwwQV7PrPtttum1157rS/lEREREREREZE+MHm3X/jKV76Sdt555zT33HO3/Mwss8ySxo0b15fyiIiIiIiIiMgnMYMfa+0bef/999NRRx3VlzKIiIiIiIiIyCft4B955JHpnXfe+djf33vvvfyeiIiIiIiIiHxKZvAHDRr0sb8/8sgjaaaZZhqocomIiIiIiIjI+FiDT1o+jj2vz33uc72c/I8++ijP6u++++7d3FtEREREREREPmkH/yc/+UmevWeDPVLxp59++p73hgwZkuaff/40YsSIgSqXiIiIiIiIiIwPB3/HHXfMPxdYYIH0hS98IU0xxRTd3EdEREREREREJrSDP2rUqDTddNPl/3/+85/PO+bzakZ8TkREREREREQmMgef9fcvvfRSmm222dIMM8zQdJO92HyP9fgiIiIiIiIiMhE6+DfffHPPDvl/+tOfxneZRERERERERGR8OPhf/OIXe/7PGvzhw4d/bBafGfwXXnih2/uLiIiIiIiIyAAwuNsv4OC/9tprH/v766+/nt8TERERERERkU+Bgx9r7Rt555130tChQweqXCIiIiIiIiIyPo7J22+//fJPnPtDDz00DRs2rOc9Nta755570jLLLNPNvUVERERERETkk3bwH3rooZ4Z/MceeywNGTKk5z3+v/TSS6f9999/oMolIiIiIiIiIuPDwY/d83faaad06qmnet69iIiIiIiIyKfRwQ/OPffc8VMSEREREREREfnkHPx33303HX/88emmm25Kr776aho3blyv95999tm+l0ZEREREREREPhkHf9ddd0233npr2n777dOcc87ZdEd9EREREREREZnIHfxrr702XX311WmVVVYZPyUSERERERERka4Z3O0XZpxxxjTTTDN1fycRERERERERmXgc/KOPPjoddthh6b333hs/JRIRERERERGR8Z+if9JJJ6VnnnkmzT777Gn++edPU0wxRa/3H3zwwe5LISIiIiIiIiKf7Az+Zpttlr773e+m/fffP2211Vbpy1/+cq9XN5x11llpqaWWStNNN11+jRgxIq/xDz744IO01157pZlnnjlNM800acstt0yvvPJKr2s8//zzaeONN07Dhg1Ls802WzrggAPShx9+2Oszt9xyS1p22WXTlFNOmRZccMF03nnndfvYIiIiIiIiIvWawT/88MMH7ObzzDNPPnJvoYUWSkVRpPPPPz8HCR566KG0+OKLp5EjR+YN/S677LI0/fTTp7333jttscUW6c9//nP+/kcffZSd+znmmCPdeeed6aWXXko77LBDzir44Q9/mD/z3HPP5c/svvvu6cILL8zH+3ESACcArL/++gP2LCIiIiIiIiKfKgd/INl00017/X7sscfmWf277747O//nnHNOuuiii9Jaa62V3z/33HPToosumt9feeWV0/XXX5+eeOKJdOONN+YlA8sss0zeI+Cggw5KRxxxRBoyZEg6++yz0wILLJCXFgDfv+OOO9Ipp5yigy8iIiIiIiKTboo+s+YnnnhiWnHFFfPMOTvql199hetefPHF6d13382p+g888EAaO3ZsWmeddXo+s8gii6R555033XXXXfl3fi655JLZuQ+YlR81alR6/PHHez5TvkZ8Jq7RjNGjR+drlF8iIiIiIiIitXLwjzzyyHTyySenr371q+mtt95K++23X06bHzx4cJ4175bHHnssr69nfTxp9L///e/TYostll5++eU8Az/DDDP0+jzOPO8BP8vOfbwf77X7DE77+++/37RMxx13XF4SEK/hw4d3/VwiIiIiIiIiE7WDzzr2X/ziF3mjvcknnzxtu+226Ze//GU+Oo/U+W5ZeOGF08MPP5zuueeetMcee6Qdd9wxp91PSA4++OAcvIjXCy+8MEHLIyIiIiIiIjLga/CZESctHph5xwGGTTbZJB166KHdXi7P0rOzPSy33HLpvvvuS6eeemrOEBgzZkx68803e83is4s+SwOAn/fee2+v68Uu++XPNO68z+/s2j/VVFM1LRPZBLxEREREREREajuDz+Z37FYPn/3sZ/NGd4BjPhBO8bhx4/IaeJx9dsNn1/vgqaeeysfisUYf+EmK/6uvvtrzmRtuuCE776T5x2fK14jPxDVEREREREREJskZ/M033zw7zCuttFL69re/nb7+9a/n3e5xvDnWrttU+A033DBvnPf222/nHfM5s/6Pf/xjXvu+yy675DX+bN6H0879cMzZQR/WW2+97Mhvv/326YQTTsjZBYccckjaa6+9eoINrOs/44wz0oEHHph23nnndPPNN6dLL700H78nIiIiIiIiMsk6+JxbH5BGH7vac5Z947F3nWDmnXPryQjAoV9qqaWyc7/uuuvm9znKjs37ttxyyzyrz+73P/3pT3u+P9lkk6Wrrroqr93H8Z966qnzGv6jjjqq5zMckYczT/CB1H8yENgzgGuJiIiIiIiITLIOfiM41n1Nd2fmvx1Dhw5NZ555Zn61Yr755kvXXHNN2+usscYa6aGHHupTGUVERERERERq6eBfcMEFbd9nRl5EREREREREJnIH/zvf+U6v38eOHZvee++9vBv+sGHDdPBFREREREREPg276L/xxhu9Xu+8807e3X7VVVdNv/nNb8ZPKUVERERERERkYB38ZrDBHpvvNc7ui4iIiIiIiMinyMGHySefPL344osDdTkRERERERERGZ9r8K+44opevxdFkY+546z5VVZZpdvLiYiIiIiIiMiEcPA322yzXr8PGjQozTrrrGmttdZKJ5100kCUSURERERERETGt4M/bty4br8iIiIiIiIiIhPrGvz//Oc/adSoUQNbGhEREREREREZ/w7+m2++mfbaa680yyyzpNlnnz3NOOOMaY455kgHH3xweu+99/pWAhERERERERH55FL0X3/99TRixIj073//O2233XZp0UUXzX9/4okn0umnn55uuOGGdMcdd6RHH3003X333Wmfffbpf+lEREREREREZGAd/KOOOioNGTIkPfPMM3n2vvG99dZbL22//fbp+uuvT6eddlrVy4qIiIiIiIjIJ+ngX3755elnP/vZx5x7IE3/hBNOSBtttFE6/PDD04477jgQZRMRERERERGRgV6Dz1n3iy++eMv3l1hiiTR48ODs4IuIiIiIiIjIROrgs7HeP/7xj5bvP/fcc2m22WYbqHKJiIiIiIiIyPhw8Ndff/30gx/8II0ZM+Zj740ePTodeuihaYMNNujm3iIiIiIiIiIyITbZW3755dNCCy2Uj8pbZJFFUlEU6cknn0w//elPs5N/wQUXDFS5RERERERERGR8OPjzzDNPuuuuu9Kee+6Zz73HuYdBgwalddddN51xxhlp3nnn7ebeIiIiIiIiIvJJO/iwwAILpGuvvTa98cYb6emnn85/W3DBBdNMM800UOURERERERERkfHt4AczzjhjWnHFFfvyVRERERERERGZkJvsiYiIiIiIiMjEiw6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUgAnq4B933HFphRVWSNNOO22abbbZ0mabbZaeeuqpXp/54IMP0l577ZVmnnnmNM0006Qtt9wyvfLKK70+8/zzz6eNN944DRs2LF/ngAMOSB9++GGvz9xyyy1p2WWXTVNOOWVacMEF03nnnfeJPKOIiIiIiIhI7R38W2+9NTvvd999d7rhhhvS2LFj03rrrZfefffdns+MHDkyXXnllemyyy7Ln3/xxRfTFlts0fP+Rx99lJ37MWPGpDvvvDOdf/752Xk/7LDDej7z3HPP5c+sueaa6eGHH0777rtv2nXXXdMf//jHT/yZRURERERERMYHk6cJyHXXXdfrdxxzZuAfeOCBtPrqq6e33nornXPOOemiiy5Ka621Vv7MueeemxZddNEcFFh55ZXT9ddfn5544ol04403ptlnnz0ts8wy6eijj04HHXRQOuKII9KQIUPS2WefnRZYYIF00kkn5Wvw/TvuuCOdcsopaf31158gzy4iIiIiIiJS2zX4OPQw00wz5Z84+szqr7POOj2fWWSRRdK8886b7rrrrvw7P5dccsns3Ac47aNGjUqPP/54z2fK14jPxDUaGT16dP5++SUiIiIiIiIyMTPROPjjxo3LqfOrrLJKWmKJJfLfXn755TwDP8MMM/T6LM4878Vnys59vB/vtfsMjvv777/fdG+A6aefvuc1fPjwAX5aERERERERkZo6+KzF/8tf/pIuvvjiCV2UdPDBB+dsgni98MILE7pIIiIiIiIiIhPvGvxg7733TldddVW67bbb0jzzzNPz9znmmCNvnvfmm2/2msVnF33ei8/ce++9va4Xu+yXP9O48z6/TzfddGmqqab6WHnYaZ+XiIiIiIiIyKeFCTqDXxRFdu5///vfp5tvvjlvhFdmueWWS1NMMUW66aabev7GMXocizdixIj8Oz8fe+yx9Oqrr/Z8hh35cd4XW2yxns+UrxGfiWuIiIiIiIiIfNqZfEKn5bND/h/+8Ic07bTT9qyZZ907M+v83GWXXdJ+++2XN97Daf/2t7+dHXN20AeO1cOR33777dMJJ5yQr3HIIYfka8cs/O67757OOOOMdOCBB6add945BxMuvfTSdPXVV0/IxxcRERERERGpxwz+WWedlde4r7HGGmnOOefseV1yySU9n+Eou0022SRtueWW+eg80u1/97vf9bw/2WST5fR+fuL4f/3rX0877LBDOuqoo3o+Q2YAzjyz9ksvvXQ+Lu+Xv/ylR+SJiIiIiIhIbZh8Qqfod2Lo0KHpzDPPzK9WzDfffOmaa65pex2CCA899FCfyikiIiIiIiIysTPR7KIvIiIiIiIiIn1HB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAZMUAf/tttuS5tuummaa6650qBBg9Lll1/e6/2iKNJhhx2W5pxzzjTVVFOlddZZJz399NO9PvP666+n7bbbLk033XRphhlmSLvsskt65513en3m0UcfTauttloaOnRoGj58eDrhhBM+kecTERERERERmSQc/HfffTctvfTS6cwzz2z6Po74aaedls4+++x0zz33pKmnnjqtv/766YMPPuj5DM79448/nm644YZ01VVX5aDBN7/5zZ73R40aldZbb70033zzpQceeCD9+Mc/TkcccUT6+c9//ok8o4iIiIiIiMgnweRpArLhhhvmVzOYvf/JT36SDjnkkPTlL385/+2CCy5Is88+e57p32abbdKTTz6ZrrvuunTfffel5ZdfPn/m9NNPTxtttFE68cQTc2bAhRdemMaMGZN+9atfpSFDhqTFF188Pfzww+nkk0/uFQgQERERERER+TQz0a7Bf+6559LLL7+c0/KD6aefPq200krprrvuyr/zk7T8cO6Bzw8ePDjP+MdnVl999ezcB2QBPPXUU+mNN95oeu/Ro0fnmf/yS0RERERERGRiZqJ18HHugRn7Mvwe7/Fzttlm6/X+5JNPnmaaaaZen2l2jfI9GjnuuONyMCFerNsXERERERERmZiZaB38CcnBBx+c3nrrrZ7XCy+8MKGLJCIiIiIiIvLpdPDnmGOO/POVV17p9Xd+j/f4+eqrr/Z6/8MPP8w765c/0+wa5Xs0MuWUU+Zd+csvERERERERkYmZidbBX2CBBbIDftNNN/X8jbXwrK0fMWJE/p2fb775Zt4dP7j55pvTuHHj8lr9+Aw7648dO7bnM+y4v/DCC6cZZ5zxE30mERERERERkVo6+JxXz472vGJjPf7//PPPp0GDBqV99903HXPMMemKK65Ijz32WNphhx3yzvibbbZZ/vyiiy6aNthgg7Tbbrule++9N/35z39Oe++9d95hn8/B1772tbzB3i677JKP07vkkkvSqaeemvbbb78J+egiIiIiIiIi9Tkm7/77709rrrlmz+/hdO+4447pvPPOSwceeGB6991383F2zNSvuuqq+Vi8oUOH9nyHY/Bw6tdee+28e/6WW26ZTjvttJ732STv+uuvT3vttVdabrnl0iyzzJIOO+wwj8gTERERERGRWjFBHfw11lgjn3ffCmbxjzrqqPxqBTvmX3TRRW3vs9RSS6Xbb7+9X2UVERERERERmZiZaNfgi4iIiIiIiEh1dPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDdDBFxEREREREakBOvgiIiIiIiIiNUAHX0RERERERKQG6OCLiIiIiIiI1AAdfBEREREREZEaoIMvIiIiIiIiUgN08EVERERERERqgA6+iIiIiIiISA3QwRcRERERERGpATr4IiIiIiIiIjVAB19ERERERESkBujgi4iIiIiIiNQAHXwRERERERGRGqCDLyIiIiIiIlIDdPBFREREREREaoAOvoiIiIiIiEgN0MEXERERERERqQE6+CIiIiIiIiI1QAdfREREREREpAbo4IuIiIiIiIjUAB18ERERERERkRqggy8iIiIiIiJSA3TwRURERERERGqADr6IiIiIiIhIDZikHPwzzzwzzT///Gno0KFppZVWSvfee++ELpKIiIiIiIjIgDDJOPiXXHJJ2m+//dLhhx+eHnzwwbT00kun9ddfP7366qsTumgiIiIiIiIi/WaScfBPPvnktNtuu6WddtopLbbYYunss89Ow4YNS7/61a8mdNFERERERERE+s3kaRJgzJgx6YEHHkgHH3xwz98GDx6c1llnnXTXXXd97POjR4/Or+Ctt97KP0eNGtXrc+NGv9fx3o3facVAXavKdQbyWp/WMtX9+SbGMtX9+SbGMtX9+SbGMtX9+SbGMtX9+SbGMtX9+SbGMtX9+SbGMtX9+SbGMtX9+cb1oUzx/6IoUlUGFd18+lPKiy++mOaee+505513phEjRvT8/cADD0y33npruueee3p9/ogjjkhHHnnkBCipiIiIiIiIyP/PCy+8kOaZZ55UhUliBr9bmOlnvX4wbty49Prrr6eZZ545DRo0qOX3iLAMHz48N8B0003X5/sP1HUm1mtZJut8YpWDgbyWZbLOJ1Y5GMhrWSbrfGKVg4G8lmWyzidWORjIa1mmibPOmYt/++2301xzzVX5upOEgz/LLLOkySabLL3yyiu9/s7vc8wxx8c+P+WUU+ZXmRlmmKHy/Wig/nbWgbzOxHoty2SdT6xyMJDXskzW+cQqBwN5LctknU+scjCQ17JM1vnEKgcDeS3LNPHV+fTTT9/V9SaJTfaGDBmSlltuuXTTTTf1mpXn93LKvoiIiIiIiMinlUliBh9Iud9xxx3T8ssvn1ZcccX0k5/8JL377rt5V30RERERERGRTzuTjIP/1a9+Nb322mvpsMMOSy+//HJaZpll0nXXXZdmn332AbsHaf2HH374x9L7J9R1JtZrWSbrfGKVg4G8lmWyzidWORjIa1km63xilYOBvJZlss4nVjkYyGtZpk93nU9yu+iLiIiIiIiI1J1JYg2+iIiIiIiISN3RwRcRERERERGpATr4IiL/Y1JYscQzTgrPKZ8MypKIiMjEhQ7+AKOxIxMjHAv56KOPpjFjxkzookzU/XbQoEGp7s/JM9b9OQdCf6vLq9XXQMrSQNe5bfjpxHarXk8fffSR9SUDyuuvv54++OCDia5WH3vssbxJen+e680335xk+osO/ngydugcb7/9dla+fQVnrD/fH2gHcXwzoTvdQN2/3XUm1DOiFDfddNP0xhtv9On7Ue5rr7023XrrrZ9IXXXD008/nU/J6E+/veWWW9IVV1yRPi2gHz788MOu+jDPeeyxx6arrrpqQPTBoYcemk8j6ev3+S4y1Yx33nknjR07Nn2ShP6Ounrvvff6dJ1ol9/85jc9MtUo6++///4E1+8YOy+88EL673//20uWquj76De//OUv0/PPPz8g5RnowNNAXo/+Nnr06DQhGcjx48UXX8wG80CU57vf/W566KGHBqhk9Q+0HnfccWnUqFFN3+tGp//73/9Op5566kThjCELjMOfRrrtV/3ph/HdJ598Mj377LNpYmSbbbZJ//nPf/r1fE888UQ6/vjje/2tr/5EfH7kyJHpL3/5S9dl+uh/4yx66ve///1Ep1+66fPdMMkckze+CWOHQe7SSy/NBs9UU02VFlpoofTlL385LbLIIpWvxXdvvvnmLMirrbZa/j7GIEI+9dRT96l8GCaUcejQofl3rgeUsQqDBw8esDrCcOfZcDYXWGCBnrrpT6eLtOP+lJP7U/d33313mnbaadNaa62Vj63AsBsyZEjlcnCdf/3rX3nGHCNqzTXXTJ/97Gd77lHV8D7xxBPTPPPMk6affvo000wzpTnmmCP/HxmgfNGWVaC9uUaz+1eZvUb2JptssnTaaaelddZZJ33xi1/scYL60258F+V27733ZhmdZZZZ0lxzzZVmnnnmSt+Ptvn+97+ftthii7Ttttt+7DM4IKusskpadNFFWyr/ySefPJ111llZJr/0pS8N2Iw+5XvggQeyExX9lzak3/GMn/nMZ/p0XRzfc845Jy222GK5LSjvhRdemH77299muf32t7/9se/EM5199tl5oIS+tmFc6+c//3mab775ev2tyrW4L3313HPPzXWw4YYb5nbgu7xHe/zoRz/KumG77bbreqYYmSJ48I9//COXj+BWu2fh2gcffHCac84502677ZbbB7m58sorsw7ff//9c/+rCuWPul5++eWzTDWW/+tf/3puq7322it1A4YhdbTgggtm/UTfJjhFmddYY41K1+CZkZULLrgg/e1vf8uBDHTKSiutlHbfffe04oor9rRRJ775zW+mG2+8Mc0777ypPzz33HP52Wabbba01FJL5X798MMP5zF1ueWWy3+r+mzU9SuvvJLH4n/+859p7bXXzjKGjuG9qvocCNRfffXV6f7778//p56pqxlmmCFf62tf+1pl2Wgnx+3q+09/+lPW9yNGjMgyTTAT/YE+GTZsWC5TyFyVvsFnqRscfPRI3DvKd80112QHFEO/HfEsv/rVr9L222/fMw7H3/uiP9EDyDNysOSSS+a//f3vf88OB/puuumma/t9ys14Muuss+a6oY/Q3tQRPxnHePG8/dHv9LtXX301yxTX5sW9pphiirZjM874UUcd1bTfM/6gq+6444629472YmwhYLvffvv1+TmivXDILr/88qyrllhiiV7lpe4Zm9s9F7bTHnvskfUu1wtZ5v8810033ZS22mqrjuU54YQT8liOfuNajKHYLvQ5XtNMM01uV8pSVeZDhqg39BTf5blpP9qtk0w1EuNUX+xNxm7kkOdEvmm7aIP4ybiKrK+66qqVroleQi/QZzj6m7LxvLQd9Uh9VQXbE/+jvzY/fZDx5Xvf+97H+tn//d//5fGH4HeVeozvI2P9CYo/8sgjadlll+35vVu7gn6JzYJdMuOMM2Zbde65587yw3iAbddNvcWz096MudgKje+ho9H13KtrOCZP+sdHH32Uf95www3FsssuWyy++OLFpptuWqyzzjrFPPPMU0wzzTTFr3/967bXGDduXP75t7/9LX/3c5/7XDFo0KBin332yX+/+uqrix122KG4//77uyrbBx98UJx++unFF7/4xWKLLbYoHnzwwfzadtttiwUWWCD/7ZFHHulVhkb+/e9/F/vtt1/x9ttvF/3ltddey9dacMEFez3fFVdcUey///7F3//+92JCcfPNNxerrrpqsfzyyxeDBw8uXnrppWLs2LHFD3/4w+Kqq66qfJ0nnniiWHvttXPb84wXXXRR/vuJJ55YfO973yv++9//drzGU089VSy11FLFaqutlsu0yiqrFPPPP3+WLdpyvfXWK7baaqvcjkcffXTH69GGO+64Y/GDH/wgtzPP1RcZ32WXXYrjjjuuGCioq2222aZYZpllis985jPF8OHDi5VWWqm4+OKLu7rO3HPPXVx55ZVNy7zwwgvntm1FyP1vfvOb4rvf/W4xatSolp/phnfeeac4/vjjixlnnLGYeuqpsyzwGjp0aDFs2LDiC1/4QtFXnn322SxfDz30UP79uuuuy3pm6623LpZYYonit7/9bcvvnn322cVhhx1WDAQXXnhhvtZ7773Xdd3AyiuvXJxxxhlNP7P00ksXZ511Vq+2rMKbb76Z+wT1MNlkk+WfIWvbb799ce211zb93nzzzVdcfvnl+f+PP/54Mf300xdf+cpXijnnnLP4/ve/X3z44YeVy8BYcMcdd+T+esghh2RdwgvZir5H/z7vvPMqXzPuv9FGGxV777138cYbb+TfN9xww2LmmWcupppqquLUU0+t1Le5L3KIrtttt92KkSNHZtmZffbZixlmmKH4v//7v8pyv+eeexaXXnpp0/c6tVtc/y9/+UuxySab5HtPN910xQUXXFAceuihPX1myimnLM4888yOZYnrPf3001mv0Mf4/te+9rX892uuuSb//Z577ul4rSj7gQcemPswdbXxxhsXa621VjFixIisp+add948ZncDcvDYY48VzzzzTJbVKuyxxx65beGoo47KsoMcbLbZZsV2221X7L777sVBBx2Ux9BH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Vlaj/QgIlPt9/J3xNI5o7jOFDAjPPfdccfDBBxdXXXVV8dZbbxXvv/9+MXbs2GLcuHFtv1d+f9111y2+//3vN/3cJptsUpx00kmVyvLRRx/ln7vuumux99579/z90EMPLb773e/2/D569Ohiyy23LI4//vj8+4cffti0fL/61a+Kz3/+8/n5hg4dWtx+++3F+eefX3zmM5/p+W4VHnrooXyNO+64I9+r2f26rfNhw4YVDz74YL+u88EHHxR77LFHsdBCCxVf+9rXijnmmKP4z3/+k9/77W9/W8w///z5/53aEiaffPLi5ptv7vW3+N4iiyxSPProo/0qK9d65513ihdffLF45JFHigceeKBy2QYC5DraDTnYfffdc909/vjjXV2H8h599NHFmWeeWVxyySXFTTfdVDz88MPFv/71r/x8/WnLv/71r8V///vfXNaqPP/88z3/v/POO4vLLrusuO666/J1+suYMWN69U3KNWrUqH5d87333iu+8Y1vFIMGDSomm2yyYuqppy6mmWaaYosttihee+21Stegvq+99triscceK/rLG2+8UTz55JP9aruB4OWXXy623377YskllyxWWGGFYquttsp/p1z77rtv8ZWvfCX/3qh7ttlmm2K99dYrVlxxxWKVVVYpRowYUay00kr5tfzyy2ddXhXaFj279NJLF0sssUSx//77F2+++eaAPB+683Of+1zW25deemnx5z//ufj9739fLLfccsWyyy6bdWI3XH311cUyyyzTS7dQh+iXTiDH0003XfHSSy/l36effvrin//8Z/7/L37xi9wO7Yg2YGxbeOGFiy996Uu5LPPMM0+WZeQa+WbM4edvfvObjmUKPUj/4Nl++MMfFjvttFOx+uqrF/PNN18xfPjwrNPL928FdXD99dcX9913X9YrfSXKhFw1G9+ps5lmmqn429/+1vT72223XXHRRRfl/59zzjnFEUccUfz617/OOhO9S3+vov///e9/F3//+9/z/2+55ZZin332KXbbbbdc/5QNWUW2GMPOPvvsrp/z6aefzvWFbUDZ+gp2wgYbbFCsuuqqud3pt/TNeeedt7jrrrsq2z/Iy+KLL950HDjuuOPyM0OVvv36668Xa621VjFy5Mg8NkR/RkamnHLK4oUXXqg8zrSy8SgHz95XnnjiieIvf/lL8corr1SW1+gDyBV1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DcshGIe64cEHH8zBLGxOdBc6kHagL5OhHAHrVvcH5BubhzEhlg2QgUHAD7Cv0es8dztdhQ1Ie0c9xE78TEjF8kT6FgGgflPIeOP9998vnnrqqY6fGzduXP75zDPPFPvtt18xYsSIYrHFFiu+9KUvFdddd13P+93w7rvvFgceeGCx4YYbFiNHjizuv//+XvcaPXp0cffdd1e61uuvv56//9hjjxWvvfZaMSEZO3Zs/rnlllsW22yzTfH0008Xb7/9di7jSy+9VPzjH/8oHnnkkcrl/M9//pPraOGFFy6OOuqo4sILLywuv/zyYvPNNy+WXXbZ4vbbb8+f++ijj5p+/4033iief/75nt+vvvrqYu211y4WWmihYppppilWW2213IbQl3aExx9/vDjjjDOK73//+8XRRx9dPPHEE32WiYA6GzNmTKXv8ex33nlnse+++xYrrLBCse666xY///nPi+eee66YEERb/O53v8v9BK644oric5/7XM9nqK+VVlqp47VGjRpV7LLLLsW3vvWt3Fa02yyzzFIMGzasGDRoUDHHHHNULteHH36Yf84zzzzFr3/966bl5n4hw33lkEMOKaaddtpiiSWWyLLLT8p6wAEHFG+++WbT79Afvvvd72Zd8O9//zuX44MPPshlqSpL8Tn63FZbbZVl4bOf/Wy+9wILLJB/8tp2223z56o+Z3/r49lnny2mm266Ytdddy3+/ve/99K///3vf4svfvGLxaabbpr/34y77rorPwtlHzx4cP7/8OHDi5133rl49dVXez17FfjsJZdcUvSXO+64I8s39cm4sMkmmxQzzDBD8bOf/ax48MEHsx444YQT8rM99NBDba/14x//uPj617+eP7v88ssXn/nMZ4qZZ565GDp0aH5mnh19xc+//e1vLfvcbrvtVnzjG99oe6/tt9+++N73vld80lBG6mmNNdbIcjDjjDPm8QB533PPPfPfq1wDrrrqqmLxxRfPfRqdvtRSS/W07ZFHHlnpWvH5Rhh70Q/UEff5pHjllVeKrbfeulhxxRWLRRddtDj22GN7lRO9svHGG3esm69+9avF3nvv3fN3ZAL92ReQbfou/W3BBRcsppxyymLIkCHF5z//+WL99dfP5d1jjz3y9ct9u1MZ0eO33nprn8rU7rr8ZOz817/+VTz88MPF9ddfn22Gww8/vKM9xfd4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G8dfekwMGQ07CpPCKPzoRz+afPnLX568//3vn7z2ta+dHHPMMZM///M/n9ztbnebHHLIIZNb3OIW7f/9/Oc/n3uNb3/725P3ve99k2c84xmTm9/85pP9999/cuMb33jyiEc8YvLud7978oMf/GD0rhx++OGTBzzgAZMf//jHM+/5Bje4weT4449f226feeaZkxe+8IXt5x588MGTa17zmpMLX/jCk+te97qTU045ZUPX/tCHPtSu9V577TX5i7/4i/Z3P/vZzwa99yMf+Ui7V+9973snG8XnP//5dt2vf/3rTx784AdPfvKTn0y+973vTT7xiU+M2sPQypvf/ObJQQcdNLnVrW7VPtu+++47ucAFLtB+7/XGN75x1LNOA5299a1vnfv3k08+efKEJzyh9zof+9jHBn3eT3/60/brk5/85Mmv//qvz/wfZ+Be97rXWf5/ET7wgQ+0Z+Xa17725Ha3u93kHve4R7tml73sZScnnnjiZN1Ydi+Wxde//vXJ6aefPvj/H/3oR7dn77jjjpvc9ra3PQsNDL13n3mf+9ynPbvW2jXgv/7rvyZ/8Ad/MHnVq17Vy/NWidw3Grjf/e7XnsPuvd7xjnecXO1qV5t85Stfmex04FMve9nLJm9729tGvzf78eIXv3jyD//wD7t4Et4M//u//zs59dRTF773T//0T9tzlnX38rd8Bef3j/7ojyarwhA+ENzhDneYXOEKV5g897nPnfzzP//z5Oijj57c/va3n1z0ohed/Ou//uvc9+XeTzjhhJa3Xu9615scdthhrVy51rWuNbn61a/enpvrXOc6k2tc4xqTI444ovderO9JJ53U8tEuvv/9708+/OEPt+tdOCumeZB9ocN85zvfafWWPoSWDzjggMlTn/rUyWmnndbK4R/+8Ift99/85jcnX/ziFydnnHHGqKVflpfhsY985CPb7+95z3u2tHWpS12qvb+b3exmkzvf+c6TP/mTP5k89rGPbfnnRuA5PeMXvvCFmXrfPLi/173udTOflW425vytYu+dW+vz0Y9+9Cx/pyM7i2RY9//nIfdNH3v2s5/dfu88P+lJT9r1d39bpx68atAv0fT0fuN7L3/5y3edhz4+xdbAI60v+fmKV7xicuCBB04uf/nLT+5+97tPPvOZz4zWyf/qr/5q8qhHPWry+Mc/fvK85z2v1VfpGmNo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",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,6))\n",
    "top_products.plot(kind = 'bar')\n",
    "plt.title('Top 10 Selling Products')\n",
    "plt.xlabel('Products Name')\n",
    "plt.ylabel('Quantity Sold')\n",
    "plt.xticks(rotation = 85)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1027a5d7-6371-455c-8f3f-ea93d04d8be5",
   "metadata": {},
   "source": [
    "<h3>Sales by Category</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "22044267-2792-4740-b6b1-da003200804d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA+kAAAKVCAYAAACzqqpxAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAYABJREFUeJzt3QeUVdX5P+5NERALalQURFERG4otKvaCYoklmthFUVGjRAUrMRbsGgsWFHuLLbFFLNh7iQpi76AQFQULKCoozH+9+/uf+c0Ag5Q7M2eG51nrMHPPPXc4s+eue+/n7L3f3aisrKwsAQAAAHWucV2fAAAAAPB/hHQAAAAoCCEdAAAACkJIBwAAgIIQ0gEAAKAghHQAAAAoCCEdAAAACkJIBwAAgIIQ0gEAAKAghHQAqCGbbbZZ3mpTo0aNUq9evWr1/wQASkdIB4D/35tvvpn+9Kc/pWWWWSa1aNEitW3bNm211Vbp0ksv1UbT8eWXX6ZjjjkmrbTSSqlly5ZpvvnmS2uvvXY644wz0nfffTfLbXbrrbem/v37a2sA5mpN6/oEAKAIXnjhhbT55punpZdeOvXs2TMtscQSadSoUemll15KF198cfrrX/9a16dYKK+88krabrvt0g8//JD22WefHM7Dq6++ms4555z0zDPPpEceeWSWQ/pbb72VjjrqqBo6awAoPiEdAFJKZ555ZmrVqlUOnwsttFCVNvnqq6+0USXRS/7HP/4xNWnSJL322mu5J33qtrz66qsbbJtNmDAhjxoAgJpguDsApJQ+/vjjtOqqq04T0MPiiy9e5fb111+ftthii7y/efPmaZVVVklXXHHFTLXjxIkT0ymnnJI6dOiQH9uuXbt03HHH5f2VPfroo2mjjTbK5zP//POnFVdcMf3tb3+b6b/VLbfckh8Tw/ajlzt6tss9+eSTee76PffcM93e7LjvxRdfrPZnX3nllemzzz5LF1544TQBPbRu3Tr9/e9/r7j9n//8J22//fapTZs2+Xdefvnl0+mnn54mT55ccUzM3X/ggQfSp59+mv//2Nq3bz/L7fbTTz+lI444Ii266KJpgQUWSDvuuGM+1/h5p556apVj4wLDtttumxZccMHcxltuuWUeOVHZDTfckB/79NNPp8MOOyz/zZdaaqk5bkMAqI6edABIKc9Dj1AVw607deo0wzaJQB6BPgJg06ZN06BBg3KAmzJlSjr88MOrfVzcH4957rnn0sEHH5xWXnnlPA/+oosuSh988EG6995783Fvv/12+sMf/pBWX331dNppp+VQ+tFHH6Xnn39+pv5WESjvuOOOHFbjsZdffnnaZptt0ssvv5x/twjEEXIjyEePeGWxL0J0ly5dqv359913X5p33nnz/P2ZEUE3QnCfPn3y1yeeeCKdfPLJafz48ekf//hHPubEE09M48aNS//73/9ye4Q4dlbaLey///7pX//6V9p3333T+uuvn9siLhBMLdp44403zgE9wv4888yTLz5E28Rj1ltvvSrHx993scUWy+cdPelz2oYAUK0yAKDskUceKWvSpEneunTpUnbccceVPfzww2WTJk2apnV+/PHHafZ169atbLnllquyb9NNN81buZtvvrmscePGZc8++2yV4wYOHFgWb8nPP/98vn3RRRfl22PGjJnlv0w8LrZXX321Yt+nn35a1qJFi7I//vGPFfv69u1b1rx587LvvvuuYt9XX31V1rRp07JTTjllhv/HwgsvXNa5c+eZPqfptdchhxxS1rJly7Kff/65Yt/2229ftswyy0xz7My225AhQ/Lto446qspx+++/f95f+ffaeeedy5o1a1b28ccfV+z7/PPPyxZYYIGyTTbZpGLf9ddfnx+70UYblf36669Vfu6ctCEAVMdwdwBIKVdxj5706LF9/fXX03nnnZe6deuWK7xHz3Fl0YtcLnp/x44dmzbddNM0fPjwfLs6//73v3MvcAwRj8eUbzF0PsQQ6lA+5D6GiUcv8qyKHtzyQm4hiuHttNNO6eGHH64YYt69e/c8VPzOO++sOC5633/99ddcCG5Gogc8hpLPrMrt9f333+ffOXqxf/zxx/Tee+/95uNntt0GDx5c0etd2dRF/6INoqjdzjvvnJZbbrmK/UsuuWTaa6+9co99/I6VRTHBmINf2Zy0IQBUZ64O6TE/b4cddshz5GLuWOXhcjMj5raVz5urvCkmA1A//f73v0933313+vbbb/PQ8L59++ZQGcO633nnnYrjYth5165d8+t9BOoYBl0+X3xGIf3DDz/Mw6zj+Mpbx44dqxSo23333dOGG26YDjrooDy/e4899shDuGc2sK+wwgrT7Iv/I0LxmDFj8u0IvPH7xtDscvF9DBGPed8zEkPEo11mVvzOMSQ8CvPFY+N3Lg+xM2qvWW23mM/euHHjtOyyy1Z5/NS/T7RBtEXM2Z9aXAyIdo7K/pVN/TPntA0BoDpz9Zz0mFPWuXPndMABB6Rddtlllh8fa8MeeuihVfZF0Zl4wwag/mrWrFl+LY8tgmCPHj1yb24ULosCc/FaHwEtCqfFvOQ4/sEHH8xzpGcUpOO+1VZbLT9ueuJnlfc8x4Xk6CGOYmrRQxw9tNFzHD3AU/fozq7oCT7yyCPzPPDoEY6iaZdddtlvPi5+92HDhqVJkybl3/23KsHHKIMI5zG/PuZqRzG7oUOHpuOPP36mLjzMbLvVpMqjAUrRhgBQnbk6pEdF19iqE2+2Ucjmtttuyx8yotjOueeem4vFlBe0KS9qE2J4ZPS0DBw4sFbOH4Cat8466+SvX3zxRf4aReLi/SGGwMcw8nLlQ65nJAJqvFdEyI+RVzMSPcJxXGwRTs8666z8nhT/T/Ti/1bP89SiwFrLli1zD3S56KGPYm7xPhdV0aN4WvTi/5YYhRZTA+6666605557zvDYp556Kn399dd5hMImm2xSsX/EiBHTHFtdm8xsu0Xxvwj08bMrjyaIonuVRRtEW7z//vvT/IwYfh9tP7PBf3bbEACqM1cPd/8tvXr1yh9Cbr/99vTGG2+kP//5z7k67vQ+/IRrrrkm97jEPDsA6pcIv/9Xd62q6CEP5UOjy3uxKx8bQ7ZjWbbfsttuu+XlwKa3hngEvBjhFb755ptp7l9jjTXy16mXHJueeO+KnupyMXQ75rdvvfXWVXrhY5myuFj9z3/+Mw/Tjve42PdbYhRZzN8++uijc/ifWgw/P+OMM6ptr+iBj4rzU4vpA9Mb/j6z7RY1BMLUP/vSSy+tcjvOKdoi2uSTTz6p2P/ll1/m5dNi6bvo+Z8Zs9uGAFCdubonfUZGjhyZP3DF15izXj68PYYcxv7o0ajs559/zm/OJ5xwQh2dMQBzIoqLxTzlmDsdw7kjSL7wwgt5mHms1x1D3kOEuxjiHb3JhxxySPrhhx9yeIz1s8t726sTy4LF3PIIuXFRIOadRxGz6L2N/VHYLXruY1h4DHePpcOidzhCbwTPWJ87AuRviZFfEVgrL8EW+vXrN93h2uVLqcXa5TNj4YUXzuuDb7fddvniQcwvLy9UFxcHole5fPmxDTbYIB+/33775fOJnvCbb755uhdE4mdEe0fPdEw1iNFq0c4z227x+F133TX1798/996XL8FWfiGhci98XEQoX4s+Cs3FUnqxBFtcBImigbNidtoQAKpVbd33uUw0xT333FNx+/7778/75ptvvipbLKuy2267TfP4W2+9Nd83evToWj5zAErhoYceKjvggAPKVlpppbL5558/L8/VoUOHsr/+9a9lX375ZZVj77vvvrLVV189L2vWvn37snPPPbfsuuuuy+8bI0aMqHYJthBLusXxq666al6+K5YzW3vttcv69etXNm7cuHzM448/XrbTTjuVtWnTJp9HfN1zzz3LPvjgg9/8PeIcDj/88LJ//vOfZSussEL+P9Zcc82yJ598crrHT5w4MZ9Dq1atyn766adZarNYsqx3795lHTt2zG0RS6rF73LmmWdW/C4hlkhbf/31y+add978u5QvbxfnWvm8fvjhh7K99tqrbKGFFsr3VV6ObWbaLUyYMCH//ossskj+O8ZSa++//37+eeecc06V8x86dGheOi+Oi3PffPPNy1544YUqx5QvwfbKK69U2w5z0oYAMLVG8U/1EX7uEVfXo1cglmMJcSV/7733ztVkpy7QE1f2l1hiiSr7Yp5cDI2LnwEA9UUsFxYjxqLH+tprr00NURS5W3PNNfOQ9HhvL7W5oQ0BqD2Gu1cj3sxjKF0MMfytOeZRoCaG3029ji4AFF0sPxpLksWQ7YYg5qhPXYk9hr9HMbjKhetKqaG1IQB1a64O6TGPsHLF1wjbcbV9kUUWyQXg4mp7vOFecMEFObTHG/Djjz+eVl999TxPsNx1112XC+jMqFI8ABTJf//731wUNeZQx3tcLJPWEMR88iFDhqTNN988zzN/6KGH8nbwwQeXfKm2htqGANStuXq4eywLE2/iU4viNjfccEP65ZdfcmGZm266KVeVjWqtUYQmCu/Eeq0hlnqJoj4R5s8888w6+C0AYNbtv//+efh3FH6L97woNtcQRDG4eJ+OJVHjYnwskxeF52L5ugjtpdRQ2xCAujVXh3QAAAAoEuukAwAAQEEI6QAAAFAQc13huJhD/vnnn6cFFlggL7sGAAAANSlmmX///fd5yc5YcWRG5rqQHgG91NVdAQAA4LeMGjUqLbXUUjM8Zq4L6dGDXt44Cy64YF2fDgAAAA3c+PHjc2dxeR6dkbkupJcPcY+ALqQDAABQW2Zm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du3a1fUpAQAAQP0P6UsssUT68ssvq+yL2wsuuOB0e9FD375907hx4yq2UaNG1dLZAgAAQAMe7t6lS5f04IMPVtn36KOP5v3ViaXaYgMAAICiq9Oe9B9++CEvpRZb+RJr8f3IkSMresG7d+9ecfyhhx6ahg8fno477rj03nvvpcsvvzz961//Sr17966z3wEAAAAaREh/9dVX05prrpm30KdPn/z9ySefnG9/8cUXFYE9xPJrDzzwQO49j/XVYym2a665xvJrAAAANAh1Otx9s802S2VlZdXef8MNN0z3Ma+99loNnxkAAADUvnpVOA4AAAAaMiEdAAAACkJIBwAAgIIQ0gEAAKAghHQAAAAoCCEdAAAACkJIBwAAgIIQ0gEAAKAghHQAAABoKCF98uTJadiwYenbb78tzRkBAADAXGqWQ/pRRx2Vrr322oqAvummm6a11lortWvXLj311FM1cY4AAAAwV5jlkH7nnXemzp075+8HDRqURowYkd57773Uu3fvdOKJJ9bEOQIAAMBcYZZD+tixY9MSSyyRv3/wwQfTn//859SxY8d0wAEHpDfffLMmzhEAAADmCrMc0lu3bp3eeeedPNR98ODBaauttsr7f/zxx9SkSZOaOEcAAACYKzSd1Qf06NEj7bbbbmnJJZdMjRo1Sl27ds37//vf/6aVVlqpJs4RAAAA5gqzHNJPPfXU1KlTpzRq1Kg81L158+Z5f/Sin3DCCTVxjgAAADBXmOWQHv70pz/lrz///HPFvv322690ZwUAAABzoVmekx5z0U8//fTUtm3bNP/886fhw4fn/SeddFLF0mwAAABALYT0M888M91www3pvPPOS82aNavYH0Pgr7nmmtk4BQAAAGC2QvpNN92UrrrqqrT33ntXqeYea6fHeukAAABALYX0zz77LHXo0GGa/VOmTEm//PLLbJ4GAAAAMMshfZVVVknPPvvsNPvvvPPOtOaaa2pRAAAAqK3q7ieffHKu5B496tF7fvfdd6f3338/D4O///77Z/c8AAAAYK43yz3pO+20Uxo0aFB67LHH0nzzzZdD+7vvvpv3bbXVVnN9gwIAAECtrpO+8cYbp0cffXS2/1MAAACgBD3pAAAAQB32pC+88MKpUaNGM/UDv/nmmzk9JwAAAJgrzVRI79+/f82fCQAAAMzlZiqkRzV3AAAAoICF48r9/PPPadKkSVX2LbjggnN6TgAAADBXmuXCcRMmTEi9evVKiy++eF6CLearV94AAACAWgrpxx13XHriiSfSFVdckZo3b56uueaa1K9fv9SmTZt00003zeZpAAAAALM83H3QoEE5jG+22WapR48eec30Dh06pGWWWSbdcsstae+999aqAAAAUBs96bHE2nLLLVcx/7x8ybWNNtooPfPMM7NzDgAAAMDshPQI6CNGjMjfr7TSSulf//pXRQ/7QgstpFEBAACgtkJ6DHF//fXX8/cnnHBCGjBgQGrRokXq3bt3OvbYY2f3PAAAAGCuN8tz0iOMl+vatWt6991309ChQ/O89NVXX32ub1AAAACok3XSQ/v27fMGAAAA1NJw9xdffDHdf//9VfZFlfdll102r5l+8MEHp4kTJ87h6QAAAMDca6ZD+mmnnZbefvvtittvvvlmOvDAA/OQ95ibHoXjzj777Jo6TwAAAGjwZjqkDxs2LG255ZYVt2+//fa03nrrpauvvjr16dMnXXLJJRWV3gEAAIAaDOnffvttat26dcXtp59+Om277bYVt3//+9+nUaNGzcYpAAAAALMU0iOgl6+PPmnSpFzRff3116+4//vvv0/zzDOPVgUAAICaDunbbbddnnv+7LPPpr59+6aWLVumjTfeuOL+N954Iy2//PKzex4AAAAw15vpJdhOP/30tMsuu6RNN900zT///OnGG29MzZo1q7j/uuuuS1tvvfVc36AAAABQ4yF90UUXTc8880waN25cDulNmjSpcv+///3vvB8AAACo4eHu5Vq1ajVNQA+LLLJIlZ71WTFgwIDUvn371KJFi1wx/uWXX57h8f37908rrrhimnfeeVO7du1S7969088//zxb/zcAAADU25BeanfccUdewu2UU07Jxeg6d+6cunXrlr766qvpHn/rrbfmufFx/Lvvvpuuvfba/DP+9re/1fq5AwAAQIMK6RdeeGHq2bNn6tGjR1pllVXSwIEDc1G6mOM+PS+88ELacMMN01577ZV732Me/J577vmbve8AAABQdHUa0mMptyFDhqSuXbv+vxNq3DjffvHFF6f7mA022CA/pjyUDx8+PD344IO5+vz0TJw4MY0fP77KBgAAAPW6cFxNGDt2bJo8eXJeg72yuP3ee+9N9zHRgx6P22ijjVJZWVn69ddf06GHHlrtcPezzz479evXr0bOHwAAAGo9pN93330z/QN33HHHVJOeeuqpdNZZZ6XLL788F5n76KOP0pFHHpmXiDvppJOmOT7WdI857+WiJz2KzQEAAEC9DOk777zzTP2wRo0a5Z7xWVnWLSrFf/nll1X2x+0lllhiuo+JIL7vvvumgw46KN9ebbXV0oQJE9LBBx+cTjzxxDxcvrLmzZvnDQAAABrEnPQpU6bM1DYrAT3Ekm1rr712evzxx6v8X3G7S5cu033Mjz/+OE0QL18SLoa/AwAAQH1Vp3PSQwxF32+//dI666yT1l133bwGevSMR7X30L1799S2bds8tzzssMMOuSL8mmuuWTHcPXrXY//01m8HAACABh3SI0Q//fTTaeTIkblCe2VHHHHELP2s3XffPY0ZMyadfPLJafTo0WmNNdZIgwcPrigmF/9H5Z7zv//973lYfXz97LPP0mKLLZYD+plnnjk7vwoAAADU35D+2muv5eXOYth5hPVFFlkkV1uPtc0XX3zxWQ7poVevXnmrrlBclRNu2jSdcsopeQMAAIC5ep303r17557rb7/9Ns0777zppZdeSp9++mmeW37++efXzFkCAADAXGCWQ/qwYcPS0UcfnYegxxzwiRMn5iXNzjvvvGrXKgcAAABqIKTPM888FXPEY3h7zBkPrVq1SqNGjZrVHwcAAADM7pz0qKr+yiuvpBVWWCFtuummueBbzEm/+eabU6dOnWb1xwEAAACz25N+1llnpSWXXDJ/HxXVF1544fSXv/wlV2i/8sorZ/XHAQAAALPbkx7rmZeL4e6xXBoAAABQBz3pW2yxRfruu++m2T9+/Ph8HwAAAFBLIT3WLZ80adI0+3/++ef07LPPzuZpAAAAADM93P2NN96o+P6dd95Jo0ePrrg9efLkPOy9bdu2WhQAAABqOqSvscYaqVGjRnmb3rD2eeedN1166aWzex4AAAAw15vpkD5ixIhUVlaWlltuufTyyy+nxRZbrOK+Zs2a5SJyTZo0mesbFAAAAGo8pC+zzDL565QpU2b7PwMAAABKuARb+Pjjj1P//v3Tu+++m2+vssoq6cgjj0zLL7/87Pw4AAAAYHaquz/88MM5lMeQ99VXXz1v//3vf9Oqq66aHn30UY0KAAAAtdWTfsIJJ6TevXunc845Z5r9xx9/fNpqq61m91wAAABgrjbLPekxxP3AAw+cZv8BBxyQl2YDAAAAaimkR1X3YcOGTbM/9kWFdwAAAKCGh7ufdtpp6Zhjjkk9e/ZMBx98cBo+fHjaYIMN8n3PP/98Ovfcc1OfPn1m8zQAAACAmQ7p/fr1S4ceemg66aST0gILLJAuuOCC1Ldv33xfmzZt0qmnnpqOOOIILQoAAAA1HdLLysry10aNGuXCcbF9//33eV+EdgAAAKAWq7tHQK9MOAcAAIA6CukdO3acJqhP7ZtvvpnTcwIAAIC50iyF9JiX3qpVq5o7GwAAAJiLzVJI32OPPSyzBgAAAHW9TvpvDXMHAAAAaimkl1d3BwAAAOp4uPuUKVNq6BQAAACAWepJBwAAAGqWkA4AAAAFIaQDAABAQQjpAAAAUBBCOgAAABSEkA4AAAAFIaQDAABAQQjpAAAAUBBCOgAAABSEkA4AAAAFIaQDAABAQQjpAAAAUBBCOgAAABSEkA4AAAAFIaQDAABAQQjpAAAAUBBCOgAAABSEkA4AAAAFUYiQPmDAgNS+ffvUokWLtN5666WXX355hsd/99136fDDD09LLrlkat68eerYsWN68MEHa+18AQAAoCY0TXXsjjvuSH369EkDBw7MAb1///6pW7du6f3330+LL774NMdPmjQpbbXVVvm+O++8M7Vt2zZ9+umnaaGFFqqT8wcAAIAGE9IvvPDC1LNnz9SjR498O8L6Aw88kK677rp0wgknTHN87P/mm2/SCy+8kOaZZ568L3rhAQAAoL6r0+Hu0Ss+ZMiQ1LVr1/93Qo0b59svvvjidB9z3333pS5duuTh7q1bt06dOnVKZ511Vpo8efJ0j584cWIaP358lQ0AAACKqE5D+tixY3O4jrBdWdwePXr0dB8zfPjwPMw9Hhfz0E866aR0wQUXpDPOOGO6x5999tmpVatWFVu7du1q5HcBAACABlE4blZMmTIlz0e/6qqr0tprr5123333dOKJJ+Zh8tPTt2/fNG7cuIpt1KhRtX7OAAAAUPg56Ysuumhq0qRJ+vLLL6vsj9tLLLHEdB8TFd1jLno8rtzKK6+ce95j+HyzZs2qHB/V32MDAACAoqvTnvQI1NEb/vjjj1fpKY/bMe98ejbccMP00Ucf5ePKffDBBzm8Tx3QAQAAoD6p8+Husfza1VdfnW688cb07rvvpr/85S9pwoQJFdXeu3fvnoesl4v7o7r7kUcemcN5VIKPwnFRSA4AAADqszpfgi3mlI8ZMyadfPLJecj6GmuskQYPHlxRTG7kyJG54nu5KPz28MMPp969e6fVV189r5Megf3444+vw98CAAAAGkBID7169crb9Dz11FPT7Iuh8C+99FItnBkAAADMRcPdAQAAgP8jpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBCOkAAABQEEI6AAAAFISQDgAAAAUhpAMAAEBBFCKkDxgwILVv3z61aNEirbfeeunll1+eqcfdfvvtqVGjRmnnnXeu8XMEAACABh/S77jjjtSnT590yimnpKFDh6bOnTunbt26pa+++mqGj/vkk0/SMccckzbeeONaO1cAAABo0CH9wgsvTD179kw9evRIq6yySho4cGBq2bJluu6666p9zOTJk9Pee++d+vXrl5ZbbrlaPV8AAABokCF90qRJaciQIalr167/74QaN863X3zxxWofd9ppp6XFF188HXjggb/5f0ycODGNHz++ygYAAABFVKchfezYsblXvHXr1lX2x+3Ro0dP9zHPPfdcuvbaa9PVV189U//H2WefnVq1alWxtWvXriTnDgAAAA1uuPus+P7779O+++6bA/qiiy46U4/p27dvGjduXMU2atSoGj9PAAAAmB1NUx2KoN2kSZP05ZdfVtkft5dYYolpjv/4449zwbgddtihYt+UKVPy16ZNm6b3338/Lb/88lUe07x587wBAABA0dVpT3qzZs3S2muvnR5//PEqoTtud+nSZZrjV1pppfTmm2+mYcOGVWw77rhj2nzzzfP3hrIDAABQn9VpT3qI5df222+/tM4666R111039e/fP02YMCFXew/du3dPbdu2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KltooYXm+NznVhHQhXQ812hIvK7huUZD43UNz7Vi+q0e9EIUjmvWrFlae+210+OPP16lpztud+nSZbqPif2Vjw+PPvpotccDAABAfVHnw91jKPp+++2X1llnnbTuuuum/v37pwkTJuRq76F79+6pbdu2eW55OPLII9Omm26aLrjggrT99tun22+/Pb366qvpqquuquPfBAAAAOp5SN99993TmDFj0sknn5yLv62xxhpp8ODBFcXhRo4cmSu+l9tggw3Srbfemv7+97+nv/3tb2mFFVbIld07depUh79FwxdTBmIt+6mnDoDnGvWV1zU812hovK7hudYwNCqbmRrwAAAAQI2r0znpAAAAwP8jpAMAAEBBCOkAAABQEEI6AAAAFESdV3cHqGzy5MnpzTffTMsss0xaeOGFNQ4AzKTx48enJ554Iq244opp5ZVX1m6U1JQpU9JHH32Uvvrqq/x9ZZtssonWLiHV3YE6ddRRR6XVVlstHXjggTmgb7rppumFF15ILVu2TPfff3/abLPN/IUAYDp22223HI569eqVfvrpp9S5c+f0ySefpFi86fbbb0+77rqrdqMkXnrppbTXXnulTz/9ND+/KmvUqFH+DEfp6EkH6tSdd96Z9tlnn/z9oEGD0ogRI9J7772Xbr755nTiiSem559/3l+IGmPkBjWlT58+090fH2ZbtGiROnTokHbaaae0yCKL+CMw25555pn8XhnuueeeHJ6+++67dOONN6YzzjhDSKdkDj300LTOOuukBx54IC255JL5tYyaoyedasUL/KKLLpq23377fPu4445LV111VVpllVXSbbfdlocjw5yKD6sxdGqppZZKBx98cO5B79+/fw7r0SMQQ/egVIzcoLZsvvnmaejQoflCUAw9Dh988EFq0qRJWmmlldL777+fP+Q+99xz+X0VZse8886bn1ft2rVL3bt3T23atEnnnHNOGjlyZH5e/fDDDxqWkphvvvnS66+/ni8wUvMUjqNaZ511Vn7xDy+++GIaMGBAOu+883Jw7927t5ajJFq3bp3eeeed/EF28ODBaauttsr7f/zxx/xhFko9ciMu/kw9ciNe08p7o6AUope8a9eu6fPPP09DhgzJ2//+97/8Grfnnnumzz77LA9T9n7KnIhwHp/RJkyYkN9Dt95667z/22+/zRfBoVTWW2+93KlC7TDcnWqNGjWq4mrZvffem4dMRU/nhhtuaJ4wJdOjR488p6586FR8qA3//e9/c28TlNLYsWPTEksskb9/8MEH05///OfUsWPHdMABB6SLL75YY1My//jHP9Kjjz6aFlxwwYp9rVq1SqeeemoOUkceeWQ6+eSTK0IVzO7ooL333jvNP//8aemll674fBbD4KPeC5TKX//613T00Uen0aNH5+fWPPPMU+X+1VdfXWOXkJBOteIF/+uvv84v+o888kjF/Lq4MhvFSaAU4gNrvNjH0LwITM2bN8/7oxf9hBNO0MjUyMiNuCgUvU5XXHFF3m/kBqU2bty4XAF56qHsY8aMqZjGs9BCC6VJkyZpfGbbYYcdltZdd93csRKjNBo3/r9Bssstt1yekw6lUl6EMC5ql4vOlaiDoHBc6QnpVCte7A866KC05ppr5vlO2223Xd7/9ttvp/bt22s55tgvv/ySttlmmzRw4MBpitvst99+WpiSM3KD2hzuHh9mL7jggvT73/8+73vllVfSMccck3beeed8++WXX84jOWBORDGv6MWM6TvLL798atq0aUU9ISiVeH5Re4R0qhVz0P/+97/nq7N33XVX+t3vfpf3x7y6mE8HcyqGSr3xxhsaklodudGpU6f8umbkBjXpyiuvzPPN99hjj/Trr7/mfRGe4gLkRRddlG/HlJ5rrrnGH4LZFqOAYhhyFPsN0akSveixr23btkakUTIKRtcu1d2BOhUfYmOIe1SjhZoWhbtiJYHq1oBdf/31/REoqaiuPXz48Px9hKeYSgalErUNYqnSWBUlRqbFhe94nv3nP//JFyVfe+01jU3JxPK4MfoxetWjYGEE93juLbvssnn0EKWjJ51qXX/99fnDRPQ2Vfbvf/87X7k1HJlSiB6m6667Lj322GNp7bXXzkt8VHbhhRdqaEominTFkldTr00dH3JjeGisLwylFO+jCipRU6Kw7x133JEvMFZet3rVVVdNH3/8sYanZKKGSxS7jGKFZ555Zl6Vp7y2RgR1Ib20LMFGtc4+++y83NrUFl988bw8G5TCW2+9ldZaa620wAIL5GF6cdW/fBs2bJhGpqTig2wE9e+//75iX1RB3nbbbdMpp5yitSmZWBLrpJNOShtssEFeKSV6NytvUApRiDA+l03v+Vc5tMOcuvTSS9PVV1+dlyutvERu1ER48803NXCJ6UmnWlFtO4avTC2GtsR9UApPPvmkhqTWxPzfP/3pT2mHHXZIDz/8cHrhhRfSjjvumKsgx7BRKJUovPr000+nfffdt2KJSSi1CEgPPPBAnoMeyp9n8VrXpUsXDU7JxBD3KCY9tZiyGBeFKC0hnWrFldmY2zR1JffXX3+9oogclHq+cKhuzjDMqVie6Pbbb89D27fYYov8Ghejhnr16qVxKamHHnooh6cNN9xQy1JjYmRjjASKpSVj+tjFF1+cv48LkHGRCEolOu5ihOPUBeRiOdOVV15ZQ5eY4e5UKyq4H3HEEbmnM+adxPbEE0/k3qaoVgulMGXKlHTaaaelVq1a5Rf+2GJ+0+mnn57vgzkVQbzy9t577+WCSlHhfZ999kmbbLJJxX1QKgsvvPA0tQ+g1DbaaKMcnCKgr7baaumRRx7JnSxR1CvqvECp9OnTJx1++OG5BkKsjR5LSMbc9L59+6bjjjtOQ5eY6u5Ua9KkSXmYXhSKi2VjQoSm7t2758qOzZo103rMsXhxv/baa1O/fv0qepyisFeEqJ49e+Y3AJjT3vMYAhofKspVvl3+fXwtL4QDc+qf//xnrrAdS2O1bNlSgwL13i233JI/n5UXJWzTpk3+/HbggQfW9ak1OEI6vymKecUQ93nnnTdfpbVOIqUUL/Bx0SfmBVcWH24PO+yw9Nlnn2lw5sinn34608d6faNUYu5mfJCNC0AxbWyeeeapcv/QoUM1NiXz1Vdf5W3qEWhWFqAmxCpPsbzk9IoWUhrmpPObOnbsmDeoCd98801aaaWVptkf++I+mFOCN3Vh55131vDUuCFDhuQlcd99990qo4WC0UHUlBgdZIRQzdKTzjTzTWIucKxVHd/PiPWrKYX11lsvb5dcckmV/VGp9pVXXkkvvfSShqakoncz1nSND7VhlVVWybU2ll9+eS0N1CudO3fOr13HH398at269TSrCLhISal8+eWX6ZhjjkmPP/54HrUx9UUh08VKS086VcTa1L/88kvF99WxlAylct555+VK24899ljFcjFR8CaKej344IMampKKZddiasUaa6xRUQPh+eefT6uuumoaNGhQ2mqrrbQ4UG8MHz483XXXXalDhw51fSo0cPvvv39egvmkk06yrGQt0JMO1LnPP/88DRgwIFfdDrGUR8xHj/nqUOp5wt26dUvnnHNOlf0nnHBCropsnjBzIqq5Rx2XRRddNFd3n9EFbdN5KNW0iijyu+uuu2pQatQCCyyQnn322XyRm5onpAMw12jRokV688030worrFBlfwSrKLD0888/19m5Uf9FJfdYorR58+b5+xmJecQwp8aOHZufS+uuu27q1KnTNAUKpy7KCrMrpoZFdfe42E3NM9ydak2YMCH3NpXPPZm6YmgMsYJS+O677/IybOVzhGPo8QEHHJDXTodSWmyxxfKawlOH9NinSi1zqnLwFsKpDTE9LKbsPPTQQ9Pcp3AcpRS1XGLU2ZVXXplXrKBmCelU66CDDkpPP/10Hka15JJLmodOjXj11Vfz8ONY4i96AsqLEsb66DH8eK211tLylEzPnj3TwQcfnC8ybrDBBnlffMA999xzf7NYJsyquLj90UcfTfdC9yabbKJBmWNRZHWfffbJ84SjcByU0tTTdqIDLwoVRmX3qUdtmMJTWoa7U62FFlooPfDAAxXFlaAmbLzxxrngzdVXX52aNv2/64a//vprvkgUQeqZZ57R8JRMVKON3oALLrgg10IIUfvg2GOPTUcccYSLkZRMrEyx1157pU8//dTSWNToPOEYCWR1CmrCb03bqczoodIS0qnWsssum6trRxEvqCnRgx4rCUy9Vvo777yT1llnnfTjjz9qfGrE999/X/EhF0otiit17Ngx9evXb7qj0UznoRQiGMXF7riwDTQchrtTrVgv/eSTT85X0WJYC9SEBRdcMC/pMXVIjyXYhCdqypgxY9L777+fv4/nXlTjhlL68MMP05133mlpLGpUXAjq27dveu6559Jqq602zRDkGCEEpRAdd02aNMlTFCuLqYmxRvq2226roUtITzrViuqNH3/8cR6mFwUipn7ht1QRpRAfIO655550/vnnV5kjHMOPY0mZGJoMpRLz6WIO50033VQxRzg+dHTv3j1deumlLkhSMltssUU67rjj0jbbbKNVqdFRj9WJ0RuK/FIqsQJKFJTebrvtquwfPHhwOv7449Prr7+usUtITzozXHsTalqE8/ggESEp5qKHuCD0l7/8ZZq1rGFORXG4KIg5aNCginob0QMVF4uOPvrodMUVV2hkZtsbb7xR8X1cDIrn1OjRo6fbwxkfeGFOjRgxQiNSa6ODYhm2qcVotCiQSWnpSQcKIeaex8iNUF45FEothrXHEOTNNtusyv4nn3wy7bbbbnkYPMyuxo0b54uOMQJtesrvszQWUN8sscQS6dZbb82jhCp77LHHcpHMWMWC0tGTzm8aMmRIlfWrYxg8lFqE8uhtgpq+GDS9ZYpijXRFCplTejWpC//73//Sfffdl+u7TJo0qcp9saQplMJOO+2UjjrqqDxFsXw1gehBjxFDO+64o0YuMT3pVCuuiO2xxx7pqaeeysuxhe+++y5tvvnm6fbbb0+LLbaY1mO27LLLLjN97N13362VKZktt9wy/e53v8tz0lu0aJH3/fTTT7lCcqzxGj0CUAqxfGTU2ShfWrJcTOt54YUXrJNOSTz++OM5IC233HLpvffeS506dUqffPJJHrGx1lprpSeeeEJLUxLjxo3LNTZeffXVtNRSS1VcIIrVBeKzWnlWoDSEdKq1++6754Ij8WG2fBm2WBYrPszGuta33Xab1mO29OjRo+L7+CARV2VjOaJYcq189EZcEIowf/3112tlSuatt97KlWknTpyYOnfunPdFsZvmzZvnCrUxWghKIQoSfvHFF3mURmVff/113hfVkGFOrbvuurmqdiz1FyuixOtZPL/23nvvHKiivguUSnxme/TRR/PzLJbQjdoam2yyiQauAUI61YrQFL1Kv//976vsf/nll9PWW2+dQxTMqagIGj2YAwcOzB9qQ3x4Peyww/LybP/4xz80MiUVw9pvueWW3OsU4iJkfKCNDxxQyvnpX3755TSjzj744IN8QXL8+PEamzkWwXzYsGF5+PHCCy+cC2HGxcYIUTE8OXrVoRSi0y468OKidmUxxSJG2EYBYErHnHSqFcsTTV2NNsS+8qWLYE5dd911+UNFeUAP8X1U4Y6hokI6pRS9mDHcvWfPnnn+5jXXXJPXS4/hezFkD0o1nSeKw+2///5VPtDGBcioAF++3CTMqfnmm69iHvqSSy6ZC7CWjwgaO3asBqakoyBjdMbUo4O+//77fJ+QXlqNS/zzaECieuORRx6ZPv/884p9n332Werdu3ee1wmlEPMzy3s0K4t9LgZRKm+++WZq3759/nARy8VEz1MME73ooovSVVddlWtt3HvvvRqckoxCiy2GhUYvZ/nt2KI68sEHH5z++c9/amlKYv31188XukOsXx1FvM4888x0wAEH5PugVMpXpphazEuP1zdKS0861brssstyMZL4YNuuXbu8b9SoUbkoiQ8YlEpcfT3wwAPz1f8ITeG///1vXiO98tx1mBPHHXdcXj0ghrnffPPN6Q9/+EPafvvt09VXX12xpnU853beeWcNzRwpr6MR753HHHNM7umEmhLV23/44Yf8fcxLj+/vuOOOtMIKK6jsTknEqk4RzmOLTrrKxTBjdFCsahE97JSWOen85lWzmJdeee5m165dtRolE73l559/frr44otzkaXyIXsxiiN6BCoPg4c5WR89qhxHkZv4EBv1Dl555ZW09tpr5/vjNS56ndTaoNTGjBmTp1SEFVdc0cooQL0SF3/Kv8bnsvnnn7/ivmbNmuULkrvuumv+ntIR0pmuX375JRdRiiGh0XMOtaG8kFIEKCh1Ea/Ro0dXzKUrr4IcyxaFKPDVpk0bFbcpaYHCXr165WJL5VN34qJjzNu89NJLU8uWLbU2JRPzgqNjpfJrXuUwBXPqxhtvzIXjypcvpWaZk850RXG4pZde2gdWaqX2QXnvZYTz8oAegT3ug1KZei7d9ObWQalE/Zann346DRo0KL/Gxfaf//wn74veKJgT0YkSc9DLxUXGqO5evsWa1TFaCEollmAW0GuPnnSqde2116a77747z99cZJFFtBS10sNZ7quvvkpt27bNozqgFM+zWEu4vNJ2BKe4CFQ+XzjWTR88eLALk5R0isWdd96ZNttssyr7n3zyybTbbrvlYfAwu6KWSyy79re//a1idNCVV16Z3zejRz1WTomv8RkOZld8/o9lI+P1LC7+zOjidiynS+koHMcMC8d99NFH+ersMsssM03xm6FDh2o9ZlssQ1TunXfeyUG9ciGSCEzxYQNK1QNQ2T777DPNMZaPodTD3Vu3bj3N/rggGffBnHjhhRfydIrKoq5G+RSemLIYF4NgTsQKKHEBKPTv319j1iI96VTr1FNPneEVs1NOOUXrMUc9m+XPr8rz6MrFB4yYtxnLyADUN1EF+Xe/+12ek14+RPSnn37KF4yixymKssLsipoG0cO51FJLVYSp6F0vnzI2cuTI1LFjx/Tzzz9rZOa43kF5UK9OTOPZdNNNtXQJCelAnfj0009zOI+r/i+//HKVisdRITR6m1R2B+qrt956K3Xr1i1PpejcuXPeF8UKI7A//PDDadVVV63rU6SeD0OOaTsbbrjhdO9//vnn0w477GAIMnMspuzEa1b5dLHpBfRY1jTCPKVjuDvVivAURUeiJ6CyKH6z1lprpeHDh2s9ZltMoQjlVY8BGpJYGeXDDz9Mt9xyS8UypnvuuWfae++980ghmNO1q++9995qQ3rUFIpjYE59/fXXeerEPffck0dBVvbMM8+k7bffPvXo0UNDl5iedGa5oFcsVdSuXbs0adIkrccci6GgM2KeMABUddddd6U99tgjzxP+y1/+UhGeoqbL5ZdfnlcQuPXWW9Of/vQnTccc+fzzz9PGG2+cLwhV/sz27LPP5oC+7777pgEDBmjlEhPSmcZ9992Xv+688855TcRWrVpV3Bcv/o8//nh69NFH0/vvv6/1mGNRLbSyqOYeRZViyHvMuVMtFKhv758zY8cdd6zRc6HhO/7449M//vGPPF+4vGBcjHL84YcfUp8+ffJ9UAoff/xxDup//vOf08UXX5yee+65vGJKjAwaOHCgRq4BQjrTKL8aG0W9pi7oFeunt2/fPl1wwQV5/gnUhBgiGj0Dxx57bJ7TCVAfTD0UtDrx/hoXvWFOvfTSS+m2227L75thhRVWyNMqotI7lHpVnpifHhcYY+j77rvvnq666iqNXEOEdKq17LLL5jnpsTYi1LZXX301L5NVPpcTAIDaNX78+CoFCf/4xz/m0bZXXnlllVWgylcWoDRm7pIvc6URI0YI6NSZpk2b5nlQAPXJE088kVZZZZUqH2zLjRs3Lld1j7mcAPXBQgstlKcmxhajaKMm1b/+9a+8wkDsK7+f0lLdnWodccQRqUOHDvlrZZdddln66KOPcrESKPUczphi8cUXX+TnWXVVawGKKt4be/bsOd1epajxcsghh6QLL7wwz+8EKLonn3yyrk9hrmS4O9Vq27ZtDlBrr712lf1Dhw7N81H+97//aT1KPoczhk7FmulbbLFFrn2w5JJLamWgXi0vOXjw4LTyyitP9/6YwrP11lunkSNH1vq5AVA/6ElnhusiVq7sXi56B8aOHavlKAnrpAMNSSxTGkVWZzSVZ8yYMbV6TgDUL+akU60Y6h69AVN76KGHKpb6gFKJCz8u/gANYRTaW2+9NcMKyUYIUWoxynHqFQOiAjdQPwnpVCvW2DzuuOPSKaeckp5++um8nXzyyemEE05IvXv31nLMse+++y4dfvjhuUBh69at8xbf9+rVK98HUN9st9126aSTTko///zzNPf99NNP+T3VEqaU2jrrrJN+97vf5ffPGM0Ra6TvtttuGhrqKXPSmaErrrginXnmmRVVtmON9FNPPTV1795dyzFHvvnmm9SlS5f02Wefpb333rti/uY777yTbr311tSuXbv0wgsvqBgK1CsRkNZaa63UpEmTHJhWXHHFirnoAwYMyL2d0esZFyWhlO+pMUoj1q2+9957876rr746v78C9Y+QzkyJ+XPzzjtvmn/++bUYJXHUUUelxx9/PD322GPTfFgdPXp0Lqy05ZZbposuukiLA/XKp59+mv7yl7+khx9+OK9YUV4Us1u3bjmoL7vssnV9itRzL730Uq5vED3olR166KF5eay4GPToo4+mddddt87OkYZ7QSiWX5v6+bj++uvX2Tk1REI6M/Trr7+mp556Kn388cdpr732SgsssEDuVY/icQI7cyJGZVx55ZX5Q+v0RD2E+LDxySefaGigXvr222/zkqUR1FdYYQUjgyiZCEQxrWL77bev2Be3r7nmmnxxKAL6E088kR544AGtTslX5YnRjwcccECeshgrQfXo0SNNmDBBS5eQkM4MewK22WabvEzMxIkT0wcffJALxh155JH59sCBA7Ues6158+b54s9SSy013ftjib8oXji9eZ0AMDeLTpMoUBhL/oVLLrkkL1sao9PiglBMHYspZePGjavrU6WBiek6MbXi2muvTcOHD8+jbWMq7N/+9re6PrUGReE4qhVhPIZRRU9ADHUv98c//jEPU4Y5EQXiZtRLPmLEiGmGUwEAKX8u+/DDD3NTXH/99enyyy9Pzz77bA7oITpTmjVrpqmYY/E8K3+uhai5sf/+++eOvFiuOZ6Lu+66q5YuMSGdasWL/d///vdpXuRjmHIU+4I5EcPcTzzxxDRp0qRp7osPFzFsL94AAICqdtxxx1y9faONNko9e/ZMf/rTn9LSSy+d74vpFeecc4756JTEIYccknvOK4vpiueee266//770xFHHJFXf6K0mpb459GATJkyZZo1N8uHIccwK5gTp512Wh6pEVf9Y07TSiutlD9YvPvuu7lHIIL6zTffrJEBYCqXXXZZDuWxikAUI9x2223zKMc11lgjr4wStRBefPFF7cYcGzJkSO49L3fnnXfmTpaoHbTBBhvkkZFR6JfSMiedau2+++6pVatWeTmPCOVxFW2xxRZLO+20U35jiOFVMCdiSPthhx2WHnnkkSoVkLfaaqv8ASTmpAMAM/bVV1+l888/P7355pupbdu2uXdz9dVX12zMsZh6+OCDD+ZihVGUMEZu/Oc//0lrrrlmvv/tt9/OIzpieiylI6RTregxjyHJEZ5iLkr0esbXuGL2zDPPpMUXX1zrURLxwl4+3ymCubnoAAB1L6ZSRLG46DWPXvQYCXncccdV3N+rV69cxDBWg6J0hHR+cwm222+/Pfei//DDD3m4y957712lkBwAANDwjB07NofymFoRo2ljSebtttsu96RH/aoY9h5TLTbddNO6PtUGRUgHAADgN8Xyfv369csdeDG14thjj80jbyktIZ0q7rvvvlmqLAoAAEDpCOlU0bjxzK3KF8W9plf5HQAAgNlnnXSmWXZtZjYBndoQy7ABADNn/Pjx6d57783LmQL1l5DONKIYxLhx4ypun3POOem7776ruP3111+nVVZZRctRUjF9IpaP+eKLL/LtMWPGpM0331wrA0A1dtttt7xkafjpp5/ySjyxL5Zfu+uuu7Qb1FNCOtOIKo2VezDPOuus9M0331Sp+P7+++9rOUqqffv26YEHHkjLL7986t27d16PMz5wAADTF0vibrzxxvn7e+65Jy+bGx0rl1xySTrjjDM0G9RTTev6BCi+eMGHmhYfKEIs+RfLe8w///zp1Vdf1fAAUI0Y+bjIIotUdLLsuuuuqWXLlmn77bfPVbeh1CZNmpRGjBiRO1WaNhUla4qedKBO9OrVK11zzTVV9n388ce5F/2AAw5Ia6+9drr00kv9dQCgGu3atUsvvvhimjBhQg7pW2+9dd7/7bffphYtWmg3SubHH39MBx54YL4ItOqqq6aRI0fm/X/961/z1FhKS0hnupXbY5t6H5TSf/7zn7TuuutW3I656FtttVXaY489cng/8cQT080336zRAaAaRx11VNp7773TUkstldq0aZM222yzimHwq622mnajZPr27Ztef/319NRTT1W5ANS1a9d0xx13aOkSM0aB6Q5v33///VPz5s3z7Z9//jkdeuihab755su3VdymFKIAYQxpL7/i361bt7Tvvvumfv365X3LLbdc+uyzzzQ2AFTjsMMOyxe8R40alS90ly+lG++h5qRTSrFqQITxqBlUufMuetVjJCSlJaQzjf3226/K7X322WeaY7p3767lmCMrrbRS/gAR88+PO+64tNNOO1UE9PD888+nZZZZRisDQDWefPLJvBJKVHWvLOakQynFqjuLL774NPtjqoURt6UnpDON66+/XqtQ42LVgChwE0vExBy6KBi30UYbpTXWWCMP0zv66KNTnz59/CUAoBrbbLNNHureo0eP3MkSc9ShJsSFoFiFJ+agh/JgHlMUu3TpotFLrFGZ0t1AHSmfOhFTK6IXPQqPRNXQeFmKuek33XSTyqEAUI2xY8fm+i033nhjevvtt9MWW2yRi3vtvPPOqVmzZtqNknnuuefStttum0fY3nDDDemQQw5J77zzTnrhhRfS008/nQv+UjpCOlAYsbbr+++/n9q2bZt7BgCAmTN06NA8GvK2227Lt2M6WQT2zp07a0JKIuaeR4dKFJD74Ycf0lprrZWOP/54RQprgJAOAAANwOeff56uuuqqHKRiDeso/htDkQcOHJgLfAH1gyXYAACgnvrll1/SnXfembbbbrtccPXhhx9Ol112Wfryyy/TRx99lPf9+c9/ruvTpIH46quv0ltvvZXeeOONKhulpScdAADqoSjiFcPbo5ZLLGN60EEHpU6dOlU5ZvTo0XkN9SlTptTZeVL/DRkyJBcnfPfdd/PzrbIoIjd58uQ6O7eGSHV3AACoh6Jw16WXXpp22WWXXIR1ehZddNG8VBvMiQMOOCB17NgxXXvttal169aWXathetIBAACo1gILLJBee+211KFDB61UC8xJB+rU4MGD87Ie5QYMGJDXSo+qtN9++22dnhsA1IeK2zHsvWvXrnk74ogj8j4opS233DJXdad26EkH6tRqq62Wzj333Fzw5s0330y///3vU58+ffLQvJVWWikvJwMATCuKxO2444754vaGG26Y9z3//PM5TA0aNChttdVWmo2SGDt2bJ6Tvu666+a6B/PMM0+V++N5SOkI6UCdmn/++XOV0Pbt26dTTz01fx9VamO91wjuUfAGAJjWmmuumbp165aXXKvshBNOSI888kh+L4VSiIs+UZxw/Pjx09yncFzpGe4O1KlmzZqlH3/8MX//2GOPpa233jp/v8gii0z3jQAA+D9RafvAAw+cbpGvKCoHpRJTKvbZZ5/0xRdf5JUCKm8qu5ee6u5Andpoo43y8PYYpvfyyy+nO+64I+//4IMP0lJLLeWvAwDVWGyxxdKwYcPSCiusUGV/7Ft88cW1GyXz9ddfp969e+fK7tQ8PelAnbrssstS06ZN8xD3K664IrVt2zbvf+ihh9I222zjrwMAUznttNPyKLSePXumgw8+ONd2efbZZ/MWQ98POeSQfB+USizzZym/2mNOOgAA1CNNmjTJw46jJ71///7pggsuSJ9//nm+r02bNunYY4/NVd5jrjCUwplnnpmfa9tvv30u+jt14bh4vlE6QjpQiA8aUw/Li2FVsc88JwCoqnHjxrmwauX3zu+//75iPWsotWWXXbba++Ji0PDhwzV6CZmTDtSpsrKy6e6fOHFiLioHAExr6l5y4ZyaNGLECA1ci4R0oE5ccsklFR8yrrnmmrwUW7noPX/mmWfyOukAwLQ6duz4m8PZv/nmG01HjXWwmE5Rc4R0oE5cdNFFFS/0AwcOzMPey0UPeqybHvsBgGn169cvtWrVStNQa2666ab0j3/8I3344YcVF4qi/kGsn05pCelAnQ6b2nzzzdM999yTFlpoIX8JAJhJe+yxh2XWqDUXXnhhOumkk1KvXr3ysrnhueeeS4ceemgaO3ZsXp6N0lE4Dqgzv/zySx7Sfv/996eVV17ZXwIA5qDoKtRk4bgYvdG9e/cq+2+88cZ06qmnmrNeYtZJB+pMLN/x888/+wsAQAmKrkJNiYtCG2ywwTT7Y1/cR2kJ6UCdOvzww9O5556bfv31V38JAJgJU6ZM0YtOrerQoUP617/+Nc3+O+64I62wwgr+GiVmTjpQp1555ZX0+OOPp0ceeSStttpqab755qty/913311n5wYAwP8VKtx9993z6jvlc9Kff/75/BlueuGdOSOkA3UqCsbtuuuu/goAAAUVn9X++9//5tV57r333rwv6gm9/PLLac0116zr02twFI4DAACAgtCTDhTCmDFj0vvvv5+/X3HFFdNiiy1W16cEADBXGz9+/Ewdt+CCC9b4ucxN9KQDdWrChAnpr3/9a7rppptyIZzypWViiY9LL700tWzZ0l8IAKAONG7cODVq1GiGKw3E/ZMnT67V82ro9KQDdapPnz7p6aefToMGDaooRPLcc8+lI444Ih199NHpiiuu8BcCAKgDTz75ZJVAvt1226VrrrkmtW3b1t+jBulJB+rUoosumu6888602WabTfOmsNtuu+Vh8AAA1L0FFlggvf7662m55Zar61Np0KyTDtSpH3/8MbVu3Xqa/Ysvvni+DwAA5iZCOlCnunTpkk455ZT0888/V+z76aef8nqccR8AAMxNzEkH6tTFF1+cunXrlpZaaqnUuXPnvC+GUbVo0SI9/PDD/joAAAUyo0JylIY56UCdi2Htt9xyS3rvvffy7ZVXXjntvffead55563rUwMAmGvtsssuVW5Hod8tttgizTfffFX233333bV8Zg2bkA4AAMA0evToMVOtcv3112u9EhLSgTr3/vvv5zXR33333Yqe9F69eqWVVlqprk8NAABqlcJxQJ266667UqdOndKQIUPynPTYhg4dmlZbbbV8HwAAzE30pAN1avnll8/zz0877bQq+6Pi+z//+c/08ccf19m5AQBAbRPSgTrVsmXL9MYbb6QOHTpU2f/hhx/mXnVrpQMAMDcx3B2oU5tttll69tlnp9n/3HPPpY033rhOzgkAAOqKddKBOrXjjjum448/Ps9JX3/99fO+l156Kf373/9O/fr1S/fdd1+VYwEAoCEz3B2oU40bz9yAnkaNGqXJkyfX+PkAAEBdEtIBAACgIMxJBwAAgIIQ0oE68eKLL6b777+/yr6bbropLbvssmnxxRdPBx98cJo4caK/DgAAcxUhHagTsS7622+/XXH7zTffTAceeGDq2rVrOuGEE9KgQYPS2Wef7a8DAMBcxZx0oE4sueSSOYivs846+faJJ56Ynn766bz0Wojq7qecckp65513/IUAAJhr6EkH6sS3336bWrduXXE7Avq2225bcfv3v/99GjVqlL8OAABzFSEdqBMR0EeMGJG/nzRpUho6dGjFOunh+++/T/PMM4+/DgAAcxUhHagT2223XZ57/uyzz6a+ffumli1bpo033rji/jfeeCMtv/zy/joAAMxVmtb1CQBzp9NPPz3tsssuadNNN03zzz9/uvHGG1OzZs0q7r/uuuvS1ltvXafnCAAAtU3hOKBOjRs3Lof0Jk2aVNn/zTff5P2VgzsAADR0QjoAAAAUhDnpAAAAUBBCOgAAABSEkA4AAAAFIaQDAABAQQjpAFBPjR49Ov31r39Nyy23XGrevHlq165d2mGHHdLjjz8+U4+/4YYb0kILLVTj5wkAzDzrpANAPfTJJ5+kDTfcMIfsf/zjH2m11VZLv/zyS3r44YfT4Ycfnt57771U38T5zzPPPHV9GgBQp/SkA0A9dNhhh6VGjRqll19+Oe26666pY8eOadVVV019+vRJL730Uj7mwgsvzOF9vvnmy73s8Zgffvgh3/fUU0+lHj16pHHjxuWfE9upp56a75s4cWI65phjUtu2bfNj11tvvXx8ZVdffXX+mS1btkx//OMf8/81da/8FVdckZZffvnUrFmztOKKK6abb765yv3xf8YxO+64Y/5/zjjjjNShQ4d0/vnnVzlu2LBh+diPPvqoRtoSAIpESAeAeuabb75JgwcPzj3mEW6nVh6WGzdunC655JL09ttvpxtvvDE98cQT6bjjjsv3bbDBBql///5pwQUXTF988UXeIpiHXr16pRdffDHdfvvt6Y033kh//vOf0zbbbJM+/PDDfP/zzz+fDj300HTkkUfmAL3VVlulM888s8o53HPPPfn+o48+Or311lvpkEMOyRcFnnzyySrHxYWBCPlvvvlmOvDAA9MBBxyQrr/++irHxO1NNtkkB3gAaOgalZWVldX1SQAAMy96z6N3++67784Bd2bdeeedOVyPHTu2Yk76UUcdlb777ruKY0aOHJnnuMfXNm3aVOzv2rVrWnfdddNZZ52V9thjj9wjf//991fcv88+++Tb5T8rhuJHz/5VV11Vccxuu+2WJkyYkB544IF8O3rH4/+/6KKLKo75/PPP09JLL51eeOGF/P/FEPg4j+hd32+//TxNAGjw9KQDQD0zs9fXH3vssbTlllvmYesLLLBA2nfffdPXX3+dfvzxx2ofEz3akydPzsPn559//ort6aefTh9//HE+5v33388BurKpb7/77rs5qFcWt2N/Zeuss06V2xHIt99++3Tdddfl24MGDcrD76M3HwDmBgrHAUA9s8IKK+Re6BkVh4vCcn/4wx/SX/7ylzwUfZFFFknPPfdcHlI+adKkPJd8eqKHvEmTJmnIkCH5a2UR1kttesP1DzrooHxBIXrYY6j77rvvXu35AkBDoycdAOqZCNzdunVLAwYMyMPHpxZDziNkT5kyJV1wwQVp/fXXzz3jMZS8sijoFr3mla255pp531dffZXngFfellhiiXxMFIF75ZVXqjxu6tsrr7xynrteWdxeZZVVfvP322677XJ4j6JyMfc+5qkDwNxCSAeAeigCeoTpGGZ+11135aJuMZQ8CsV16dIlh+qYz33ppZem4cOH58rqAwcOrPIz2rdvn3vOY131mKcew+AjzO+9996pe/fuec77iBEj8hz4s88+u2IueazN/uCDD+aK7vH/Xnnllemhhx7Kvfvljj322DznPYJ2HBPHxs8rL043I9GDv//++6e+ffvmUQPx+wDA3EJIB4B6KIq7DR06NG2++ea5gnqnTp1ylfUI3BGMO3funIPxueeem++75ZZbctCuLCq8RyG5GE6+2GKLpfPOOy/vjyHmEdLj50av+c4775x7yqOgW/nc8gj88fPj/4ne7t69e6cWLVpU/Ox4zMUXX5wLvkUBuQjy8XM322yzmfr9yoflR0V4AJibqO4OAMyxnj175jnyzz77bElaM35OFL0bNWpUat26dUl+JgDUBwrHAQCzLHrIo+c+5o7HUPdYh/3yyy+f45aMSu5jxozJ66dHRXcBHYC5jeHuAMAsi3nqEdJXW221PPQ95sJHVfY5ddttt6VlllkmF78rH34PAHMTw90BAACgIPSkAwAAQEEI6QAAAFAQQjoAAAAUhJAOAAAABSGkAwAAQEEI6QAAAFAQQjoAAAAUhJAOAAAABSGkAwAAQCqG/w88gWVK1AShqAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,6))\n",
    "category_sales.plot(kind = 'bar')\n",
    "plt.title('Sales by Category')\n",
    "plt.xlabel('Category')\n",
    "plt.ylabel('Total Sales')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff062e48-65fc-482a-9fc3-fdf1a0ea50bf",
   "metadata": {},
   "source": [
    "<h3>Sales by Payment Method</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "d8819056-46b9-4fc7-b517-c5bdc4416fe3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAh0AAAG+CAYAAAA3ALY6AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAb85JREFUeJzt3Qd4VNXWBuBv0nshPRAISYDQQgcREQUUBCmCYhfsXbHXXyk28CpIsyOKWAA7KqEJCNJr6CWUQALpvSfzP2t7JzcNSJnMmfK9zzOGmTk5Z82eMWfN3mvvo9Pr9XoQERERNTG7pj4AEREREZMOIiIiMhn2dBAREZFJMOkgIiIik2DSQURERCbBpIOIiIhMgkkHERERmQSTDiIiIjIJJh1ERERkEkw6SFNXXXWVupmSTqfDY489ZtJjkvk7efKk+mz85z//afJjTZo0SR2LyNYw6aB6iYuLw4033ohWrVrBxcUFzZs3xzXXXIPZs2ezJStZu3atOqkYbo6OjoiIiMBdd92F+Ph4m2qrt956Cz///HO9Tvxye+ONN2rd5vbbb1fPe3h4NCieP/74Q530icj0mHRQnf3zzz/o2bMn9uzZg/vvvx9z5szBfffdBzs7O3zwwQdsyVo88cQTWLhwIT755BMMHz4c33//PXr16oXExESbaa/6JB0GktB+++23NR7Py8vDL7/8op5vKEk6Jk+e3ODfJ6KGc2jE75KNefPNN+Ht7Y1t27bBx8enynPJycmaxWXO+vfvr3qGxN133422bduqROTLL7/ESy+9pHV4ZmvYsGH48ccfVYLbpUuXiscl4SguLsbQoUOxZs0aTWMkovpjTwfV2fHjx9GxY8caCYcIDAyscv+LL77AwIED1ePOzs7o0KEDPvzwwzodp6ioCK+//jqioqLU74aFheH5559Xj1e2cuVKXHHFFSoe6Wpv164dXn755Tq/nkWLFqnfkW/NPXr0wPr16yue++uvv1QX/k8//VTj97755hv13KZNm1Bf0ibixIkTdW6n8ePHw9/fHyUlJTX2d+2116rXUL1eZcmSJWpfrq6u6Nu3rxoWEx9//LFqV3nNUksjwxnVbdmyRZ3UJcF0c3PDgAEDsHHjxlprEo4dO4YJEyao90C2l8QqPz+/SjzSOyFJlmHYRLa/FIm5devWqq2rv2cSW7NmzWr9vT///FMleu7u7vD09FS9S/v37694Xo49d+7citgMt+qkZyoyMlK9J9IzJYl2dZL0GI4lr3/UqFE4ePBgje02bNig9iFtLvuU94DIZsml7Ynq4tprr9V7enrq4+LiLrltr1699BMmTNDPmDFDP3v2bPW78nGbM2dOle0GDBigbgZlZWVqWzc3N/3EiRP1H3/8sf6xxx7TOzg46EeNGlWx3b59+/ROTk76nj176j/44AP9Rx99pH/22Wf1V1555SVjkzg6deqk9/f310+ZMkU/bdo0fatWrfSurq4Vr628vFwfFhamHzt2bI3fHzZsmD4yMvKix/jrr7/UcZYsWVLl8V9++UU9/uKLL9a5nVauXKke++2336rsKykpSW9vb69eQ+XXFhMTo2J/55131M3b21vfsmVLtc8OHTro33vvPf2rr76q2u/qq6+uss/Vq1erx/v27au2k7hkf/LYli1bKrZ7/fXX1bG6deumHzNmjH7evHn6++67Tz32/PPPV2y3cOFCvbOzs75///7q33L7559/LthuJ06cUPt499139S+//LKKW94LkZKSoj4H3377rX78+PF6d3f3Kr/71Vdf6XU6nX7o0KGqLeV9DQ8P1/v4+Kj9Cjn2Nddco45hiEdulY8trykqKkr9/vTp09XnpEWLFvri4uIq74nE0rZtW7XN5MmT1Xa+vr4VxxJ79+5Vnyt5HW+//bZ+6tSp+qCgINWm/PNLtohJB9XZihUr1ElObnJSkpNLbGxslT/GBvn5+TUeGzJkiD4iIuKiSYecAOzs7PR///13le0kqZA/0hs3blT35WQo9+VEVF/ye3Lbvn17xWOnTp3Su7i46G+44YaKx1566SV1wszMzKx4LDk5WZ1s5KRbl6Rj/vz5KsbExET977//rk6CcmLctm1bndtJEjE56d18881Vtnv//ffVvuLj46u8Nom58olPEjd5PDg4WJ+dnV3l9cnjhm3l5N6mTRt1fMOJ3hBj69at1cm6etJxzz33VIlJ2s/Pz6/KY5IcSJJQF5WTDkks5d+Gz8LcuXP1Hh4e+ry8vBpJR05Ojkou7r///ir7O3funEq6Kj/+6KOP1nrCNxxb4k9PT6+RKFZO+rp27aoPDAzUp6WlVTy2Z88e9dm96667Kh4bPXq0+lzJ58vgwIED6v8hJh1kizi8QnUms1RkSGHkyJFqrH369OkYMmSImsHy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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10,5))\n",
    "payment_sales.plot(kind = 'pie')\n",
    "plt.title('Sales by Payment Method')\n",
    "plt.xlabel('Payment Method')\n",
    "plt.ylabel('Total Sales')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78304b5f-dc32-482e-a919-d086095d66b4",
   "metadata": {},
   "source": [
    "<h3>Monthly Sales Trend</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "d459259f-f079-4ad9-89c2-1c667d2172b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Mr2toalXr172ZbNmzZIBAwaYv52mTZuaA/atW7faHz/rrLPk5ptvLvfc+/btk5CQEJk/f34D/Ta+PYdGQkKCtGjRwrxm999/v3z99dcmRNne31lZWea9GhcXJ9HR0eY1Wb16dbnn+fbbb+XUU08178lmzZrJhRdeaH+soKBA7rzzTvN/NGrUSPr06SOLFi2q9NkxY8YM6dy5s0RERJj3dF5envzvf/8zXfKaNGkit9xyizmQcpSTkyNXXHGFeV59/ldffbXc4862/ZFHHjGfP2+//ba0bdvWbD/qryul7mvd5zb6Ga37Xv9e9HXXz/Vvvvmm3M+sXbtWzj33XImMjDSf99dcc41kZGTwMnnZMYK+5/X1/u6776RHjx7mvXb66aeb17fiZ4H+DSQnJ5vPpx07dtCSWU+GDBliPv+feuqpatf54osvpFu3bua10Pf0888/b39Mvy/087yinj17yqOPPmq/r+/xrl27mte8S5cu5hjORo/R9O/i008/lYEDB0p4eLj5Ltm0aZOsXLlSevfubd77+hmg3/0VTZw40f75rr1cHE9+aejW300/2/V5dbs+//zzSn+T+n13yimnmN9xyZIlx7An/Q/BqZb0D1v/6PXg5uqrrzZdeuoyBdYHH3wgTzzxhDnD8euvv5qD6MmTJ9fpxfrll1/MAZS+KTdu3GgOvM844wzzmAamvn37yg033GDOoutFD97hHmPHjpWpU6fa7+vfy3XXXVdundzcXLn99tvN66pBKDAw0BxE2bqK6UGvtlLpwbfNtGnTzEGyHgTD9XS/6heMLfSOGjVK9u7da75c9H2rAevss8+WAwcOmMf1QEhfsxEjRsjvv/9uXsfTTjvN/nwafLX7jrZA/vHHH+b5tKVr8+bN9nU0JL300ktmHX1P6xeaPufMmTPN5f3335c33nij3Jeeeu6558y26v+rJ2G0tWzu3Ln2x51tu9qyZYs5ONDfd9WqVfxJNTA98Ln00kvN34b+DV111VX210eDr/496skW/YzQv409e/aY9eGdxwh33XWXOfjWg2I94D3vvPOkqKio3GeBHiPowfaff/5pTrSifmiXyieffFJefvll+euvvyo9rp+Z+l67/PLLZc2aNeakx4MPPmgPxPpeXbFiRbmTnfqa6Xv5yiuvtB/3PfTQQ+bYb/369eb/0+fQk2KOHn74YXnggQfk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Wb16tVlPL7rMJiMjQy688ELzcx07dpRvvvmmwfYBAMA9CE4AAK8yduxYmTp1qv3+O++8I9ddd125de6++2754osv5H//+5/89ttv0qFDBxk+fLgcOHCg3Hr//ve/5fnnn5dffvlFgoKCzHOryy67TO644w7p1q2bpKenm4sus9FQdemll8off/whI0aMkKuuuqrScwMAfAvBCQDgVa6++mpZsmSJpKammstPP/1kltnk5ubK5MmT5bnnnpNzzz1XkpOT5a233pLw8HCZMmVKued64oknZNCgQWade++9V5YuXWq6/um6kZGRJkwlJCSYiy6z0bFUV1xxhQlkTz75pBw6dEhWrFjRoPsBANCwghr4/wMA4LjExcXJyJEjTdc5q9Vqbjdr1sz++NatW6WoqEj69+9vXxYcHCynnXaarF+/vtxz9ejRw347MTHRXO/du9fpeCnHn2vUqJFER0ebnwMA+C6CEwDA62iXuptvvtncfvXVV4/5eTRQ2eg4JlVaWlqnn7P9bG1+DgDgveiqBwDwOuecc44UFhaaliUdu+Soffv2EhISYrrw2eh6WhxCu+TVlj5HSUmJS7cbAOC9aHECAHgdi8Vi73antx1p17mbbrpJ7rrrLomNjTXd7p599lnJy8uTcePG1fr/aNOmjaSkpMiqVaukZcuWEhUVJaGhoS7/XQAA3oHgBADwSjquqDpPP/206Tp3zTXXSE5Ojik5Pnv2bGnSpEmtn//iiy82pc7PPPNMycrKMpX8XDnBLgDAuwRYdWQtAAAAAKBajHECAAAAACcITgAAAADgBMEJAAAAAJwgOAEAAACAEwQnAAAAAHCC4AQAAAAAThCcAAAAAMAJghMAAAAAOEFwAgAAAAAnCE4AAAAA4ATBCQAAAACkZv8Pof8QI4O0iFAAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "monthly_sales = df.groupby('Month')['TotalAmount'].sum().sort_values(ascending = False)\n",
    "plt.figure(figsize = (10,5))\n",
    "monthly_sales.plot(kind = 'line' , marker = 'o')\n",
    "plt.title('Monthly Sales Trend')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Total Sales')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "305984fd-3e26-4955-9b28-44db3bb6408a",
   "metadata": {},
   "source": [
    "<h3>Top 10 States by Sales</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "7f7adead-8e5e-4371-b38c-5a4c27136ed5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA04AAAHfCAYAAABnBYhOAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAOoFJREFUeJzt3QecFPX9P/4PIFWlqYAoVmyIAnZJFDXYNZZYY2Kv0a+9YSK2JMQKJhLRWLDGFsUaexC7omIvkaggAmpUUBQwsL/Hex7/u/8d3DGH3nG3u8/n4zEcOzt7OzO7tzuv+Xw+72lWKBQKCQAAgFo1r/0uAAAABCcAAIA60OIEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAGlCzZs3SMcccU3T7+MADD0wrrbRSY68GQJMhOAE0kYPrukyjR49u8HW5/PLL05577plWWGGF7DnjALo2X331VTr88MPTMssskxZffPG05ZZbppdffrlOzzN37tx0/fXXp4033jh17tw5Lbnkkmn11VdP+++/f3ruuecql3vrrbfS2WefnT788MMfvE0333xzGjZsWCplsX8OOuigtOqqq6Y2bdqkbt26pc033zydddZZjb1qACVhscZeAQBSuuGGG6rthggUjzzyyHzz11prrQbfXeeff376+uuv00YbbZQmT568wOCz4447pldffTWdcsopaemll05//etf0xZbbJFeeumltNpqqy3weY499tg0fPjwtMsuu6T99tsvLbbYYundd99N//znP9Mqq6ySNtlkk8rgdM4552S/94e2gERweuONN9Lxxx+fStH777+fNtxww9S2bdt08MEHZ/spXrsIsfF6xv4D4McRnACagF/96lfVbkeLSwSneecvCk888URla9MSSyxR63J33HFHeuaZZ9Ltt9+e9thjj2zeXnvtlbUaRStHhJXaTJ06NQtZhx12WLryyiur3RctQ5999lk9blHpGzp0aPrmm2/SuHHj0oorrljtvk8//bTR1guglOiqB1AkZsyYkU466aTUo0eP1Lp167TGGmukiy66KBUKhRrH1Nx0003ZMtFta/31109jxoyp0/PEgXf8jjwRnLp27Zp23333ynnRZS/C0913351mzZpV62M/+OCDbL1/8pOfzHdfPHeXLl2y/48cOTLrNhiiG+C8XRbjeaLVq3v37tk+iW5q5513XpozZ07l74uWqvvvvz999NFHlY+v2nIV6xlBr2fPntnviP176qmnzrf+EWR/+tOfpo4dO2aBMvbtGWeckepqQa/Hv/71r2y97rrrrvkeFwE07nv22Wdr/d3jx49Pyy+//HyhKVTsywp12WcLamWMYLv22mtn2xGv/xFHHJG+/PLLasuNHTs2bbvttlkrZLSCrbzyyllLGEAx0+IEUAQiZPz85z/PDrAPOeSQ1Ldv3/TQQw9lXeQmTZqUtTjM22p06623Zt3h4uA4Wne222679MILL6TevXvXyzq98sorab311kvNm1c/Bxdd/KIV6b333kvrrLNOjY+tOMCP1qoIRu3atatxuRijE9vw5z//OQspFV0VK35GsIoQc+KJJ2Y/H3/88TR48OA0ffr0dOGFF2bL/Pa3v03Tpk1LH3/8ceV+qmhJiyAQ+/Wpp57KxmrF73399dez5WL9R40alS335ptvpp122imtu+666dxzz832aXSPe/rpp+u0r/Jejwh3EdgiXO22227VHhvzItxsuummtf7+2J+PPvpotv1bbbXVAtelLvusNhGS4vExliq2JQLwZZddlr0XYl+0bNkya+HaZpttshB9+umnZ0Ezxl/deeedddpXAE1WAYAm5+ijj45mpMrbo0aNym7//ve/r7bcHnvsUWjWrFnh/fffr5wXy8U0duzYynkfffRRoU2bNoXddtttodZj8cUXLxxwwAG13nfwwQfPN//+++/Pnv/BBx9c4O/ef//9s+U6deqUrddFF11UePvtt+db7vbbb8+W+9e//jXffd9+++1884444ohCu3btCjNnzqyct+OOOxZWXHHF+Za94YYbCs2bNy88+eST1eaPGDEie86nn346uz106NDs9meffVZYWHV9PQYNGlRo3bp14auvvqqc9+mnnxYWW2yxwllnnbXA53jjjTcKbdu2zZ6nb9++heOOOy57z8yYMeMH77N43avus9hH8ftvuummao+N17nq/Lvuuiu7/eKLL9Zh7wAUD131AIrAAw88kFq0aJGd5a8quu7FsXkUVKgqWieiO1iFGLMURRiilaouXbLq4rvvvstaT+YVXbgq7l+Qa6+9NmutiG5c0UXt5JNPzlp8fvazn2WtaHUR3cAqREGLzz//PG222Wbp22+/Te+8807u46PFK55zzTXXzB5bMVW02kQLX4hWk4pubtFKtbDq8npENcHoHhhdICtEK9X//ve/3LFu0XUuxjfFctG6c+mll6Zdd90160r3t7/9rV72WeyrDh06pK233rravortipareffVfffdl77//vuF3lcATVVZB6foX77zzjtn/byj/3hFl4y6ivK4NZULjpK8APUpxufEZ1WU7K6qosta3F9VTRXtomhDHBzXV+GFOACvaRzTzJkzK+9fkOjid/TRR2cV+OIAPELJ9ttvn3Ud22effeq0DtGFLrq2xQF9+/bts+5hFSEjuufl+fe//539jnhc1Sn2VdXCCnvvvXc2HuvQQw/Nwkis32233VbnEFWX1yPCW1TGi655FeL/UV0wxl/lid8XVRhjX7722mvpj3/8Y1apMLogRje+H7vPYl/F/TFmat79FYUpKvbVgAED0i9+8Yuskl+McYqAGCF5QWPeAIrBYuU+0LpPnz7ZgNWqg5vrKs6OHnnkkdXmxZnS+OIDKHXLLrtsjeXKK+ZF0KurpZZaKhtrFFOM94kxQREGayp2UPUaUnGQHgf/Me6o4vpFUYL7tNNOq1OoiWViHNYll1xS4/0x7qgiBMbJtmhViUITDz74YNYaFC1TDz/8cNYaWB+i1em4447LxmNF0IjqitEqtzBiXWKbYoqWriiqEQFs4MCBP2qfxX0RmqoGu6oiQIU4gRitZrHu9957b9aqFt+zF198cTZvQZUaAZqysg5OcWYzptrEl1YMKv773/+efdnEAN64HkZ8qYf48K/6BRDXMonrjYwYMWKRrD9QPioG/0fXqqqtThVdq+YNGNE6MK8odhBFGCoOcH+sKFDx5JNPZgfUVQtEPP/889nzVLTaLKwNNtggC04RwBZU4S8q6/33v//Nig5EEYkKUbBgXrX9jggO8dkdJ73yKgnGNsZyMUXQihad+I6IMBWhZEHq+npES1YUbYjvnejqGMUWorXrh4p9WTXMLsw+q2lfxXswWt7yWhNDtJTF9Ic//CGrDBjX6rrllluyVjuAYlTWXfXyRDnfKP8aH/TR7SEqP0UVpJq+AMNVV12VHShEX3GA+rTDDjtkY2HmbX2I6m9xwD/vSaD47IpWhAoTJ07MusJFtbP6ah2JazfF9ZiqVkuLbmIxFia6Qdc0/qnClClTshNN85o9e3Z67LHHspBS0T2tovtznMCqqmI7qpZjj8dHxbp5xe+oqRtalE6P8VTzjgMKEVyiZ0L44osvagyOoS5d0Or6ekTXtngtb7zxxqxlJ75zYl6eCLA1jSeKsXEhyqAv7D6raV/FezBKl88rxmFVvD5RmnzeEvkLs68AmqqybnFakAkTJmR9suNnRXeT6JoX3TNifpxpnLdPf3zJRelVgPoWQSS6XEULRwz+j27G0UUsDr6PP/74rDWgqmghj+voVC1/HWLcSZ7oXhWtMCEOxuPE0e9///vsdnSli5LcFcEpWhSiNHWEoDjAj+eJg+u854muaFG2PLq6RQtOt27dsjEy0dISzx3bVBEY4qA7DvijxT/CT2xPPK5///6pU6dO6YADDsi2MwJkjPGZ96A9RAGD6FoXrTnRnTp6C8Q+/fWvf52NVYpu19FyFK0psf7Rkhfzo5tZtNpEt7boqhfXP4pWsFjX2Na4dlJc2ynPwrwe0V2v4oLCNYWUmsS+ibFi0e284vWJoHb99denzp07Z/szLMw+m1d08Yty5EOGDMkKUUToixaxOJkYYTkKUsR6X3fdddn2xTiqeF9GK2kE0+geGCcAAIpWY5f1aypiV0QJ1Qr33XdfNi/K7VadoizsXnvtNd/jb7755uy+KVOmLOI1B8qhHHn4+uuvCyeccEKhe/fuhZYtWxZWW221woUXXliYO3duteXicfH4G2+8MVsmSlz369evxnLeNYky1BUltOedrr322mrLfvHFF4VDDjmksNRSS2XlrAcMGFCnMtTTp08vXHrppYVtt922sPzyy2fbs+SSSxY23XTTwt/+9rf5tinmrbLKKoUWLVpUK00e5cI32WSTrBR37JdTTz218NBDD81Xvvybb74p/PKXvyx07Ngxu69qme3Zs2cXzj///MLaa6+d7asoj77++usXzjnnnMK0adOyZR577LHCLrvskj1Hq1atsp/77rtv4b333svd1oV9PWbNmpWtQ4cOHQrfffdd7u+v2A/xHL17984eF/tzhRVWKBx44IGF8ePHz7dsXfbZvOXIK1x55ZXZ/onHx2u2zjrrZL/jk08+ye5/+eWXs30Tzx/b2qVLl8JOO+1UrRw7QDFqFv80dnhrCiqu2B7lW0OcmYz+2FF9aN5uLXGmMs6OVhVnTONsWk1XfQdY1J9nUa1uYYsK0DREt7fo6RAtYldffXVjrw4A/x9d9WrRr1+/rLtGdMfIG7MUg2qji8c999yzwOUAIE9cGiNKlEeXPQCajrIOTnHdiffff79aAIp+29EfPIo8RItTfHFFCdUIUvFFFoOWo/949HOvcM0112RleRdUoQ8AFiSqEcZ4shjXFN85MaYIgKajrKvqjR07NvtyiinEoOH4/+DBg7PbUQQigtNJJ52UVSSKbnwvvvhidsX3ClGGd+TIkenAAw+st0pVAJSfyy+/PB111FHZtZKiqAMATYsxTgAAADnKusUJAACgLgQnAACAHGVXHCLGJH3yySdpySWXzEr2AgAA5alQKGQX6o7LQDRvvuA2pbILThGaevTo0dirAQAANBETJ05Myy+//AKXKbvgFC1NFTsnLlgLAACUp+nTp2eNKhUZYUHKLjhVdM+L0CQ4AQAAzeowhEdxCAAAgByCEwAAQA7BCQAAIIfgBAAAkENwAgAAyCE4AQAA5BCcAAAAcghOAAAAOQQnAACAHIITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5FstbgOpWOv3+RtklH/5pRy8FAAA0Ei1OAAAAOQQnAACAHIITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAACCH4AQAAJBDcAIAAMghOAEAAOQQnAAAAHIITgAAADkEJwAAgByCEwAAQA7BCQAAIIfgBAAAkENwAgAAyCE4AQAA5BCcAAAAcghOAAAAOQQnAACAHIITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAACCH4AQAAJBDcAIAAMghOAEAAOQQnAAAAJpycBoyZEjacMMN05JLLpm6dOmSdt111/Tuu+/mPu72229Pa665ZmrTpk1aZ5110gMPPLBI1hcAAChPjRqcnnjiiXT00Uen5557Lj3yyCPp+++/T9tss02aMWNGrY955pln0r777psOOeSQ9Morr2RhK6Y33nhjka47AABQPpoVCoVCaiI+++yzrOUpAtXmm29e4zJ77713Fqzuu+++ynmbbLJJ6tu3bxoxYkTuc0yfPj116NAhTZs2LbVv336h13Gl0+9PjeHDP+3YKM8LAAClamGyQZMa4xQrHDp37lzrMs8++2waOHBgtXnbbrttNr8ms2bNynZI1QkAAGBhNJngNHfu3HT88cenn/zkJ6l37961LjdlypTUtWvXavPidsyvbRxVpMiKqUePHvW+7gAAQGlrMsEpxjrFOKVbbrmlXn/voEGDspasimnixIn1+vsBAIDSt1hqAo455phszNKYMWPS8ssvv8Blu3XrlqZOnVptXtyO+TVp3bp1NgEAABRli1PUpYjQdNddd6XHH388rbzyyrmP2XTTTdNjjz1WbV5U5Iv5AAAAJdfiFN3zbr755nT33Xdn13KqGKcUY5Hatm2b/X///fdPyy23XDZWKRx33HFpwIAB6eKLL0477rhj1rVv7Nix6corr2zMTQEAAEpYo7Y4XX755dm4oy222CItu+yyldOtt95aucyECRPS5MmTK2/3798/C1sRlPr06ZPuuOOONGrUqAUWlAAAACjaFqe6XEJq9OjR883bc889swkAAKCsquoBAAA0VYITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAACCH4AQAAJBDcAIAAMghOAEAAOQQnAAAAHIITgAAADkEJwAAgByCEwAAQA7BCQAAIIfgBAAAkENwAgAAyCE4AQAA5FgsbwHK20qn398oz/vhn3ZslOcFAICaaHECAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAACCH4AQAAJBDcAIAAMghOAEAAOQQnAAAAHIITgAAADkEJwAAgByCEwAAQA7BCQAAIIfgBAAAkENwAgAAyCE4AQAA5BCcAAAAcghOAAAAOQQnAACAHIITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAADkEJwAAAByCE4AAAA5BCcAAIAcghMAAEAOwQkAACCH4AQAAJBDcAIAAMghOAEAAOQQnAAAAHIITgAAADkEJwAAgByCEwAAQA7BCQAAIIfgBAAAkENwAgAAyCE4AQAA5BCcAAAAcghOAAAAOQQnAACAHIITAABAUw5OY8aMSTvvvHPq3r17atasWRo1atQClx89enS23LzTlClTFtk6AwAA5adRg9OMGTNSnz590vDhwxfqce+++26aPHly5dSlS5cGW0cAAIDFGnMXbL/99tm0sCIodezYsUHWCQAAoCTGOPXt2zctu+yyaeutt05PP/10Y68OAABQ4hq1xWlhRVgaMWJE2mCDDdKsWbPSVVddlbbYYov0/PPPp/XWW6/Gx8RyMVWYPn36IlxjAACgFBRVcFpjjTWyqUL//v3T+PHj09ChQ9MNN9xQ42OGDBmSzjnnnEW4lgAAQKkpyq56VW200Ubp/fffr/X+QYMGpWnTplVOEydOXKTrBwAAFL+ianGqybhx47IufLVp3bp1NgEAABRlcPrmm2+qtRZ98MEHWRDq3LlzWmGFFbLWokmTJqXrr78+u3/YsGFp5ZVXTmuvvXaaOXNmNsbp8ccfTw8//HAjbgUAAFDqGjU4jR07Nm255ZaVt0888cTs5wEHHJBGjhyZXaNpwoQJlffPnj07nXTSSVmYateuXVp33XXTo48+Wu13AAAAlFRwiop4hUKh1vsjPFV16qmnZhMAAMCiVPTFIQAAABqa4AQAAJBDcAIAAMghOAEAAOQQnAAAAHIITgAAAA0dnObMmZNdtPbLL7/8sb8KAACgNILT8ccfn66++urK0DRgwIC03nrrpR49eqTRo0c3xDoCAAAUV3C64447Up8+fbL/33vvvemDDz5I77zzTjrhhBPSb3/724ZYRwAAgOIKTp9//nnq1q1b9v8HHngg7bnnnmn11VdPBx98cHr99dcbYh0BAACKKzh17do1vfXWW1k3vQcffDBtvfXW2fxvv/02tWjRoiHWEQAAoFEttrAPOOigg9Jee+2Vll122dSsWbM0cODAbP7zzz+f1lxzzYZYRwAAgOIKTmeffXbq3bt3mjhxYtZNr3Xr1tn8aG06/fTTG2IdAQAAiis4hT322CP7OXPmzMp5BxxwQP2tFQAAQDGPcYqxTeedd15abrnl0hJLLJH+85//ZPPPPPPMyjLlAAAAZR2c/vCHP6SRI0emCy64ILVq1apyfnTfu+qqq+p7/QAAAIovOF1//fXpyiuvTPvtt1+1Knpxbae4nhMAAEAq9+A0adKk1LNnz/nmz507N33//ff1tV4AAADFG5x69eqVnnzyyfnm33HHHalfv371tV4AAADFW1Vv8ODBWQW9aHmKVqY777wzvfvuu1kXvvvuu69h1hIAAKCYWpx22WWXdO+996ZHH300Lb744lmQevvtt7N5W2+9dcOsJQAAQLFdx2mzzTZLjzzySP2vDQAAQCm0OAEAAJSbOrU4derUKTVr1qxOv/CLL774sesEAABQfMFp2LBhDb8mAAAAxRycoooeAABAufpBxSEqzJw5M82ePbvavPbt2//YdQIAACju4hAzZsxIxxxzTOrSpUtWjjzGP1WdAAAAUrkHp1NPPTU9/vjj6fLLL0+tW7dOV111VTrnnHNS9+7ds4vgAgAApHLvqhcXuo2AtMUWW6SDDjoou6ZTz54904orrphuuummtN9++zXMmgIAABRLi1OUG19llVUqxzNVlB//6U9/msaMGVP/awgAAFBswSlC0wcffJD9f80110y33XZbZUtUx44d638NAQAAii04Rfe8V199Nfv/6aefnoYPH57atGmTTjjhhHTKKac0xDoCAAAU1xinCEgVBg4cmN5+++308ssvZ+Oc1l133fpePwAAgOK+jlNYaaWVsgkAACCVe1e9Z599Nt13333V5kV1vZVXXjm7ptPhhx+eZs2a1RDrCAAAUBzB6dxzz01vvvlm5e3XX389HXLIIVl3vRjrFMUhhgwZ0lDrCQAA0PSD07hx49LPfvazytu33HJL2njjjdPf/va3dOKJJ6Y///nPlRX2AAAAyjI4ffnll6lr166Vt5944om0/fbbV97ecMMN08SJE+t/DQEAAIolOEVoqrh+0+zZs7NKeptssknl/V9//XVq2bJlw6wlAABAMQSnHXbYIRvL9OSTT6ZBgwaldu3apc0226zy/tdeey2tuuqqDbWeAAAATb8c+XnnnZd23333NGDAgLTEEkuk6667LrVq1ary/muuuSZts802DbWeAAAATT84Lb300mnMmDFp2rRpWXBq0aJFtftvv/32bD4AAEAq9wvgdujQocb5nTt3ro/1AQAAKN4xTgAAAOVKcAIAAMghOAEAAOQQnAAAAOqjOMQ999yT6urnP/95nZcFAAAomeC066671umXNWvWLM2ZM+fHrhMAAEDxBae5c+c2/JoAAAA0UcY4AQAA1PcFcMOMGTPSE088kSZMmJBmz55d7b5jjz32h/xKAACA0glOr7zyStphhx3St99+mwWozp07p88//zy1a9cudenSRXACAABKzkJ31TvhhBPSzjvvnL788svUtm3b9Nxzz6WPPvoorb/++umiiy5qmLUEAAAopuA0bty4dNJJJ6XmzZunFi1apFmzZqUePXqkCy64IJ1xxhkNs5YAAADFFJxatmyZhaYQXfNinFPo0KFDmjhxYv2vIQAAQLGNcerXr1968cUX02qrrZYGDBiQBg8enI1xuuGGG1Lv3r0bZi0BAACKqcXpj3/8Y1p22WWz///hD39InTp1SkcddVT67LPP0hVXXNEQ6wgAAFBcLU4bbLBB5f+jq96DDz5Y3+sEAABQ3C1OW221Vfrqq6/mmz99+vTsPgAAgFTuwWn06NHzXfQ2zJw5Mz355JP1tV4AAADF11Xvtddeq/z/W2+9laZMmVJ5e86cOVmXveWWW67+1xAAAKBYglPfvn1Ts2bNsqmmLnlxMdy//OUv9b1+AAAAxROcPvjgg1QoFNIqq6ySXnjhhbTMMstU3teqVausUERcEBcAAKBsg9OKK66Y/Zw7d25Drg8AAEDxlyMP48ePT8OGDUtvv/12drtXr17puOOOS6uuump9rx8AAEDxVdV76KGHsqAU3fXWXXfdbHr++efT2muvnR555JGGWUsAAIBianE6/fTT0wknnJD+9Kc/zTf/tNNOS1tvvXV9rh8AAEDxtThF97xDDjlkvvkHH3xwVqZ8YYwZMybtvPPOqXv37lm1vlGjRtXpOlLrrbdeat26derZs2caOXLkQj0nAABAgwenqKY3bty4+ebHvKistzBmzJiR+vTpk4YPH17nyn477rhj2nLLLbPnO/7449Ohhx6adR8EAABo9K565557bjr55JPTYYcdlg4//PD0n//8J/Xv3z+77+mnn07nn39+OvHEExfqybfffvtsqqsRI0aklVdeOV188cXZ7bXWWis99dRTaejQoWnbbbddqOcGAACo9+B0zjnnpCOPPDKdeeaZackll8zCy6BBg7L7oqvd2WefnY499tjUkJ599tk0cODAavMiMEXLEwAAQKMHp7j4bYixSFEcIqavv/46mxdBalGYMmVK6tq1a7V5cXv69Onpu+++S23btp3vMbNmzcqmCrEsAABAg41xitBUVQSmRRWafqghQ4akDh06VE49evRo7FUCAABKuRz56quvPl94mtcXX3yRGkq3bt3S1KlTq82L2+3bt6+xtSlEd8KqY6+ixUl4AgAAGiw4xTinaLVpLJtuuml64IEHqs2Li+7G/NpE2fKYAAAAFklw2meffRa65PiCfPPNN+n999+vVm48yox37tw5rbDCCllr0aRJk9L111+f3R/FKS677LJ06qmnZteNevzxx9Ntt92W7r///npbJwAAgB88ximvi94PMXbs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e+65dNVVV2UHYSussEJ6++23s4AYAarUXHrppVk4euyxx2q8f+DAgWm33XZLRx99dColEYKvvvrq9I9//CN17949O8D+xS9+kTbccMNUyj744IN0zTXXpJEjR2YX647X97777kvFbu7cudkJnvibXX311dOaa66ZzY+/3ffffz/tueee6e9//3tq1qxZKgevvvpqWm+99Uqia/F1111XLfDHd8+5556bunTpUm25+J4qBc2bN899n8b9//vf/1I5KKX3coiQH98zcVI2vntK2b///e80ePDgdMUVV6T27dvPFyTib/n3v/99WmWVVVIp/N327t07/fe//0133nln2njjjavdP3Xq1Oz1bnLv47gALvXvf//7X2HvvfcuNG/evLDEEksURo8eXZK7+aKLLir06tWrsNxyyxVOPvnkwrhx47L5iy22WOHNN98slKINN9ywcM8999R6/7333pstUwomT55cGDJkSKFnz56FLl26FI455piSfm0rzJw5s3DjjTcWttxyy0LLli2zv+NLLrmkMG3atEKpiO3p3Llz9n6d1913353dN3To0EK5iM+ueJ1LUXwHjR8/vlCqRo0aVet02mmnFdq2bVto3bp1oVyU2nt50qRJhR122KHQqVOnwg033FAoZYcddljhlFNOqfX+U089tXDkkUcWSkHz5s0LEyZMKBx66KGFNm3aFK655ppq90+ZMqVJvo8FpwYwe/bswqBBg7IDrn333Tf7Y99mm20KEydOLJSaFi1aFM4444wsKFZVygfXHTt2LHz00Ue13h/3xTLFbqeddiq0b98+ew/fd999la9xKb+2Y8eOLRx11FHZ67fBBhsULr300uzDuxS3eZ111ilcffXVtd5/1VVXZcuUi1I72Cyn4FSTd955p7Drrrtm31H7779/4cMPPyyUi1J9L1977bXZ8dTuu+9eeOmllwqvvvpqtakUrL766oUXXnhhgd9RsUwpaNasWWHq1KnZ/4cPH15o1apV4dhjjy3MmTOnSQcnY5zq2bhx47Im8ltuuSU99NBD6eabb06vv/56atGiRdYkGV2dSsl5552XdfVZeeWVs/Fd5VAsILp7RJet2sR9pdAlJMbzHHLIIemcc85JO+64Y/YeLnXRVaB169ZZ19MXX3wxK+bStWvXVKpdQqLbYW3ivlgGisknn3ySDjvssGxMcXwOx3dydF1cccUVG3vV+JEOPPDAdNttt6W7774767rXt2/f1K9fv8qfpWDChAnzdamtaumll04TJ05MpeY3v/lNeuSRR7Jj52222aZajYCmZrHGXoFSPPCKfuOXXHJJWmKJJbJ5yy23XHrggQeyMUBRKCHGiMTtUjBo0KBseuKJJ7JxILH9PXv2zPrVN+U3/o+x9tprp0cffTStv/76Nd7/8MMPZ8sUu6eeeioL+rGda621Vvr1r3+d9tlnn1TKouJlbHNcViC2d9ttty3ZMT4x1vKrr77KxiTWJAqdtGnTJpWKGJO3ILEvKF4x/uOPf/xj+stf/pIdSMcY1FIcY1vO7+U4rjrzzDPTr371q+znYouV3iFshw4d0vjx42sN+jH+dN6xT6Vi8803z05YxhjxCMaXX355aooUh2iAs/Tbb799rfd/9NFH6dBDD82SdalWXItWtghRL730UlZ5LaqQlVJlvagoF9sTZ0Z22mmnavfde++92YD7+IAvlapG33zzTXaWL17TF154IRuoGdt38MEHpyWXXDKVmjibV1EMIioo7r333llxl9deey0LkKUiWhEjNNX25XTkkUdmZz9L5SRPnK2uSwiOAejFbt7P2+HDh2cHm3FQVlX8HZeCCy64ICu81K1btyw87bLLLqmU1bXSWCm8l8N//vOf7IR0tIBH0YRSfn332muv9P3336e77rqrxvtj21u1apX19CmF4hBTpkyZr4UtypBHb5eo7hqtxk2tOITgVM+ictHJJ5+c2rVrl8pddNuLs/c33XRTnS4MXEziICQCYlQiW2ONNbJ577zzTnbtqvjgi2pkpVBNLrpgVvXuu+9mr+kNN9yQndXceuutswqDpSpaFiNExZdYjx49spMAMUV33GL3zDPPpC222CLtuuuu2WdWvJejpTiq6l188cVZd5iojPmTn/yksVeVhbTlllvmLhMh8vHHHy+JfRsHYNGCGt1LF9SlOCp3lUqQWGmllbLtLgfReyda/yM0RVe1UvbKK6+kTTfdNDspG9fBrHp8EScI7r///uyzuxS+g7bccsvsu7Vjx4413n/hhRem008/XXAqdfGhHTXpF9RHtZTEF+8xxxyTjQmpqXRmfABESfYFjaUoVtEKE6Ewms7jgDNKOv/yl7/MglMpiC/l6C4QH25bbbVV9jO6nYY4AxStaxEqSik4xXZddNFF2TbF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iq54s2bNmu/+F198Mft57bXXpsmTJ1fe/uabb9IOO+yQtUy98sorabvttks777xzmjBhQnb/nXfemZZffvl07rnnZo+LKUTgimWjleu1115Lt956axakjjnmmEW63QA0Hi1OABSlf/zjH+mwww5L3333XVpvvfWylqd99tknrbvuupVjnO6666606667LvD39O7dOx155JGVIShaq44//vhsqnDooYemFi1apCuuuKJyXgSneM5ouWrTpk2DbScATYMWJwCKUrT+fPLJJ+mee+7JWoOi214EqJEjR9b6mGhxOvnkk7Mueh07dsxard5+++3KFqfavPrqq9nvrWjpiikKUcydOzd98MEHDbB1ADQ1ikMAULSipWfrrbfOpjPPPDNrGTrrrLPSgQceWOPyEZoeeeSRdNFFF6WePXumtm3bpj322CMrMrEgEbiOOOKIdOyxx853X1T1A6D0CU4AlIxevXpVliBv2bJlmjNnTrX7o1R5hKoo7FARiKJoRFWtWrWa73HRkvXWW29lYQuA8qSrHgBFJ0qOb7XVVunGG2/MijVEd7nbb789XXDBBWmXXXapHKsURSCmTJmSvvzyy2zeaqutlhWAGDduXNb97pe//GXW3a6qeNyYMWPSpEmT0ueff57NO+2009IzzzyTjYOKx/773/9Od999t+IQAGVEcAKg6MQYo4033jgNHTo0bb755lmBh+iqF8UiLrvssmyZiy++OOuW16NHj9SvX79s3iWXXJKVMe/fv39WTS/GKUVrUlVRUS9aoVZdddW0zDLLZPOi4ESUKX/vvffSZpttlv2+wYMHp+7duzfC1gPQGFTVAwAAyKHFCQAAIIfgBAAAkENwAgAAyCE4AQAA5BCcAAAAcghOAAAAOQQnAACAHIITAABADsEJAAAgh+AEAACQQ3ACAADIITgBAACkBft/OWFpT6LRijYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10,5))\n",
    "top_sales_state.plot(kind = 'bar')\n",
    "plt.title('Top 10 States by Sales')\n",
    "plt.xlabel('State')\n",
    "plt.ylabel('Total Sales')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "afa4d001-b7eb-43da-a947-d63ed76e464f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"Amazon_Cleaned.csv\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "152ebded-32db-44dd-a50d-7e43062e4106",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#10B981;\">🎯 Conclusion</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b30880a3-06a0-459a-bfcb-6b427cd3e263",
   "metadata": {},
   "source": [
    "### Project Summary\n",
    "\n",
    "This project analyzed Amazon sales data using Python, Pandas, Matplotlib, and Jupyter Notebook to identify sales trends, customer purchasing behavior, and business performance.\n",
    "\n",
    "### Key Findings\n",
    "\n",
    "- Electronics generated the highest total revenue among all product categories.\n",
    "- Credit Card was the most preferred payment method.\n",
    "- Sales performance varied across different states and cities.\n",
    "- The top-selling products contributed significantly to overall revenue.\n",
    "- Discounts and shipping costs influenced the final order amount.\n",
    "\n",
    "### Business Recommendations\n",
    "\n",
    "- Increase marketing efforts for high-performing categories such as Electronics.\n",
    "- Maintain sufficient inventory for top-selling products to avoid stock shortages.\n",
    "- Promote digital payment methods by offering cashback or discounts.\n",
    "- Focus marketing campaigns on high-revenue states and cities.\n",
    "- Review discount strategies to maximize profit while maintaining sales growth.\n",
    "\n",
    "### Conclusion\n",
    "\n",
    "The analysis provides valuable insights into customer behavior, product performance, and revenue trends. These findings can support better business decisions related to inventory management, marketing strategies, pricing, and sales optimization."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
