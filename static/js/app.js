/**
 * Created by yannis on 2017/10/11.
 */
$(function(){
    //alert(1)
    $("#friendlist li").click(function(){
        var puid=$(this).attr("puid");
        var type=$(this).attr("type");
        $.get("/bot/search/"+puid+","+type+"/",function(data){
            alert(data)
        })
    })
})
