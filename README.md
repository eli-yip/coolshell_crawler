# coolshell_crawler

一个简单的对于coolshell的爬虫实现，非常丑陋，但是能用。

核心逻辑是从网站获取文章url，然后在从web archive中获取存档。技巧在于web archive会自动重定向，不需要我们获取全网址。

如果你只是需要pdf版本的文件，你可以直接通过markdown文件转换，如果需要markdown文件，可以在src/result.md或者release界面找到，不需要对web archive造成额外的服务器压力。

目前存在的问题是markdown文件代码块没有语言说明，这个问题是我采用的html2text库对于html文件中`<pre data-enlighter-language="shell" class="EnlighterJSRAW">`处理的不够完善导致的，后续有时间再调整一下，也欢迎pr。

最后，再次感谢陈皓老师对我技术的启蒙之恩，2013年遇见您是我最大的幸运！

Update:

苏洋大佬做了一份更好的，欢迎移步：

https://github.com/soulteary/forever-coolshell

R.I.P!