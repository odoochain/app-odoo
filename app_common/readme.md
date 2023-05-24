当odoo渲染页面视图时，会调用tools.view_validation中的relaxng方法

通过app_relaxng的方法重载，先寻找本地rng。最关键是的etree.RelaxNG方法。

参考 https://blog.csdn.net/run_noob_vip/article/details/122804867