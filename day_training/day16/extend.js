/**
 * Created by Administrator on 2017/2/24 0024.
 */
//一般通过自执行函数拓展
(function (arg) {
    arg.extend({    //用于拓展jQuery的方法. 方式一：
        zcl: function () {
            return "丑";
        }
    });

    arg.fn.extend({　　 //方式二:
        alex: function () {
            return "better 丑";
        }
    });

})(jQuery);
