## selenium

### 常用的导入

```python
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
# ActionChains类鼠标操作的常用方法
from selenium.webdriver import ActionChains
```


### 常用的查找元素方法

#### 查找单个元素
- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text - find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

#### 查找多个元素
- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text - find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector
