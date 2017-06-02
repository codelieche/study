## 执行

### 先开启master再开启worker
`python task_master.py`

```
2017-06-02 19-18-34: Start!
Put task 965...
Put task 628...
Put task 635...
Put task 736...
Put task 995...
Put task 756...
Put task 770...
Put task 644...
Put task 274...
Put task 261...
开始读取结果
Result: 965 * 965 = 931225
Result: 628 * 628 = 394384
Result: 635 * 635 = 403225
Result: 736 * 736 = 541696
Result: 995 * 995 = 990025
Result: 756 * 756 = 571536
Result: 770 * 770 = 592900
Result: 644 * 644 = 414736
Result: 274 * 274 = 75076
Result: 261 * 261 = 68121
2017-06-02 19-18-46: Done!
```

`python task_workder.py`

```
Connect to Server 127.0.0.1
Worker 16671 start!
run task 965 * 965
run task 628 * 628
run task 635 * 635
run task 736 * 736
run task 995 * 995
run task 756 * 756
run task 770 * 770
run task 644 * 644
run task 274 * 274
run task 261 * 261
Worker 16671 Done!
```