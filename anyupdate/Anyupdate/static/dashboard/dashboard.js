$(function () {
  var options = {
    alwaysShowResizeHandle: /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
  };
  $('.grid-stack').gridstack(options);
});

$(function () {
    $('.grid-stack').gridstack();
    var self = this;
    this.grid = $('.grid-stack').data('gridstack');

    var isInited = false;
    load();
    setInterval(function(){load()},30000);

    function load() {
        $.ajax({
            url: "/servicenow/apps/",
            dataType: "json",
            success: function(result){
                if(!isInited) {
                    var grid = $('.grid-stack').data('gridstack')
                    $('.grid-stack').on('added', function(event, items) {
                        for (var i = 0; i < items.length; i++) {
                            $(items[i].el[0]).attr('data-anijs', 'if: added, do: swing animated, after: $removeAnimations, on: $gridstack');
                        }
                        AniJS.run();
                        self.gridstackNotifier = AniJS.getNotifier('gridstack');
                        self.gridstackNotifier.dispatchEvent('added');
                    });
                    grid.movable('.grid-stack-item', false);
                    grid.resizable('.grid-stack-item', false);
                }
               result.forEach(function(app){
                    if(!isInited) {
                        initLoad(app, grid);
                    }
                    setupData(app);
               });

               result.forEach(function(app){
                    incidentEvent(app["configitem"], app["app_name"]);
               });
               isInited = true;
               //console.log(result);
             }
        });
    }

    function initLoad(app, grid) {
        var classtag = app["app_name"].replace(/\s+/g, "_");
        var id = app["app_name"].replace(" ", "_");
        grid.addWidget($('<div class="'+classtag+'"><div class="grid-stack-item-content" id='+id+'>'+app["app_name"]+'</div></div>'), app["Posx"]*2, app["Posy"], 2, app["Colspan"]*2);

        $('#'+id).hover(function(){
            $('#'+id).css({
                'box-shadow': '10px 10px 10px grey'
            })
        },function(){
            $('#'+id).css({
                'box-shadow': ''
            })
        });
    }

    function setupData(app) {
       var gridv = $("." + app["app_name"].replace(/\s+/g, "_") + " .grid-stack-item-content");
       var hasInc = false;
       var configitems = app["configitem"];
       var id = app["app_name"].replace(" ", "_");

       if (configitems.length > 0) {
            configitems.forEach(function(configitem){
                if(configitem["incs"].length > 0) {
                    hasInc = true;
                }
            });

           var gridtext = "<h3>" + app["app_name"] + "</h3>";
           if (hasInc) {
               gridv.css("background-color", "#A41914");
//               $('#'+id + ":not(.bound)").addClass('bound').bind("click", function(){
//                    window.open("/flow/");
//               });
           } else {
                gridv.css("background-color", "#34A417");
//                $('#'+id + ":not(.bound)").addClass('bound').unbind("click");
           }
           configitems.forEach(function(configitem) {
               if (hasInc) {
                    gridtext += setupIncidents(configitem["incs"], id);
               }
           });
//           gridtext += "<p>Last updated at:" + new Date() + "</p>";
           gridv.html(gridtext);


       }
    }

    function incidentEvent(configitems, appname) {
        hasInc = false;
        if (configitems.length > 0) {
            configitems.forEach(function(configitem){
                if(configitem["incs"].length > 0) {
                    hasInc = true;
                }
            });
            configitems.forEach(function(configitem) {
               if (hasInc) {
                    incs = configitem["incs"];
                    for(var i=0; i<incs.length; i++) {
                        inc = incs[i];
                        $('#'+inc["inc_id"]).hover(function(){
                            $(this).css({"background-color": "#ff0000"});
                            $('#'+appname).css({
                                'box-shadow': '10px 10px 10px red'
                            });
                            if (inc["parent"] != null) {
                                $('#' + inc["parent"]).css({"background-color": "#ff0000"});
                            }
                            if (inc["child"] != null) {
                                $('#' + inc["child"]).css({"background-color": "#ff0000"});
                            }
                        }, function(){
                            $(this).css({"background-color": "#A41914"});
                            if (inc["parent"] != null) {
                                $('#' + inc["parent"]).css({"background-color": "#A41914"});
                            }
                            if (inc["child"] != null) {
                                $('#' + inc["child"]).css({"background-color": "#A41914"});
                            }
                        });

                    }
               }
           });
        }
    }

    function setupIncidents(incs, appname) {
        var result = "";
        result += "<ul class='incidentlist'>";
        for(var i=0; i<incs.length; i++) {
            result += "<li id='"+ incs[i]["inc_id"] +"'>" + incs[i]["inc_id"] + ": " + incs[i]["short_desc"];
            if (incs[i].eta != null) {
                result += " ETA:" + incs[i].eta + "h";
            }
            result += "</li>";
        }
        result += "</ul>";
        return result
    }

    var animationHelper = AniJS.getHelper();

    //Defining removeAnimations to remove existing animations
    animationHelper.removeAnimations = function(e, animationContext){
         $('.grid-stack-item').attr('data-anijs', '');
    };
});