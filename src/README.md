# Leetcode 教程

项目为长期维护项目，愿景是制作最好的 Leetcode 题目解析。

本教程围绕 Leetcode 的题目，题目直接按照序号排序。

# 项目结构

todo 由于 Leetcode 目前的题目分类做了改变，本项目分类也将在将来改变分类方式

```
project
    |- docs                               // 渲染出的 html 放到这里面
    |- script                             // 存放项目相关的脚本
        |- add_leetcode_question.py       // 用于生成新的题目模版
        |- add_lmage_to_leetcode_blog.py  // 用于添加资源文件到 static 中
    |- src
        |- content                        // 存放相关教程 markdown 的文件夹，文件夹下按照题目编号进行分类
            |- 1-99                       // 编号为 [1, 99] 的题目放在 1-99 的文件夹里
            |- 100-199                    // 编号为 [100, 199] 的题目放在 100-199 的文件夹里
                                          // 依次类推
        |- static                         // 图片之类的静态资源放到这里面
                                          // 内部的图片分类按照加入到文件夹的时间进行分类                      
```

如果想在本地预览本项目请使用 terminal 进入 src 目录，然后运行 `gitbook serve` 即可。如果碰到安装 gitbook 插件安装不上的问题请参考[《如何安装 gitbook 插件》](https://zhixiangyuan.github.io/2020/02/10/%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85-gitbook-%E6%8F%92%E4%BB%B6/)。

# 微信群交流群

![](/static/2020/February/1.jpeg)