## selenium waits
> selenium的延迟等待分为，显式等待（Explicit Waits）和隐式（Implicit Waits）。

### 显式等待(Explicit Waits)
> 显式等待，就是明确的要等到某个元素的出现或者是某个元素的课点击等条件，等不到，就一直等待下去，  
除非设置了超时时间，超过设置的时间后，会抛出异常。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox() driver.get("http://somedomain/url_that_delays_loading") try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
) finally:
    driver.quit()
```

### 隐式等待(Implicit Waits)
> 隐式等待：是针对Driver每次执行命令的最长执行时间，可以理解为超时时间。  
隐式等待是设置了有一个最长等待时间，如果在规定的时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。  
注意：比如一个页面很大，想要的元素很快就出来了，但是浏览器还在转圈圈，加载其它数据，不需要这样等待下去，那么我们可以用显式等待。

**隐式等待对整个浏览器driver的周期都起作用，所以设置一次即可！**

```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://www.codelieche.com")
logo_element = driver.find_element_by_id("logo")
```

### sleep
> 另外一种强制等待的方式就是：

```python
import time
time.sleep(10)
```
