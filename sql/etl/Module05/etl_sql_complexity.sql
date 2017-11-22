--How to increasingly add complexity to a typical ETL SQL script
-- Get product data
SELECT 
    [ProductID] 
  , [Name] 
  , [ProductNumber]
  , [Color]
  , [StandardCost]
  , [ListPrice] 
  , [Size]
  , [Weight]
  , [SellStartDate] 
  , [SellEndDate]
  , [DiscontinuedDate] 
FROM [AdventureWorksLT2012].[SalesLT].[Product]

-- Add aliases and transformations
SELECT 
    [ProductID] = T1.[ProductID] 
  , [ProductName] = T1.[Name] 
  , [ProductNumber] =  Cast( T1.ProductNumber as nvarchar(50))
  , [ProductColor] = IsNull( Cast( T1.[Color] as nvarchar(50)), 'Not Defined') 
  , [ProductStandardCost] = T1.[StandardCost]
  , [ProductListPrice] = T1.[ListPrice] 
  , [ProductSize] = IsNull( T1.[Size], -5) 
  , [ProductWeight] = IsNull( T1.[Weight], -5)
  , [SellStartDate] = T1.[SellStartDate]
  , [SellEndDate] = T1.[SellEndDate]
  , [DiscontinuedDate] = T1.[DiscontinuedDate]
FROM [AdventureWorksLT2012].[SalesLT].[Product] as T1

-- Add data from product models
SELECT 
    [ProductID] =T1.[ProductID] 
  , [ProductName] = T1.[Name] 
  , [ProductNumber] =  Cast( T1.ProductNumber as nvarchar(50))
  , [Color] = IsNull( Cast( T1.[Color]  as nvarchar(50)), 'Not Defined') 
  , [ProductStandardCost] = T1.[StandardCost]
  , [ProductListPrice] = T1.[ListPrice] 
  , [ProductSize] = IsNull( T1.[Size], -5) 
  , [ProductWeight] = IsNull(T1.[Weight], -5)
  , [SellStartDate] = T1.[SellStartDate]
  , [SellEndDate] = T1.[SellEndDate]
  , [DiscontinuedDate] = T1.[DiscontinuedDate]
  , [ProductModelID] = T2.[ProductModelID]
  , [ProductModelName] = T2.[Name]
FROM [AdventureWorksLT2012].[SalesLT].[Product] as T1
JOIN [AdventureWorksLT2012]. [SalesLT].[ProductModel] as T2
  ON T1.ProductModelID = T2.ProductModelID
