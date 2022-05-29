-- https://leetcode.com/problems/second-highest-salary/
Select MAX(Salary) AS SecondHighestSalary from Employee
where Salary < (Select MAX(Salary) from Employee)