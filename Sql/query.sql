select Region ,Category,
round(max(Sales*Quantity),1) as revenue,round(max(Profit),1) as profit
from sales
group by Region ,Category
order by revenue,profit desc
limit 1;

select 
case
when Discount = 0 then 'No dicount'
when Discount between 0.1 and 0.10 then 'low Discount'
when Discount between 0.11 and 0.20 then 'Medium Discount'
when Discount between 0.21 and 0.30 then 'High Discount'
when Discount > 0.31 then 'Very high Discount'
end as discount_allowed,
count(*) as number_order,
round(avg(profit),1) as avg_profit,
round(sum(profit),1) as total_profit
from sales
group by discount_allowed
order by avg_profit;

select 
DATE_FORMAT(Order_Date, '%Y-%m') as order_month,
sum(Sales) as total_sales,
sum(Profit) as total_profit,
count(distinct order_id) as total_order
from sales 
group by DATE_FORMAT(Order_Date, '%Y-%m')
order by order_month;

select 
Category,
sum(Profit) as total_profit,
sum(Sales) as total_sales,
count(order_id)
from sales 
group by Category 
having sum(Profit) < 0
order by sum(Sales) desc;

select 
Customer_Name,
round(sum(Sales),0) as total_revue,
round(sum(Profit),0) as total_profit,
count(distinct order_id) as total_order
from sales 
group by Customer_Name
order by total_revue desc
limit 10;

















