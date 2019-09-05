var colors = ['#edbd00','#367d85','#97ba4c','#f5662b','#3f3e47'];
var flowColors = ['#d6d6dba','#242429','#9f9fa3'];
d3.json("/data/", function(error, json) {
    var chart = d3.select("#chart").append("svg").chart("Sankey.Path");
    chart
      .name(label)
      .colorNodes(function(name, node) {
        return colors.pop();
      })
      .colorLinks(function(link) {
        return flowColors.pop();
      })
      .nodeWidth(40)
      .nodePadding(10)
      .spread(true)
      .iterations(0)
      .draw(json);
    function label(node) {
      return node.name.replace(/\s*\(.*?\)$/, '');
    }
});