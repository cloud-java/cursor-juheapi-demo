## 前言
今年 deepseek 异军突起，真是火出圈了。如果你还没开始尝试用 AI 助力开发，那么你要问自己一下——头发还好吗？

尽管你用过很多开发工具，但是我强烈推荐你，使用 cursor。比如我最近使用的 Cursor 软件，通过与 AI 的四五轮对话， 就快速构建了一个 H5 应用，我将其称之为 <font color=red>对话式开发</font>。 
也许你对 AI 编程还有怀疑，体验过你就会知道，它早已不再是早期段誉的六脉神剑——时灵时不灵，而是修炼大成后那种“心随剑动、无形胜有形”的境界。你只需要提出想法，它便能快速响应，无论是构建页面、生成代码，还是优化逻辑，都能迅速助力完成。

cursor 到底有什么优点呢，我们来说一下：
- <font color=red>五分钟即可完成环境搭建</font>
- <font color=red>3句话就能生成完整的项目架构</font>
- <font color=red>零基础也能快速上手</font>


cursor 有多强，下面我带大家来感受一下。

## 项目实例复现
我在[聚合数据官网](http://www.juhe.cn)看到了很多比较常用的 API 接口，今天我以<font color=red>聚合数据</font>的众多接口中的一个老黄历接口，来复现，如何通过这个接口，使用 cursor 来完成一个 H5 应用的生成。


---

## **安装 Cursor？**  

访问 [Cursor 官网](https://www.cursor.so) ,选择对应的版本（macOS、Windows 或 Linux），然后下载安装即可，非常简单，这里省略了。 

### 创建项目

![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578093490587345.png?x-oss-process=style/thumb)
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578090077754108.png?x-oss-process=style/thumb)
 ### 安装插件
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578098286754861.png?x-oss-process=style/thumb)
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578094231825394.png?x-oss-process=style/thumb)
<font color=red>提示：在以后的使用中，当你要求生成不同语言的代码的时候，如果是第一次，都会提示你安装对应的插件,你点击安装就可以了。</font>

### 创建开发笔记
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578092715178223.png?x-oss-process=style/thumb)
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578094666554980.png?x-oss-process=style/thumb)
具体内容如下：

![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578091825451069.png?x-oss-process=style/thumb)


### 后端接口服务
这里我使用的是 composer 功能，composer 就是用来生成代码的。
#### 输入需求

![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578090692802762.png?x-oss-process=style/thumb)
因为我们是第一次生成代码，所以可以直接选择接受所有的生成代码，当然你也可以点击每个文件的代码进行阅读后再决定是否接受
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578097034873110.png?x-oss-process=style/thumb)
#### 安装插件
下面点击 main.py文件后，会提示你是否安装 python 插件，我们点击接受安装
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578097958476327.png?x-oss-process=style/thumb)
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578092824356587.png?x-oss-process=style/thumb)
#### 安装依赖
打开控制台终端
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578094567129017.png?x-oss-process=style/thumb)
安装必要的python 依赖
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578099220186441.png?x-oss-process=style/thumb)
#### 运行后端服务
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578098622913607.png?x-oss-process=style/thumb)
这里显示运行成功
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578094090805245.png?x-oss-process=style/thumb)
 #### 测试后端接口
新开一个终端，测试后端接口，我这里运行的命令是
```python
curl http://localhost:8000/huangli/2025-01-01 |jq #jq是一个插件，用来格式化输出 json
```

![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578096933609741.png?x-oss-process=style/thumb)
这里显示 json 格式的数据，表示成功运行了，并且返回了预期的数据



### 编写前端开发需求
这里和编写开发后端需求类似，新建一个 notepad，然后添加内容，我的需求如下：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578090326491805.png?x-oss-process=style/thumb)
### 生成前端代码
在刚才的 composer 对话框中继续输入要求
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578099956815069.png?x-oss-process=style/thumb)
代码生成好之后，同样点击全部接受
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578091591052837.png?x-oss-process=style/thumb)
#### 安装依赖
在控制台中安装依赖
```shell
npm install
```
### 启动前端服务
```shell
npm run dev
```
如下，表示启动成功
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578095691250693.png?x-oss-process=style/thumb)
打开链接，看到如下内容
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578098648924593.png?x-oss-process=style/thumb)
表示已经成功运行了

### 前端页面优化
前端页面优化也不是我们去修改代码，也是让cursor帮我们进行优化，我们只需要说出自己的想法，或者给他参考示例，就可以进行。
比如，我看到页面颜色过于单一，我就输入以下对话内容：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578093847937465.png?x-oss-process=style/thumb)

第一次优化后的效果如下：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578099863234497.png?x-oss-process=style/thumb)



然后我又让修改了一下背景颜色，效果如下：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578099874506573.png?x-oss-process=style/thumb)


我发现日期控件下面的显示信息过于单一，于是又让优化了一下：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578094558198561.png?x-oss-process=style/thumb)





最终效果如下：
![image.png](https://statics.sdk.cn/articles/img/202502/1001009_794b7085d71578091374082960.png?x-oss-process=style/thumb)

## 总结
通过以上的演练可以发现，短短几轮对话，我们就可以快速的落地一个 H5 应用，这惊人的效率，敢问哪个程序员能赶上？

[聚合数据官网](http://www.juhe.cn)还有很多有趣的接口，你也可以浏览聚合数据官网，找几个你自己感兴趣的接口，快速体验一下吧。
