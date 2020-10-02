<!--
 * @Github: https://github.com/Certseeds/CS323-Compilers
 * @Organization: SUSTech
 * @Author: nanoseeds
 * @Date: 2020-10-02 22:48:23
 * @LastEditors: nanoseeds
 * @LastEditTime: 2020-10-02 23:06:43
 * @License: CC-BY-NC-SA_V4_0 or any later version 
 -->
### 
这个部分主要的目的是,使用flex和json,实现判断json是否合法.

通过`judge.sh`,调用`jsonparser_test.py`,对`data/`下的文件进行判断.

只判断哪些会出现语法分析阶段会出现的错误,  

并在error出现时使用形如`{ puts("*, recovered"); }`的方式来输出.

TODO在`syntax.y`中

目标在于`./judge.sh`之后,`Recovered/Total: x/x`