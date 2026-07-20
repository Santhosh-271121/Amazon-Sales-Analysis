-- ====================================
-- Amazon Sales Analysis Project
-- Author: Santhosh
-- ====================================

-- Create Database

CREATE DATABASE amazon_sales;

USE amazon_sales;
s
select * from amazon_orders limit 10;

select count(*) as total_orders from amazon_orders;     # How many orders are there?

select sum(TotalAmount) as Revinue from amazon_orders;  # What is the total revenue?

select avg(TotalAmount) as Average_amount_per_order from amazon_orders;  # What is the average amount spent per order?

select sum(Quantity) as Total_quantity_sold from amazon_orders;  # How many products were sold?

select ProductName , sum(Quantity) as total_qt from amazon_orders group by ProductName order by total_qt desc limit 10;  # Top 10 Best Selling Products

select ProductName , sum(TotalAmount) as Revenue from amazon_orders group by ProductName order by Revenue desc limit 10 ;  #Top 10 Revenue Generating Products

select Category , sum(TotalAmount) as Sales from amazon_orders group by Category order by Sales desc;   #  Sales by Category

select Brand , sum(TotalAmount) as Revenue from amazon_orders group by Brand order by Revenue desc;  # Sales by Brand

select CustomerName , sum(TotalAmount) as Revenue from amazon_orders group by CustomerName order by Revenue desc limit 10;  #  Top 10 Customers

select State , sum(TotalAmount) as Revenue from amazon_orders group by State order by Revenue desc; #  Sales by State

select City , sum(TotalAmount) as Revenue from amazon_orders group by City order by Revenue desc;  #  Sales by City

select PaymentMethod , sum(TotalAmount) as Sales from amazon_orders group by PaymentMethod order by Sales desc;  #  Payment Method Analysis

select OrderStatus , count(*) as Total_sales from amazon_orders group by OrderStatus order by Total_sales desc; #  Order Status Analysis

select Month, sum(TotalAmount) as Revenue from amazon_orders group by Month order by Revenue desc;  # Monthly Revenue

select Year, sum(TotalAmount) as Revenue from amazon_orders group by Year order by Revenue desc;  #  Yearly Revenue

select Category , round(avg(Discount),2) as Avg_Discount from amazon_orders group by Category order by Avg_Discount desc;  #  Average Discount by Category

select State , round(avg(ShippingCost),2) as Average_Shipping_Cost from amazon_orders group by State order by  Average_Shipping_Cost desc; #  Average Shipping Cost by State

select CustomerName , sum(TotalAmount) as Revenue from amazon_orders group by CustomerName order by Revenue desc limit 10; #  Highest Revenue Customer

select State , sum(TotalAmount) as Revenue from amazon_orders group by State order by  Revenue desc;  #  Highest Revenue State

select Category , sum(TotalAmount) as Revenue from amazon_orders group by Category order by  Revenue desc;  #  Highest Revenue Category
