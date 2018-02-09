if (window['cytoscape'] === undefined) {
    var paths = {
        cytoscape: 'https://raw.githubusercontent.com/cytoscape/cytoscape.js/master/dist/cytoscape.min.js'
    };

    require.config({
        paths: paths
    });

    require(['cytoscape'], function (cytoscape) {
        console.log('Loading Cytoscape.js Module...');
        window['cytoscape'] = cytoscape;

        var event = document.createEvent("HTMLEvents");
        event.initEvent("load_cytoscape", true, false);
        window.dispatchEvent(event);
    });
}
