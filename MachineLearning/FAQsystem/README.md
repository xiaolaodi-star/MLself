FAQ系统2.0版本
#使用的基本框架在https://zhuanlan.zhihu.com/p/216148298
##使用的Elasticsearch没有对其中索引进行压缩
原因：因为数据量比较少，检索的速度比较快就没有对检索进行压缩。
如果数据量比较大，可以考虑进行检索压缩