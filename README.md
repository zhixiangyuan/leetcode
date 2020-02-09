# Leetcode 教程

项目为长期维护项目，目标是为 Leetcode 的每道题加上详细的解题方案。

本教程围绕 Leetcode 的题目，题目直接按照序号排序。

# 项目结构

```
project
    |- content                        // 存放相关教程 markdown 的文件夹
                                      // 文件夹下按照题目编号进行分类
                                      // 编号为 [1, 99] 的题目放在 1-99 的文件夹里
                                      // 编号为 [100, 199] 的题目放在 100-199 的文件夹里
                                      // 依次类推
    |- static                         // 图片之类的静态资源放到这里面
                                      // 内部的图片分类按照加入到文件夹的时间进行分类
    |- docs                           // 渲染出的 html 放到这里面
    |- script                         // 存放项目相关的脚本
        ｜- add_leetcode_question.py  // 用于生成新的题目模版
        ｜- add_lmage_to_blog.py      // 用于添加资源文件到 static 中
```

# 微信群交流群

![](/static/2020/February/1.jpeg)