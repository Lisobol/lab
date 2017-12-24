$(function(){
    var from = $('#from');
    var to = $('#to');
    var func = $('#func');
    var button = $('#plot_button');
    var plot = $('#plot');
    $(onLoad);
    function onLoad(){
        var $button= $('.button')
    };

    button.click(function(e){
        e.preventDefault();

        var from1 = parseFloat(from.val());
        var to1 = parseFloat(to.val());
        const c = 0.1;
        var points = []
        for(var x = from1; x <= to1+c; x += c){
            points.push([x, eval(func.val())])
        }
        $.plot(plot, [points], {})

    });
    var options = {
        series: {
            lines: { show: true },
            points: { show: true }
        }
    };

    $.plot(placeholder, data, options);

})