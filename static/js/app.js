/**
 * Created by yannis on 2017/10/11.
 */
$(function(){
    //alert(1)
    $("#friendlist li").click(function(){
        alert($(this).find("span").text())
    })
})