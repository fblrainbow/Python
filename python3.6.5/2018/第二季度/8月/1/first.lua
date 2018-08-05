--C语言里面的 a?b:c 相当于 这里的  a and b or c
a = true
b = 1
c = 2
-- print(a and b or c)

---遍历表格
t = {
	MarketCode="1", 
	ETFList={
		{
          Code="510050",
          Name="上证50ETF"
      }, 
		{
          Code="510180",  
          Name="上证180ETF"
      } 
	} 
}
m = {x="1",y={z = "2"}}
a = 12.1231
print(type(a .. ""))
print(a)
b = "123.34"
--local msglog = sys_format("%s",a)
t = 12
-- print(--t)
print(t or {})
local x = 1
local log = "信息" .. x
local y = []

